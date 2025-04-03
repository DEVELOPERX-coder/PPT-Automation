# simple_md2pptx.py
import os
import re
import sys
import traceback
import yaml
from pathlib import Path

def parse_markdown(md_file):
    """Parse the markdown file into slide data."""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    slides = []
    settings = {}
    
    # Extract global settings if present
    if content.startswith('---'):
        end_index = content.find('---', 3)
        if end_index != -1:
            yaml_content = content[3:end_index].strip()
            try:
                settings = yaml.safe_load(yaml_content)
            except Exception as e:
                print(f"Warning: Could not parse global settings: {e}")
            content = content[end_index+3:].strip()
    
    # Split into slides by headings
    slide_blocks = re.split(r'\n\s*#\s+', content)
    if not content.lstrip().startswith('#'):
        slide_blocks = slide_blocks[1:]  # Skip non-slide content
    
    # Process each slide
    for block in slide_blocks:
        if not block.strip():
            continue
            
        # Get slide title
        title_match = re.match(r'([^\n]+)', block)
        title = title_match.group(1) if title_match else ""
        block = block[title_match.end():].strip() if title_match else block.strip()
        
        # Get slide settings
        slide_settings = {}
        settings_match = re.match(r'\{\s*(.*?)\s*\}', block, re.DOTALL)
        if settings_match:
            settings_str = settings_match.group(1)
            # Parse simple key-value settings
            for setting in re.finditer(r'(\w+)\s*:\s*("[^"]*"|[^,}\s][^,}]*)', settings_str):
                key = setting.group(1).strip()
                value = setting.group(2).strip()
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                slide_settings[key] = value
                
            block = block[settings_match.end():].strip()
        
        # Extract elements
        elements = []
        for element_match in re.finditer(r':::(\w+)(?:\[(.*?)\])?\s*\n((?:\{.*?\})?\s*[\s\S]*?)(?=\n:::|$)', block):
            element_type = element_match.group(1)
            inline_props = element_match.group(2) or ""
            element_content = element_match.group(3).strip()
            
            # Parse properties
            properties = {}
            
            # From inline props
            if inline_props:
                for prop in re.finditer(r'(\w+)\s*:\s*("[^"]*"|[^,\s][^,]*)', inline_props):
                    key, value = prop.group(1).strip(), prop.group(2).strip()
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]
                    properties[key] = value
            
            # From property block
            prop_block_match = re.match(r'\{\s*(.*?)\s*\}([\s\S]*)', element_content, re.DOTALL)
            if prop_block_match:
                prop_str = prop_block_match.group(1)
                for prop in re.finditer(r'(\w+)\s*:\s*("[^"]*"|[^,}\s][^,}]*)', prop_str):
                    key, value = prop.group(1).strip(), prop.group(2).strip()
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]
                    properties[key] = value
                    
                element_content = prop_block_match.group(2).strip()
            
            elements.append({
                'type': element_type, 
                'properties': properties,
                'content': element_content
            })
        
        slides.append({
            'title': title,
            'settings': slide_settings,
            'elements': elements
        })
    
    return slides, settings

def create_presentation(slides, settings, output_file):
    """Create PowerPoint presentation from slide data."""
    try:
        # Load required modules
        import win32com.client
        
        # Create PowerPoint application
        print("Starting PowerPoint...")
        ppt = win32com.client.Dispatch("PowerPoint.Application")
        ppt.Visible = True  # Make it visible for debugging
        
        # Create new presentation
        print("Creating presentation...")
        presentation = ppt.Presentations.Add()
        
        # Apply global settings
        if 'slide_width' in settings and 'slide_height' in settings:
            try:
                # Convert to points (1 inch = 72 points)
                w_match = re.match(r'(\d+(\.\d+)?)(in|cm|pt|px)?', str(settings['slide_width']))
                h_match = re.match(r'(\d+(\.\d+)?)(in|cm|pt|px)?', str(settings['slide_height']))
                
                if w_match and h_match:
                    w_num = float(w_match.group(1))
                    h_num = float(h_match.group(1))
                    
                    w_unit = w_match.group(3) or 'in'
                    h_unit = h_match.group(3) or 'in'
                    
                    # Convert to points
                    if w_unit == 'in': w_points = w_num * 72
                    elif w_unit == 'cm': w_points = w_num * 28.35
                    elif w_unit == 'pt': w_points = w_num
                    elif w_unit == 'px': w_points = w_num * 0.75
                    
                    if h_unit == 'in': h_points = h_num * 72
                    elif h_unit == 'cm': h_points = h_num * 28.35
                    elif h_unit == 'pt': h_points = h_num
                    elif h_unit == 'px': h_points = h_num * 0.75
                    
                    presentation.PageSetup.SlideWidth = w_points
                    presentation.PageSetup.SlideHeight = h_points
            except Exception as e:
                print(f"Warning: Could not set slide dimensions: {e}")
        
        # Process each slide
        print(f"Adding {len(slides)} slides...")
        for i, slide_data in enumerate(slides):
            # Get layout
            layout_name = slide_data['settings'].get('layout', 'Blank').lower()
            layout_idx = 6  # Default to blank
            
            if layout_name == 'title slide': layout_idx = 0
            elif layout_name == 'title and content': layout_idx = 1
            elif layout_name == 'section header': layout_idx = 2
            elif layout_name == 'two content': layout_idx = 3
            elif layout_name == 'comparison': layout_idx = 4
            elif layout_name == 'title only': layout_idx = 5
            elif layout_name == 'blank': layout_idx = 6
            elif layout_name == 'content with caption': layout_idx = 7
            elif layout_name == 'picture with caption': layout_idx = 8
            
            # Add slide
            slide = presentation.Slides.Add(i+1, layout_idx+1)
            print(f"  Slide {i+1}: {slide_data['title']} - Layout: {layout_name}")
            
            # Set title if layout has title
            if slide.Shapes.HasTitle and slide_data['title']:
                slide.Shapes.Title.TextFrame.TextRange.Text = slide_data['title']
            
            # Set background
            if 'background' in slide_data['settings']:
                bg_color = slide_data['settings']['background']
                if bg_color.startswith('#'):
                    # Convert hex to RGB
                    hex_color = bg_color.lstrip('#')
                    if len(hex_color) == 6:
                        r = int(hex_color[0:2], 16)
                        g = int(hex_color[2:4], 16)
                        b = int(hex_color[4:6], 16)
                        rgb = r + (g << 8) + (b << 16)
                        
                        slide.Background.Fill.Visible = True
                        slide.Background.Fill.Solid()
                        slide.Background.Fill.ForeColor.RGB = rgb
            
            # Process elements
            for element in slide_data['elements']:
                element_type = element['type'].lower()
                properties = element['properties']
                content = element['content']
                
                # Basic position and size parsing
                left = 72  # Default 1 inch
                top = 72   # Default 1 inch
                width = 288  # Default 4 inches
                height = 72  # Default 1 inch
                
                if 'x' in properties:
                    x_match = re.match(r'(\d+(\.\d+)?)(in|cm|pt|px)?', str(properties['x']))
                    if x_match:
                        x_num = float(x_match.group(1))
                        x_unit = x_match.group(3) or 'in'
                        if x_unit == 'in': left = x_num * 72
                        elif x_unit == 'cm': left = x_num * 28.35
                        elif x_unit == 'pt': left = x_num
                        elif x_unit == 'px': left = x_num * 0.75
                
                if 'y' in properties:
                    y_match = re.match(r'(\d+(\.\d+)?)(in|cm|pt|px)?', str(properties['y']))
                    if y_match:
                        y_num = float(y_match.group(1))
                        y_unit = y_match.group(3) or 'in'
                        if y_unit == 'in': top = y_num * 72
                        elif y_unit == 'cm': top = y_num * 28.35
                        elif y_unit == 'pt': top = y_num
                        elif y_unit == 'px': top = y_num * 0.75
                
                if 'width' in properties:
                    w_match = re.match(r'(\d+(\.\d+)?)(in|cm|pt|px)?', str(properties['width']))
                    if w_match:
                        w_num = float(w_match.group(1))
                        w_unit = w_match.group(3) or 'in'
                        if w_unit == 'in': width = w_num * 72
                        elif w_unit == 'cm': width = w_num * 28.35
                        elif w_unit == 'pt': width = w_num
                        elif w_unit == 'px': width = w_num * 0.75
                
                if 'height' in properties:
                    h_match = re.match(r'(\d+(\.\d+)?)(in|cm|pt|px)?', str(properties['height']))
                    if h_match:
                        h_num = float(h_match.group(1))
                        h_unit = h_match.group(3) or 'in'
                        if h_unit == 'in': height = h_num * 72
                        elif h_unit == 'cm': height = h_num * 28.35
                        elif h_unit == 'pt': height = h_num
                        elif h_unit == 'px': height = h_num * 0.75
                
                # Add element based on type
                if element_type == 'text':
                    shape = slide.Shapes.AddTextbox(1, left, top, width, height)
                    shape.TextFrame.TextRange.Text = content
                    
                    # Apply text formatting
                    if 'font' in properties:
                        shape.TextFrame.TextRange.Font.Name = properties['font']
                    
                    if 'font_size' in properties:
                        try:
                            size = float(properties['font_size'])
                            shape.TextFrame.TextRange.Font.Size = size
                        except:
                            pass
                    
                    if 'font_color' in properties:
                        color = properties['font_color']
                        if color.startswith('#'):
                            hex_color = color.lstrip('#')
                            if len(hex_color) == 6:
                                r = int(hex_color[0:2], 16)
                                g = int(hex_color[2:4], 16)
                                b = int(hex_color[4:6], 16)
                                rgb = r + (g << 8) + (b << 16)
                                shape.TextFrame.TextRange.Font.Color.RGB = rgb
                    
                    if 'bold' in properties and properties['bold'].lower() in ['true', '1', 'yes']:
                        shape.TextFrame.TextRange.Font.Bold = True
                    
                    if 'italic' in properties and properties['italic'].lower() in ['true', '1', 'yes']:
                        shape.TextFrame.TextRange.Font.Italic = True
                    
                    if 'align' in properties:
                        align = properties['align'].lower()
                        if align == 'center':
                            shape.TextFrame.TextRange.ParagraphFormat.Alignment = 2  # Center
                        elif align == 'right':
                            shape.TextFrame.TextRange.ParagraphFormat.Alignment = 3  # Right
                        elif align == 'justify':
                            shape.TextFrame.TextRange.ParagraphFormat.Alignment = 4  # Justify
                
                elif element_type == 'shape':
                    # Map shape type
                    shape_type = properties.get('shape_type', 'rectangle').lower()
                    shape_map = {
                        'rectangle': 1,
                        'rounded_rectangle': 5,
                        'oval': 9,
                        'triangle': 6,
                        'diamond': 4
                    }
                    shape_id = shape_map.get(shape_type, 1)
                    
                    # Create shape
                    shape = slide.Shapes.AddShape(shape_id, left, top, width, height)
                    
                    # Add text if present
                    if content:
                        shape.TextFrame.TextRange.Text = content
                    
                    # Set fill color
                    if 'fill' in properties:
                        fill_color = properties['fill']
                        if fill_color.startswith('#'):
                            hex_color = fill_color.lstrip('#')
                            if len(hex_color) == 6:
                                r = int(hex_color[0:2], 16)
                                g = int(hex_color[2:4], 16)
                                b = int(hex_color[4:6], 16)
                                rgb = r + (g << 8) + (b << 16)
                                
                                shape.Fill.Visible = True
                                shape.Fill.Solid()
                                shape.Fill.ForeColor.RGB = rgb
                    
                    # Set border
                    if 'border_color' in properties:
                        border_color = properties['border_color']
                        if border_color.startswith('#'):
                            hex_color = border_color.lstrip('#')
                            if len(hex_color) == 6:
                                r = int(hex_color[0:2], 16)
                                g = int(hex_color[2:4], 16)
                                b = int(hex_color[4:6], 16)
                                rgb = r + (g << 8) + (b << 16)
                                
                                shape.Line.Visible = True
                                shape.Line.ForeColor.RGB = rgb
                    
                    # Text formatting (for shapes with text)
                    if content:
                        if 'font' in properties:
                            shape.TextFrame.TextRange.Font.Name = properties['font']
                        
                        if 'font_size' in properties:
                            try:
                                size = float(properties['font_size'])
                                shape.TextFrame.TextRange.Font.Size = size
                            except:
                                pass
                        
                        if 'font_color' in properties:
                            color = properties['font_color']
                            if color.startswith('#'):
                                hex_color = color.lstrip('#')
                                if len(hex_color) == 6:
                                    r = int(hex_color[0:2], 16)
                                    g = int(hex_color[2:4], 16)
                                    b = int(hex_color[4:6], 16)
                                    rgb = r + (g << 8) + (b << 16)
                                    shape.TextFrame.TextRange.Font.Color.RGB = rgb
                        
                        if 'align' in properties:
                            align = properties['align'].lower()
                            if align == 'center':
                                shape.TextFrame.TextRange.ParagraphFormat.Alignment = 2  # Center
                            elif align == 'right':
                                shape.TextFrame.TextRange.ParagraphFormat.Alignment = 3  # Right
                
                # We could add more element types here (image, table, etc.)
                
        # Save the presentation
        output_path = os.path.abspath(output_file)
        print(f"Saving presentation to: {output_path}")
        presentation.SaveAs(output_path)
        print(f"Presentation saved successfully to: {output_path}")
        
        # Don't close PowerPoint automatically
        # ppt.Quit()
        
        return True
        
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        print("\nDetailed error information:")
        traceback.print_exc()
        print("\nPossible solutions:")
        print("1. Make sure Microsoft PowerPoint is installed")
        print("2. Try running: pip install --upgrade pywin32")
        print("3. If using a virtual environment, make sure to run: python -m pywin32_postinstall -install")
        return False

def main():
    """Main function to process command line arguments and execute the conversion."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert Markdown to PowerPoint')
    parser.add_argument('input_file', help='Input Markdown file')
    parser.add_argument('-o', '--output', help='Output PowerPoint file')
    
    args = parser.parse_args()
    
    # Validate input file
    if not os.path.exists(args.input_file):
        print(f"Error: Input file '{args.input_file}' not found.")
        return 1
    
    # Determine output file
    output_file = args.output
    if not output_file:
        input_path = Path(args.input_file)
        output_file = str(input_path.with_suffix('.pptx'))
    
    # Parse markdown
    print(f"Parsing {args.input_file}...")
    slides, settings = parse_markdown(args.input_file)
    print(f"Found {len(slides)} slides")
    
    # Create PowerPoint
    if create_presentation(slides, settings, output_file):
        print("\nSUCCESS: Converted markdown to PowerPoint")
        return 0
    else:
        print("\nFAILED: Could not create PowerPoint presentation")
        return 1

if __name__ == "__main__":
    sys.exit(main())