#!/usr/bin/env python3
"""
MD2PPTX - Markdown to PowerPoint Converter

This script converts a specially formatted Markdown file into a PowerPoint presentation.
It supports advanced PowerPoint features like precise positioning, formatting, animations, and more.
"""

import os
import re
import argparse
import yaml
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt, Cm
from pptx.enum.text import PP_ALIGN, MSO_VERTICAL_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from pptx.enum.dml import MSO_THEME_COLOR
from pptx.enum.action import PP_ACTION
from pptx.enum.animation import PP_ANIMATION_TYPE, PP_ANIMATION_EFFECT

class MarkdownParser:
    """Parse the markdown file and extract PowerPoint elements."""
    
    def __init__(self, md_file):
        """Initialize the parser with a markdown file."""
        self.md_file = md_file
        self.content = self._read_file()
        self.slides = []
        self.global_settings = {}
    
    def _read_file(self):
        """Read the markdown file content."""
        with open(self.md_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def parse(self):
        """Parse the markdown content into slide data."""
        # Extract global settings if present
        if self.content.startswith('---'):
            end_index = self.content.find('---', 3)
            if end_index != -1:
                yaml_content = self.content[3:end_index].strip()
                try:
                    self.global_settings = yaml.safe_load(yaml_content)
                except yaml.YAMLError:
                    print("Warning: Could not parse global settings YAML.")
                self.content = self.content[end_index+3:].strip()
        
        # Split content into slides
        slide_blocks = re.split(r'\n#{1,2} ', self.content)
        if slide_blocks[0].strip() == '':
            slide_blocks = slide_blocks[1:]
        else:
            # If the file doesn't start with a heading, treat the first block as content
            slide_blocks[0] = '# ' + slide_blocks[0]
        
        # Process each slide block
        for block in slide_blocks:
            if block.strip():
                slide_data = self._parse_slide(block)
                self.slides.append(slide_data)
        
        return self.slides, self.global_settings
    
    def _parse_slide(self, block):
        """Parse a single slide block."""
        lines = block.split('\n')
        slide_title = lines[0].lstrip('#').strip()
        
        # Extract slide-specific YAML if present
        slide_settings = {}
        content_start = 1
        if len(lines) > 1 and lines[1].strip() == '{':
            end_brace_index = block.find('}', block.find('{'))
            if end_brace_index != -1:
                yaml_text = block[block.find('{')+1:end_brace_index].strip()
                try:
                    slide_settings = yaml.safe_load(yaml_text)
                except yaml.YAMLError:
                    print(f"Warning: Could not parse slide settings for slide '{slide_title}'")
                
                # Find where content starts after the YAML block
                content_start = 0
                for i, line in enumerate(lines):
                    if '}' in line:
                        content_start = i + 1
                        break
        
        # Extract content elements
        elements = []
        current_element = None
        
        i = content_start
        while i < len(lines):
            line = lines[i]
            
            # Check for element definition
            if line.startswith(':::'):
                # Save previous element if exists
                if current_element:
                    elements.append(current_element)
                
                # Start new element
                element_type = line.lstrip(':').strip()
                current_element = {'type': element_type, 'content': '', 'properties': {}}
                
                # Check if element has inline properties
                if '[' in element_type and ']' in element_type:
                    props_text = element_type[element_type.find('[')+1:element_type.find(']')]
                    current_element['type'] = element_type[:element_type.find('[')].strip()
                    
                    # Parse properties
                    try:
                        props_dict = {}
                        for prop in props_text.split(','):
                            if ':' in prop:
                                key, value = prop.split(':', 1)
                                props_dict[key.strip()] = value.strip()
                        current_element['properties'] = props_dict
                    except Exception:
                        print(f"Warning: Could not parse element properties: {props_text}")
            
            # Check for element property block
            elif line.startswith('{') and '}' in line and current_element:
                prop_text = line.strip()[1:-1]  # Remove { and }
                try:
                    for prop in prop_text.split(','):
                        if ':' in prop:
                            key, value = prop.split(':', 1)
                            current_element['properties'][key.strip()] = value.strip()
                except Exception:
                    print(f"Warning: Could not parse element property: {prop_text}")
            
            # Otherwise it's content for the current element or slide
            elif current_element:
                if current_element['content']:
                    current_element['content'] += '\n'
                current_element['content'] += line
            
            i += 1
        
        # Add the last element if exists
        if current_element:
            elements.append(current_element)
        
        return {
            'title': slide_title,
            'settings': slide_settings,
            'elements': elements
        }


class PowerPointGenerator:
    """Generate a PowerPoint presentation from parsed markdown data."""
    
    def __init__(self, slides_data, global_settings):
        """Initialize the generator with slide data and settings."""
        self.slides_data = slides_data
        self.global_settings = global_settings
        self.prs = Presentation()
        self._apply_global_settings()
    
    def _apply_global_settings(self):
        """Apply global presentation settings."""
        if 'slide_width' in self.global_settings and 'slide_height' in self.global_settings:
            try:
                width = self._parse_dimension(self.global_settings['slide_width'])
                height = self._parse_dimension(self.global_settings['slide_height'])
                self.prs.slide_width = width
                self.prs.slide_height = height
            except ValueError:
                print("Warning: Invalid slide dimensions in global settings.")
    
    def _parse_dimension(self, value):
        """Parse dimension values with units (inches, cm, etc.)."""
        if isinstance(value, (int, float)):
            return Inches(value)
        
        value = str(value).strip().lower()
        match = re.match(r'(\d+(\.\d+)?)(in|cm|pt|px)?', value)
        if match:
            num = float(match.group(1))
            unit = match.group(3) or 'in'  # Default to inches
            
            if unit == 'in':
                return Inches(num)
            elif unit == 'cm':
                return Cm(num)
            elif unit == 'pt':
                return Pt(num)
            elif unit == 'px':
                # Approximate conversion from pixels to points
                return Pt(num * 0.75)
        
        raise ValueError(f"Cannot parse dimension: {value}")
    
    def _parse_color(self, color_str):
        """Parse color strings (RGB, hex, or named)."""
        color_str = str(color_str).strip().lower()
        
        # Check for RGB format
        rgb_match = re.match(r'rgb\((\d+),\s*(\d+),\s*(\d+)\)', color_str)
        if rgb_match:
            r, g, b = map(int, rgb_match.groups())
            return RGBColor(r, g, b)
        
        # Check for hex format
        hex_match = re.match(r'#?([0-9a-f]{6})', color_str)
        if hex_match:
            hex_value = hex_match.group(1)
            r = int(hex_value[0:2], 16)
            g = int(hex_value[2:4], 16)
            b = int(hex_value[4:6], 16)
            return RGBColor(r, g, b)
        
        # Common color names
        color_map = {
            'black': RGBColor(0, 0, 0),
            'white': RGBColor(255, 255, 255),
            'red': RGBColor(255, 0, 0),
            'green': RGBColor(0, 128, 0),
            'blue': RGBColor(0, 0, 255),
            'yellow': RGBColor(255, 255, 0),
            'purple': RGBColor(128, 0, 128),
            'orange': RGBColor(255, 165, 0),
            'gray': RGBColor(128, 128, 128),
        }
        
        if color_str in color_map:
            return color_map[color_str]
        
        # Default
        print(f"Warning: Could not parse color '{color_str}', using black")
        return RGBColor(0, 0, 0)
    
    def _get_alignment(self, align_str):
        """Convert alignment string to PowerPoint alignment enum."""
        align_map = {
            'left': PP_ALIGN.LEFT,
            'center': PP_ALIGN.CENTER,
            'right': PP_ALIGN.RIGHT,
            'justify': PP_ALIGN.JUSTIFY,
            'top': MSO_VERTICAL_ANCHOR.TOP,
            'middle': MSO_VERTICAL_ANCHOR.MIDDLE,
            'bottom': MSO_VERTICAL_ANCHOR.BOTTOM
        }
        
        align_str = str(align_str).strip().lower()
        if align_str in align_map:
            return align_map[align_str]
        
        # Default horizontal alignment
        if align_str in ['h-left', 'h-center', 'h-right', 'h-justify']:
            return align_map[align_str[2:]]
        
        # Default vertical alignment
        if align_str in ['v-top', 'v-middle', 'v-bottom']:
            return align_map[align_str[2:]]
        
        print(f"Warning: Unknown alignment '{align_str}'")
        return None
    
    def _apply_shape_style(self, shape, properties):
        """Apply styling properties to a shape."""
        # Position and size
        if 'x' in properties:
            shape.left = self._parse_dimension(properties['x'])
        if 'y' in properties:
            shape.top = self._parse_dimension(properties['y'])
        if 'width' in properties:
            shape.width = self._parse_dimension(properties['width'])
        if 'height' in properties:
            shape.height = self._parse_dimension(properties['height'])
        
        # Fill
        if 'fill' in properties:
            fill_color = self._parse_color(properties['fill'])
            shape.fill.solid()
            shape.fill.fore_color.rgb = fill_color
        
        # Line/border
        if 'border_color' in properties:
            border_color = self._parse_color(properties['border_color'])
            shape.line.color.rgb = border_color
        if 'border_width' in properties:
            shape.line.width = self._parse_dimension(properties['border_width'])
        if 'border_style' in properties:
            # Would require mapping to line style enums
            pass
        
        # Transparency
        if 'transparency' in properties:
            try:
                trans_value = float(properties['transparency'])
                if 0 <= trans_value <= 1:
                    shape.fill.transparency = trans_value
            except ValueError:
                print(f"Warning: Invalid transparency value: {properties['transparency']}")
        
        # Shadow
        # (python-pptx has limited shadow support)
        
        # Rotation
        if 'rotation' in properties:
            try:
                rotation = float(properties['rotation'])
                shape.rotation = rotation
            except ValueError:
                print(f"Warning: Invalid rotation value: {properties['rotation']}")
        
        # Animation (limited support in python-pptx)
        # This would require COM automation or more advanced libraries
        
        return shape
    
    def _apply_text_style(self, text_frame, properties):
        """Apply styling properties to a text frame."""
        # Alignment
        if 'align' in properties:
            alignment = self._get_alignment(properties['align'])
            if alignment in [PP_ALIGN.LEFT, PP_ALIGN.CENTER, PP_ALIGN.RIGHT, PP_ALIGN.JUSTIFY]:
                for paragraph in text_frame.paragraphs:
                    paragraph.alignment = alignment
        
        if 'vertical_align' in properties:
            v_alignment = self._get_alignment(properties['vertical_align'])
            if v_alignment in [MSO_VERTICAL_ANCHOR.TOP, MSO_VERTICAL_ANCHOR.MIDDLE, MSO_VERTICAL_ANCHOR.BOTTOM]:
                text_frame.vertical_anchor = v_alignment
        
        # Margins
        if 'margin_left' in properties:
            text_frame.margin_left = self._parse_dimension(properties['margin_left'])
        if 'margin_right' in properties:
            text_frame.margin_right = self._parse_dimension(properties['margin_right'])
        if 'margin_top' in properties:
            text_frame.margin_top = self._parse_dimension(properties['margin_top'])
        if 'margin_bottom' in properties:
            text_frame.margin_bottom = self._parse_dimension(properties['margin_bottom'])
        
        # Font properties (applied to all runs in all paragraphs)
        for paragraph in text_frame.paragraphs:
            for run in paragraph.runs:
                # Font family
                if 'font' in properties:
                    run.font.name = properties['font']
                
                # Font size
                if 'font_size' in properties:
                    try:
                        size_value = properties['font_size']
                        if isinstance(size_value, (int, float)):
                            run.font.size = Pt(size_value)
                        else:
                            # Strip 'pt' suffix if present
                            size_str = str(size_value).lower()
                            if size_str.endswith('pt'):
                                size_str = size_str[:-2]
                            run.font.size = Pt(float(size_str))
                    except ValueError:
                        print(f"Warning: Invalid font size: {properties['font_size']}")
                
                # Font color
                if 'font_color' in properties:
                    color = self._parse_color(properties['font_color'])
                    run.font.color.rgb = color
                
                # Font style
                if 'bold' in properties and properties['bold'].lower() in ['true', '1', 'yes']:
                    run.font.bold = True
                if 'italic' in properties and properties['italic'].lower() in ['true', '1', 'yes']:
                    run.font.italic = True
                if 'underline' in properties and properties['underline'].lower() in ['true', '1', 'yes']:
                    run.font.underline = True
        
        return text_frame
    
    def _add_text_element(self, slide, content, properties):
        """Add a text element to the slide."""
        x = self._parse_dimension(properties.get('x', '1in'))
        y = self._parse_dimension(properties.get('y', '1in'))
        width = self._parse_dimension(properties.get('width', '8in'))
        height = self._parse_dimension(properties.get('height', '1in'))
        
        textbox = slide.shapes.add_textbox(x, y, width, height)
        textbox.text_frame.text = content
        
        # Apply styling
        self._apply_shape_style(textbox, properties)
        self._apply_text_style(textbox.text_frame, properties)
        
        return textbox
    
    def _add_image_element(self, slide, content, properties):
        """Add an image element to the slide."""
        x = self._parse_dimension(properties.get('x', '1in'))
        y = self._parse_dimension(properties.get('y', '1in'))
        width = self._parse_dimension(properties.get('width', '3in'))
        height = self._parse_dimension(properties.get('height', '3in'))
        
        image_path = content.strip()
        if os.path.exists(image_path):
            picture = slide.shapes.add_picture(image_path, x, y, width, height)
            self._apply_shape_style(picture, properties)
            return picture
        else:
            print(f"Warning: Image file not found: {image_path}")
            return None
    
    def _add_shape_element(self, slide, content, properties):
        """Add a shape element to the slide."""
        x = self._parse_dimension(properties.get('x', '1in'))
        y = self._parse_dimension(properties.get('y', '1in'))
        width = self._parse_dimension(properties.get('width', '2in'))
        height = self._parse_dimension(properties.get('height', '2in'))
        
        shape_type = properties.get('shape_type', 'rectangle').lower()
        shape_map = {
            'rectangle': MSO_SHAPE.RECTANGLE,
            'oval': MSO_SHAPE.OVAL,
            'rounded_rectangle': MSO_SHAPE.ROUNDED_RECTANGLE,
            'triangle': MSO_SHAPE.TRIANGLE,
            'right_triangle': MSO_SHAPE.RIGHT_TRIANGLE,
            'diamond': MSO_SHAPE.DIAMOND,
            'pentagon': MSO_SHAPE.PENTAGON,
            'hexagon': MSO_SHAPE.HEXAGON,
            'star': MSO_SHAPE.STAR_5_POINTS,
            'arrow': MSO_SHAPE.ARROW,
            # Add more shapes as needed
        }
        
        shape_enum = shape_map.get(shape_type, MSO_SHAPE.RECTANGLE)
        shape = slide.shapes.add_shape(shape_enum, x, y, width, height)
        
        # Add text if provided
        if content.strip():
            shape.text_frame.text = content
            self._apply_text_style(shape.text_frame, properties)
        
        # Apply styling
        self._apply_shape_style(shape, properties)
        
        return shape
    
    def _add_chart_element(self, slide, content, properties):
        """Add a chart element to the slide."""
        # This would require more complex parsing of chart data
        # python-pptx does support charts, but the implementation is complex
        print("Warning: Chart element is not fully implemented yet")
        
        # Placeholder for chart implementation
        x = self._parse_dimension(properties.get('x', '1in'))
        y = self._parse_dimension(properties.get('y', '1in'))
        width = self._parse_dimension(properties.get('width', '6in'))
        height = self._parse_dimension(properties.get('height', '4in'))
        
        textbox = slide.shapes.add_textbox(x, y, width, height)
        textbox.text_frame.text = f"Chart placeholder: {content}"
        
        return textbox
    
    def _add_table_element(self, slide, content, properties):
        """Add a table element to the slide."""
        x = self._parse_dimension(properties.get('x', '1in'))
        y = self._parse_dimension(properties.get('y', '1in'))
        
        # Parse table content
        rows = content.strip().split('\n')
        if not rows:
            print("Warning: Empty table content")
            return None
        
        # Split rows into cells
        table_data = []
        for row in rows:
            if row.strip().startswith('|') and row.strip().endswith('|'):
                # Markdown table format
                cells = row.strip().strip('|').split('|')
                table_data.append([cell.strip() for cell in cells])
            else:
                # Simple CSV-like format
                cells = row.split(',')
                table_data.append([cell.strip() for cell in cells])
        
        if not table_data:
            print("Warning: Could not parse table data")
            return None
        
        # Create table
        cols = len(table_data[0])
        rows = len(table_data)
        width = self._parse_dimension(properties.get('width', '6in'))
        height = self._parse_dimension(properties.get('height', f"{rows}in"))
        
        table = slide.shapes.add_table(rows, cols, x, y, width, height)
        
        # Populate table cells
        for row_idx, row_data in enumerate(table_data):
            for col_idx, cell_text in enumerate(row_data):
                if col_idx < cols:  # Ensure we don't exceed column count
                    cell = table.table.cell(row_idx, col_idx)
                    cell.text = cell_text
        
        # Apply styling
        self._apply_shape_style(table, properties)
        
        # Apply cell-specific styling (limited in python-pptx)
        
        return table
    
    def _add_slide_elements(self, slide, elements, slide_settings):
        """Add all elements to a slide."""
        for element in elements:
            element_type = element['type'].lower()
            content = element['content']
            properties = element['properties']
            
            # Merge with slide settings if applicable
            merged_properties = slide_settings.copy()
            merged_properties.update(properties)
            
            try:
                if element_type == 'text':
                    self._add_text_element(slide, content, merged_properties)
                elif element_type == 'image':
                    self._add_image_element(slide, content, merged_properties)
                elif element_type == 'shape':
                    self._add_shape_element(slide, content, merged_properties)
                elif element_type == 'chart':
                    self._add_chart_element(slide, content, merged_properties)
                elif element_type == 'table':
                    self._add_table_element(slide, content, merged_properties)
                else:
                    print(f"Warning: Unknown element type '{element_type}'")
            except Exception as e:
                print(f"Error adding {element_type} element: {e}")
    
    def _apply_slide_background(self, slide, settings):
        """Apply background settings to a slide."""
        if 'background' in settings:
            bg_fill = slide.background.fill
            bg_value = settings['background']
            
            # Check if it's a color
            try:
                bg_color = self._parse_color(bg_value)
                bg_fill.solid()
                bg_fill.fore_color.rgb = bg_color
            except:
                # Check if it's an image path
                if os.path.exists(bg_value):
                    # python-pptx doesn't directly support background images
                    # This would require more complex handling
                    print(f"Warning: Background images not fully supported: {bg_value}")
                else:
                    print(f"Warning: Invalid background specification: {bg_value}")
    
    def _apply_slide_transition(self, slide, settings):
        """Apply transition settings to a slide."""
        # Note: python-pptx doesn't directly support slide transitions
        # This would require COM automation or more advanced libraries
        if 'transition' in settings:
            print(f"Info: Slide transitions not fully supported: {settings['transition']}")
    
    def generate(self):
        """Generate the PowerPoint presentation from the parsed data."""
        for slide_data in self.slides_data:
            # Determine slide layout based on settings
            layout_name = slide_data['settings'].get('layout', 'Title and Content')
            layout = None
            
            # Try to find the requested layout
            for layout_obj in self.prs.slide_layouts:
                if layout_obj.name.lower() == layout_name.lower():
                    layout = layout_obj
                    break
            
            # Fall back to default if not found
            if not layout:
                layout = self.prs.slide_layouts[1]  # Title and Content is usually index 1
            
            # Create the slide
            slide = self.prs.slides.add_slide(layout)
            
            # Set slide title if the layout has a title placeholder
            if hasattr(slide, 'shapes') and hasattr(slide.shapes, 'title') and slide.shapes.title:
                slide.shapes.title.text = slide_data['title']
            
            # Apply slide background
            self._apply_slide_background(slide, slide_data['settings'])
            
            # Apply slide transition
            self._apply_slide_transition(slide, slide_data['settings'])
            
            # Add slide elements
            self._add_slide_elements(slide, slide_data['elements'], slide_data['settings'])
        
        return self.prs
    
    def save(self, output_file):
        """Save the generated presentation to a file."""
        self.prs.save(output_file)
        print(f"Presentation saved to: {output_file}")


def main():
    """Main function to process command line arguments and execute the conversion."""
    parser = argparse.ArgumentParser(description='Convert Markdown to PowerPoint')
    parser.add_argument('input_file', help='Input Markdown file')
    parser.add_argument('-o', '--output', help='Output PowerPoint file')
    parser.add_argument('-g', '--generate-readme', action='store_true', 
                        help='Generate README.md with syntax documentation')
    
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
    parser = MarkdownParser(args.input_file)
    slides_data, global_settings = parser.parse()
    
    # Generate PowerPoint
    generator = PowerPointGenerator(slides_data, global_settings)
    generator.generate()
    generator.save(output_file)
    
    # Generate README if requested
    if args.generate_readme:
        generate_readme()
    
    return 0


def generate_readme():
    """Generate README.md file with syntax documentation."""
    readme_content = """# Markdown to PowerPoint Converter

This tool converts specially formatted Markdown files into feature-rich PowerPoint presentations.
It supports a wide range of PowerPoint features including precise element positioning, 
formatting, animations, and more.

## Installation

```bash
pip install python-pptx pyyaml
```

## Usage

```bash
python md2pptx.py input.md -o output.pptx
```

## Markdown Syntax

The converter uses a specialized Markdown format that includes YAML-style properties and custom
element tags to describe PowerPoint features.

### Global Settings

At the top of your Markdown file, you can specify global presentation settings using YAML frontmatter:

```markdown
---
slide_width: 10in
slide_height: 7.5in
default_font: Arial
default_font_size: 18
---
```

### Slide Structure

Each slide begins with a level 1 or 2 heading:

```markdown
# Slide Title
```

### Slide Settings

You can specify slide-specific settings immediately after the slide title:

```markdown
# Slide Title
{
    layout: "Title and Content",
    background: "#FFFFFF",
    transition: "fade"
}
```

### Elements

Elements are defined using triple colon syntax followed by the element type:

```markdown
:::text
This is a text box
:::
```

Elements can have properties specified in brackets:

```markdown
:::text[x:1in, y:2in, width:4in, height:2in]
This is a positioned text box
:::
```

Or with a separate property block:

```markdown
:::text
{x:1in, y:2in, width:4in, height:2in, font_size:24, font_color:blue}
This is a styled text box
:::
```

### Element Types

#### Text

```markdown
:::text
{x:1in, y:1in, width:8in, height:2in, font:"Arial", font_size:24, font_color:"#FF0000", align:center}
This is a styled text box
:::
```

#### Images

```markdown
:::image
{x:2in, y:3in, width:4in, height:3in}
/path/to/image.jpg
:::
```

#### Shapes

```markdown
:::shape
{x:1in, y:1in, width:2in, height:2in, shape_type:oval, fill:"#0000FF", border_color:"#000000", border_width:2pt}
Text inside shape
:::
```

#### Tables

```markdown
:::table
{x:1in, y:1in, width:8in, height:3in}
Header 1, Header 2, Header 3
Cell 1, Cell 2, Cell 3
Cell 4, Cell 5, Cell 6
:::
```

Or using Markdown table syntax:

```markdown
:::table
{x:1in, y:1in, width:8in, height:3in}
| Header 1 | Header 2 | Header 3 |
| Cell 1 | Cell 2 | Cell 3 |
| Cell 4 | Cell 5 | Cell 6 |
:::
```

#### Charts (Basic Support)

```markdown
:::chart
{x:1in, y:1in, width:6in, height:4in, chart_type:bar}
Category 1, 10
Category 2, 15
Category 3, 7
Category 4, 12
:::
```

## Property Reference

### Global Settings Properties

- `slide_width`: Width of all slides (e.g., "10in", "25.4cm")
- `slide_height`: Height of all slides (e.g., "7.5in", "19.05cm")
- `default_font`: Default font for all text
- `default_font_size`: Default font size for all text
- `default_font_color`: Default font color

### Slide Properties

- `layout`: Slide layout name (e.g., "Title Slide", "Title and Content")
- `background`: Background color or image path
- `transition`: Slide transition effect (limited support)

### Element Properties

#### Position and Size
- `x`: Horizontal position
- `y`: Vertical position
- `width`: Element width
- `height`: Element height

#### Text Formatting
- `font`: Font family name
- `font_size`: Font size (in points)
- `font_color`: Text color
- `bold`: "true" or "false"
- `italic`: "true" or "false"
- `underline`: "true" or "false"
- `align`: Text alignment ("left", "center", "right", "justify")
- `vertical_align`: Vertical alignment ("top", "middle", "bottom")
- `margin_left`, `margin_right`, `margin_top`, `margin_bottom`: Text margins

#### Shape Properties
- `shape_type`: Shape type (rectangle, oval, triangle, diamond, etc.)
- `fill`: Fill color
- `border_color`: Border/line color
- `border_width`: Border/line width
- `transparency`: Fill transparency (0.0 to 1.0)
- `rotation`: Rotation angle in degrees

#### Animation Properties (Limited Support)
- `animation`: Animation type
- `animation_delay`: Delay before animation starts
- `animation_duration`: Animation duration

## Examples

### Basic Slide

```markdown
# Simple Slide
{background: "#EFEFEF"}

:::text[x:1in, y:1in, width:8in, height:1in]
{font_size:36, align:center, font_color:"#333333"}
This is a heading
:::

:::text[x:1in, y:3in, width:8in, height:4in]
{font_size:24}
- This is a bullet point
- This is another bullet point
- This is a third bullet point
:::
```

### Multi-Element Slide

```markdown
# Complex Slide

:::shape
{x:1in, y:1in, width:3in, height:3in, shape_type:oval, fill:"#0078D7", transparency:0.2}
:::

:::text
{x:4.5in, y:1in, width:5in, height:2in, font_size:28, font_color:"#333333"}
Key Information
:::

:::table
{x:4.5in, y:3in, width:5in, height:2in}
| Item | Value |
| Product | $1,200 |
| Service | $800 |
| Total | $2,000 |
:::

:::image
{x:1.5in, y:4.5in, width:2in, height:2in}
/path/to/logo.png
:::
```

## Known Limitations

- Chart creation is limited
- Some advanced animations are not supported
- Some advanced formatting options require PowerPoint editing after generation

## Troubleshooting

If you encounter issues:

1. Check your Markdown syntax matches the examples
2. Ensure all file paths are correct
3. Verify that all measurements include units (in, cm, pt)
"""
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("README.md generated with syntax documentation.")


if __name__ == "__main__":
    main()