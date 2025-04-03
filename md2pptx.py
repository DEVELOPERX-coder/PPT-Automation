#!/usr/bin/env python3
"""
MD2PPTX - Markdown to PowerPoint Converter

This script converts a specially formatted Markdown file into a PowerPoint presentation.
It supports advanced PowerPoint features like positioning, formatting, and animations.
"""

import os
import re
import argparse
import yaml
import sys
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt, Cm
from pptx.enum.text import PP_ALIGN, MSO_VERTICAL_ANCHOR, MSO_AUTO_SIZE
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor
from pptx.oxml.xmlchemy import OxmlElement

# Constants for layout types
LAYOUT_TITLE_SLIDE = 0
LAYOUT_TITLE_AND_CONTENT = 1
LAYOUT_SECTION_HEADER = 2
LAYOUT_TWO_CONTENT = 3
LAYOUT_COMPARISON = 4
LAYOUT_TITLE_ONLY = 5
LAYOUT_BLANK = 6
LAYOUT_CONTENT_WITH_CAPTION = 7
LAYOUT_PICTURE_WITH_CAPTION = 8

# Helper functions
def parse_color(color_str):
    """Parse color string to RGB tuple."""
    if not color_str:
        return None
        
    color_str = str(color_str).strip().lower()
    
    # Hex color format
    hex_match = re.match(r'#?([0-9a-f]{6})', color_str)
    if hex_match:
        hex_value = hex_match.group(1)
        r = int(hex_value[0:2], 16)
        g = int(hex_value[2:4], 16)
        b = int(hex_value[4:6], 16)
        return RGBColor(r, g, b)
    
    # RGB format
    rgb_match = re.match(r'rgb\((\d+),\s*(\d+),\s*(\d+)\)', color_str)
    if rgb_match:
        r, g, b = map(int, rgb_match.groups())
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
        'cyan': RGBColor(0, 255, 255),
        'magenta': RGBColor(255, 0, 255),
    }
    
    if color_str in color_map:
        return color_map[color_str]
    
    print(f"Warning: Unknown color '{color_str}', using black")
    return RGBColor(0, 0, 0)

def parse_dimension(value):
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
            # Approximate conversion
            return Pt(num * 0.75)
    
    # Default to inches if no unit is specified
    try:
        return Inches(float(value))
    except:
        print(f"Warning: Cannot parse dimension: {value}, using 1 inch")
        return Inches(1)

def parse_alignment(align_str):
    """Convert alignment string to PowerPoint alignment enum."""
    if not align_str:
        return None
        
    align_str = str(align_str).strip().lower()
    
    align_map = {
        'left': PP_ALIGN.LEFT,
        'center': PP_ALIGN.CENTER,
        'right': PP_ALIGN.RIGHT,
        'justify': PP_ALIGN.JUSTIFY,
        'distributed': PP_ALIGN.DISTRIBUTE,
        'top': MSO_VERTICAL_ANCHOR.TOP,
        'middle': MSO_VERTICAL_ANCHOR.MIDDLE,
        'bottom': MSO_VERTICAL_ANCHOR.BOTTOM
    }
    
    if align_str in align_map:
        return align_map[align_str]
    
    return None

def get_slide_layout(presentation, layout_name):
    """Get slide layout by name or index."""
    # Try to interpret as a number first
    try:
        layout_idx = int(layout_name)
        if 0 <= layout_idx < len(presentation.slide_layouts):
            return presentation.slide_layouts[layout_idx]
    except (ValueError, TypeError):
        pass
    
    # Try to find by name
    layout_name = layout_name.lower()
    layout_map = {
        'title slide': LAYOUT_TITLE_SLIDE,
        'title and content': LAYOUT_TITLE_AND_CONTENT,
        'section header': LAYOUT_SECTION_HEADER,
        'two content': LAYOUT_TWO_CONTENT,
        'comparison': LAYOUT_COMPARISON,
        'title only': LAYOUT_TITLE_ONLY,
        'blank': LAYOUT_BLANK,
        'content with caption': LAYOUT_CONTENT_WITH_CAPTION,
        'picture with caption': LAYOUT_PICTURE_WITH_CAPTION
    }
    
    if layout_name in layout_map:
        idx = layout_map[layout_name]
        if idx < len(presentation.slide_layouts):
            return presentation.slide_layouts[idx]
    
    # Default to title and content
    return presentation.slide_layouts[1]

class MarkdownParser:
    """Parse the markdown file and extract PowerPoint elements."""
    
    def __init__(self, md_file):
        """Initialize the parser with a markdown file."""
        self.md_file = md_file
        with open(md_file, 'r', encoding='utf-8') as f:
            self.content = f.read()
        self.slides = []
        self.global_settings = {}
    
    def parse(self):
        """Parse the markdown content into slide data."""
        # Extract global settings if present
        if self.content.startswith('---'):
            end_index = self.content.find('---', 3)
            if end_index != -1:
                yaml_content = self.content[3:end_index].strip()
                try:
                    self.global_settings = yaml.safe_load(yaml_content)
                except yaml.YAMLError as e:
                    print(f"Warning: Could not parse global settings YAML: {e}")
                self.content = self.content[end_index+3:].strip()
        
        # Split content into slides using markdown headings
        slide_blocks = re.split(r'\n\s*#\s+', self.content)
        
        # If the file doesn't start with a heading, the first block is not a slide
        if not self.content.lstrip().startswith('#'):
            slide_blocks = slide_blocks[1:]  # Skip the initial content
        
        # Process each slide block
        for i, block in enumerate(slide_blocks):
            if block.strip():
                slide_data = self._parse_slide_block(f"# {block}")
                self.slides.append(slide_data)
        
        return self.slides, self.global_settings
    
    def _parse_slide_block(self, block):
        """Parse a single slide block."""
        # Extract slide title (heading)
        title_match = re.match(r'#\s+([^\n]+)', block)
        title = title_match.group(1) if title_match else ""
        
        # Remove title from block
        block = block[title_match.end():].strip() if title_match else block.strip()
        
        # Extract slide settings if present
        settings = {}
        settings_match = re.match(r'\{\s*(.*?)\s*\}', block, re.DOTALL)
        if settings_match:
            settings_str = settings_match.group(1)
            # Parse simple key-value settings
            for setting in re.finditer(r'(\w+)\s*:\s*("[^"]*"|[^,}\s][^,}]*)', settings_str):
                key = setting.group(1).strip()
                value = setting.group(2).strip()
                # Remove quotes if present
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                settings[key] = value
            
            # Remove settings from block
            block = block[settings_match.end():].strip()
        
        # Parse elements
        elements = self._parse_elements(block)
        
        return {
            'title': title,
            'settings': settings,
            'elements': elements
        }
    
    def _parse_elements(self, block):
        """Parse slide elements from markdown block."""
        elements = []
        
        # Find all element blocks using ::: syntax
        element_pattern = r':::(\w+)(?:\[(.*?)\])?\s*\n((?:\{.*?\})?\s*[\s\S]*?)(?=\n:::|$)'
        for match in re.finditer(element_pattern, block):
            element_type = match.group(1)
            inline_props = match.group(2) or ""
            element_content = match.group(3).strip()
            
            # Extract properties from inline style [x:1in, y:2in, etc]
            properties = {}
            if inline_props:
                for prop in re.finditer(r'(\w+)\s*:\s*("[^"]*"|[^,\s][^,]*)', inline_props):
                    key = prop.group(1).strip()
                    value = prop.group(2).strip()
                    # Remove quotes if present
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]
                    properties[key] = value
            
            # Check for separate property block
            prop_block_match = re.match(r'\{\s*(.*?)\s*\}([\s\S]*)', element_content, re.DOTALL)
            if prop_block_match:
                prop_str = prop_block_match.group(1)
                # Extract properties from block
                for prop in re.finditer(r'(\w+)\s*:\s*("[^"]*"|[^,}\s][^,}]*)', prop_str):
                    key = prop.group(1).strip()
                    value = prop.group(2).strip()
                    # Remove quotes if present
                    if value.startswith('"') and value.endswith('"'):
                        value = value[1:-1]
                    properties[key] = value
                
                # Get content after property block
                element_content = prop_block_match.group(2).strip()
            
            elements.append({
                'type': element_type,
                'properties': properties,
                'content': element_content
            })
        
        return elements

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
        # Set slide dimensions
        if 'slide_width' in self.global_settings and 'slide_height' in self.global_settings:
            try:
                width = parse_dimension(self.global_settings['slide_width'])
                height = parse_dimension(self.global_settings['slide_height'])
                self.prs.slide_width = width
                self.prs.slide_height = height
            except Exception as e:
                print(f"Warning: Could not set slide dimensions: {e}")
    
    def generate(self):
        """Generate the PowerPoint presentation from the parsed data."""
        for slide_data in self.slides_data:
            self._add_slide(slide_data)
        
        return self.prs
    
    def _add_slide(self, slide_data):
        """Add a slide to the presentation."""
        # Get slide layout
        layout_name = slide_data['settings'].get('layout', 'Title and Content')
        layout = get_slide_layout(self.prs, layout_name)
        
        # Create the slide
        slide = self.prs.slides.add_slide(layout)
        
        # Set slide title if the layout has a title placeholder
        if hasattr(slide, 'shapes') and hasattr(slide.shapes, 'title') and slide.shapes.title:
            slide.shapes.title.text = slide_data['title']
        
        # Apply slide background if specified
        if 'background' in slide_data['settings']:
            bg_color = parse_color(slide_data['settings']['background'])
            if bg_color:
                slide.background.fill.solid()
                slide.background.fill.fore_color.rgb = bg_color
        
        # Add elements to the slide
        for element in slide_data['elements']:
            self._add_element(slide, element)
    
    def _add_element(self, slide, element):
        """Add an element to the slide."""
        element_type = element['type'].lower()
        properties = element['properties']
        content = element['content']
        
        try:
            if element_type == 'text':
                self._add_text_element(slide, content, properties)
            elif element_type == 'image':
                self._add_image_element(slide, content, properties)
            elif element_type == 'shape':
                self._add_shape_element(slide, content, properties)
            elif element_type == 'table':
                self._add_table_element(slide, content, properties)
            elif element_type == 'chart':
                self._add_chart_element(slide, content, properties)
            else:
                print(f"Warning: Unknown element type '{element_type}'")
        except Exception as e:
            print(f"Error adding {element_type} element: {e}")
    
    def _add_text_element(self, slide, content, properties):
        """Add a text element to the slide."""
        # Get position and size
        left = parse_dimension(properties.get('x', '1in'))
        top = parse_dimension(properties.get('y', '1in'))
        width = parse_dimension(properties.get('width', '4in'))
        height = parse_dimension(properties.get('height', '1in'))
        
        # Create textbox
        textbox = slide.shapes.add_textbox(left, top, width, height)
        text_frame = textbox.text_frame
        
        # Set auto-size properties
        if 'auto_size' in properties:
            auto_size = properties['auto_size'].lower()
            if auto_size == 'none':
                text_frame.auto_size = MSO_AUTO_SIZE.NONE
            elif auto_size == 'text':
                text_frame.auto_size = MSO_AUTO_SIZE.TEXT_TO_FIT_SHAPE
            elif auto_size == 'shape':
                text_frame.auto_size = MSO_AUTO_SIZE.SHAPE_TO_FIT_TEXT
        
        # Add text content
        text_frame.text = content
        
        # Set text alignment
        if 'align' in properties:
            alignment = parse_alignment(properties['align'])
            if alignment in [PP_ALIGN.LEFT, PP_ALIGN.CENTER, PP_ALIGN.RIGHT, PP_ALIGN.JUSTIFY]:
                for paragraph in text_frame.paragraphs:
                    paragraph.alignment = alignment
        
        # Set vertical alignment
        if 'vertical_align' in properties:
            v_alignment = parse_alignment(properties['vertical_align'])
            if v_alignment in [MSO_VERTICAL_ANCHOR.TOP, MSO_VERTICAL_ANCHOR.MIDDLE, MSO_VERTICAL_ANCHOR.BOTTOM]:
                text_frame.vertical_anchor = v_alignment
        
        # Set text margins
        for margin in ['margin_left', 'margin_right', 'margin_top', 'margin_bottom']:
            if margin in properties:
                setattr(text_frame, margin, parse_dimension(properties[margin]))
        
        # Apply text formatting
        for paragraph in text_frame.paragraphs:
            # Create bullet points
            if 'bullet' in properties and properties['bullet'].lower() in ['true', '1', 'yes']:
                paragraph.level = int(properties.get('bullet_level', 0))
                paragraph._pPr.get_or_add_pPr().set('bullet', True)
            
            # Apply font formatting to all runs
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
                    except Exception as e:
                        print(f"Warning: Invalid font size: {e}")
                
                # Font color
                if 'font_color' in properties:
                    color = parse_color(properties['font_color'])
                    if color:
                        run.font.color.rgb = color
                
                # Font style
                if 'bold' in properties and properties['bold'].lower() in ['true', '1', 'yes']:
                    run.font.bold = True
                if 'italic' in properties and properties['italic'].lower() in ['true', '1', 'yes']:
                    run.font.italic = True
                if 'underline' in properties and properties['underline'].lower() in ['true', '1', 'yes']:
                    run.font.underline = True
    
    def _add_image_element(self, slide, content, properties):
        """Add an image element to the slide."""
        # Get position and size
        left = parse_dimension(properties.get('x', '1in'))
        top = parse_dimension(properties.get('y', '1in'))
        
        # Trim any whitespace from the image path
        image_path = content.strip()
        
        # Check if the image file exists
        if not os.path.exists(image_path):
            print(f"Warning: Image file not found: {image_path}")
            return
        
        # Add the image
        if 'width' in properties and 'height' in properties:
            width = parse_dimension(properties['width'])
            height = parse_dimension(properties['height'])
            picture = slide.shapes.add_picture(image_path, left, top, width, height)
        elif 'width' in properties:
            width = parse_dimension(properties['width'])
            picture = slide.shapes.add_picture(image_path, left, top, width=width)
        elif 'height' in properties:
            height = parse_dimension(properties['height'])
            picture = slide.shapes.add_picture(image_path, left, top, height=height)
        else:
            picture = slide.shapes.add_picture(image_path, left, top)
        
        # Set image rotation if specified
        if 'rotation' in properties:
            try:
                rotation = float(properties['rotation'])
                picture.rotation = rotation
            except:
                print(f"Warning: Invalid rotation value: {properties['rotation']}")
    
    def _add_shape_element(self, slide, content, properties):
        """Add a shape element to the slide."""
        # Get position and size
        left = parse_dimension(properties.get('x', '1in'))
        top = parse_dimension(properties.get('y', '1in'))
        width = parse_dimension(properties.get('width', '2in'))
        height = parse_dimension(properties.get('height', '2in'))
        
        # Determine shape type
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
            'arrow': MSO_SHAPE.ARROW
        }
        
        shape_enum = shape_map.get(shape_type, MSO_SHAPE.RECTANGLE)
        
        # Create the shape
        shape = slide.shapes.add_shape(shape_enum, left, top, width, height)
        
        # Set fill color
        if 'fill' in properties:
            fill_color = parse_color(properties['fill'])
            if fill_color:
                shape.fill.solid()
                shape.fill.fore_color.rgb = fill_color
        
        # Set border/line properties
        if 'border_color' in properties:
            border_color = parse_color(properties['border_color'])
            if border_color:
                shape.line.color.rgb = border_color
        
        if 'border_width' in properties:
            shape.line.width = parse_dimension(properties['border_width'])
        
        # Set transparency
        if 'transparency' in properties:
            try:
                trans_value = float(properties['transparency'])
                if 0 <= trans_value <= 1:
                    shape.fill.transparency = trans_value
            except:
                print(f"Warning: Invalid transparency value: {properties['transparency']}")
        
        # Set rotation
        if 'rotation' in properties:
            try:
                rotation = float(properties['rotation'])
                shape.rotation = rotation
            except:
                print(f"Warning: Invalid rotation value: {properties['rotation']}")
        
        # Add text content if provided
        if content:
            shape.text_frame.text = content
            
            # Apply text formatting
            text_frame = shape.text_frame
            
            # Set text alignment
            if 'align' in properties:
                alignment = parse_alignment(properties['align'])
                if alignment in [PP_ALIGN.LEFT, PP_ALIGN.CENTER, PP_ALIGN.RIGHT, PP_ALIGN.JUSTIFY]:
                    for paragraph in text_frame.paragraphs:
                        paragraph.alignment = alignment
            
            # Set vertical alignment
            if 'vertical_align' in properties:
                v_alignment = parse_alignment(properties['vertical_align'])
                if v_alignment in [MSO_VERTICAL_ANCHOR.TOP, MSO_VERTICAL_ANCHOR.MIDDLE, MSO_VERTICAL_ANCHOR.BOTTOM]:
                    text_frame.vertical_anchor = v_alignment
            
            # Apply font formatting to all runs in all paragraphs
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
                        except:
                            print(f"Warning: Invalid font size: {properties['font_size']}")
                    
                    # Font color
                    if 'font_color' in properties:
                        color = parse_color(properties['font_color'])
                        if color:
                            run.font.color.rgb = color
                    
                    # Font style
                    if 'bold' in properties and properties['bold'].lower() in ['true', '1', 'yes']:
                        run.font.bold = True
                    if 'italic' in properties and properties['italic'].lower() in ['true', '1', 'yes']:
                        run.font.italic = True
                    if 'underline' in properties and properties['underline'].lower() in ['true', '1', 'yes']:
                        run.font.underline = True
    
    def _add_table_element(self, slide, content, properties):
        """Add a table element to the slide."""
        # Get position and size
        left = parse_dimension(properties.get('x', '1in'))
        top = parse_dimension(properties.get('y', '1in'))
        width = parse_dimension(properties.get('width', '6in'))
        
        # Parse table content
        lines = [line.strip() for line in content.strip().split('\n')]
        if not lines:
            print("Warning: Empty table content")
            return
        
        # Process table rows
        rows = []
        for line in lines:
            # Check for pipe-separated format
            if '|' in line:
                # Skip separator lines (like |---|---|)
                if re.match(r'\s*\|[-:\s]+\|', line):
                    continue
                # Remove leading/trailing pipes and split
                cells = [cell.strip() for cell in line.strip('|').split('|')]
            else:
                # Assume comma-separated
                cells = [cell.strip() for cell in line.split(',')]
            rows.append(cells)
        
        if not rows:
            print("Warning: No table data found")
            return
        
        # Determine rows and columns
        num_rows = len(rows)
        num_cols = max(len(row) for row in rows)
        
        # Create table
        table = slide.shapes.add_table(num_rows, num_cols, left, top, width)
        
        # Fill table with data
        for i, row in enumerate(rows):
            for j, cell_text in enumerate(row):
                cell = table.table.cell(i, j)
                cell.text = cell_text
                
                # Apply text properties
                if 'font' in properties:
                    for paragraph in cell.text_frame.paragraphs:
                        for run in paragraph.runs:
                            run.font.name = properties['font']
                
                if 'font_size' in properties:
                    try:
                        size_value = properties['font_size']
                        if isinstance(size_value, (int, float)):
                            size_pt = Pt(size_value)
                        else:
                            # Strip 'pt' suffix if present
                            size_str = str(size_value).lower()
                            if size_str.endswith('pt'):
                                size_str = size_str[:-2]
                            size_pt = Pt(float(size_str))
                        
                        for paragraph in cell.text_frame.paragraphs:
                            for run in paragraph.runs:
                                run.font.size = size_pt
                    except:
                        print(f"Warning: Invalid font size: {properties['font_size']}")
        
        # Style the table
        if 'header_row' in properties and properties['header_row'].lower() in ['true', '1', 'yes']:
            # Apply header row formatting
            for j in range(num_cols):
                cell = table.table.cell(0, j)
                for paragraph in cell.text_frame.paragraphs:
                    for run in paragraph.runs:
                        run.font.bold = True
    
    def _add_chart_element(self, slide, content, properties):
        """Add a chart element to the slide."""
        # Note: python-pptx has limited chart support
        # This implementation provides basic chart functionality
        print("Warning: Chart elements have limited functionality in this version")
        
        # Get position
        left = parse_dimension(properties.get('x', '1in'))
        top = parse_dimension(properties.get('y', '1in'))
        width = parse_dimension(properties.get('width', '6in'))
        height = parse_dimension(properties.get('height', '4in'))
        
        # Create a textbox placeholder for the chart
        textbox = slide.shapes.add_textbox(left, top, width, height)
        textbox.text_frame.text = f"Chart: {properties.get('title', '')}\n\n{content}"
        
        # Add note about chart limitations
        textbox.text_frame.add_paragraph().text = "\n(Chart visualization requires manual editing in PowerPoint)"
    
    def save(self, output_file):
        """Save the generated presentation to a file."""
        self.prs.save(output_file)
        print(f"Presentation saved to: {output_file}")

def create_readme():
    """Generate README.md file with syntax documentation."""
    readme_content = """# Markdown to PowerPoint Converter

This tool converts specially formatted Markdown files into PowerPoint presentations.

## Installation

```bash
pip install python-pptx pyyaml
```

## Usage

```bash
python md2pptx.py input.md -o output.pptx
```

## Markdown Format

### Global Settings

At the beginning of your Markdown file, you can define global presentation settings:

```markdown
---
slide_width: 10in
slide_height: 7.5in
default_font: Arial
default_font_size: 18
---
```

### Slides

Each slide begins with a level-1 Markdown heading:

```markdown
# Slide Title
```

### Slide Settings

You can specify slide-specific settings in curly braces after the title:

```markdown
# Slide Title
{
    layout: "Title and Content",
    background: "#FFFFFF"
}
```

### Elements

Elements are defined using the triple-colon syntax:

```markdown
:::text
This is a text box
:::
```

You can specify positioning and formatting with brackets or a properties block:

```markdown
:::text[x:1in, y:2in, width:4in]
This is a positioned text box
:::

# OR

:::text
{x:1in, y:2in, width:4in, font_size:24, font_color:blue}
This is a styled text box
:::
```

## Element Types

### Text

```markdown
:::text
{x:1in, y:1in, width:8in, height:2in, font:"Arial", font_size:24, font_color:"#FF0000", align:center}
This is a styled text box
:::
```

### Images

```markdown
:::image
{x:2in, y:3in, width:4in, height:3in}
/path/to/image.jpg
:::
```

### Shapes

```markdown
:::shape
{x:1in, y:1in, width:2in, height:2in, shape_type:oval, fill:"#0000FF", border_color:"#000000"}
Text inside shape
:::
```

Available shape types: rectangle, oval, rounded_rectangle, triangle, diamond, pentagon, hexagon, star, arrow

### Tables

```markdown
:::table
{x:1in, y:1in, width:8in, font_size:14, header_row:true}
Header 1, Header 2, Header 3
Cell 1, Cell 2, Cell 3
Cell 4, Cell 5, Cell 6
:::
```

Or using Markdown table syntax:

```markdown
:::table
{x:1in, y:1in, width:8in}
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |
:::
```

## Common Properties

### Position and Size
- `x`, `y`: Position (e.g., "1in", "2.54cm")
- `width`, `height`: Size (e.g., "4in", "10cm")

### Text Formatting
- `font`: Font family (e.g., "Arial", "Calibri")
- `font_size`: Font size in points (e.g., 24)
- `font_color`: Text color (e.g., "#FF0000", "red")
- `bold`, `italic`, `underline`: Text style (e.g., true, false)
- `align`: Text alignment (e.g., "left", "center", "right")
- `vertical_align`: Vertical alignment (e.g., "top", "middle", "bottom")
- `bullet`: Enable bullet points (e.g., true, false)

### Shape Properties
- `shape_type`: Shape type (e.g., "rectangle", "oval", "triangle")
- `fill`: Fill color (e.g., "#0000FF", "blue")
- `border_color`: Border color (e.g., "#000000", "black")
- `border_width`: Border width (e.g., "2pt", "0.03in")
- `transparency`: Fill transparency (e.g., 0.5)
- `rotation`: Rotation angle in degrees (e.g., 45)

## Example

```markdown
---
slide_width: 10in
slide_height: 7.5in
default_font: "Calibri"
default_font_size: 18
---

# Welcome to My Presentation
{
    layout: "Title Slide",
    background: "#0078D7"
}

:::text[x:1in, y:2.5in, width:8in, height:1.5in]
{font_size:44, font_color:"#FFFFFF", align:center, bold:true}
Welcome to My Presentation
:::

:::text[x:1in, y:4.5in, width:8in, height:0.5in]
{font_size:24, font_color:"#FFFFFF", align:center}
John Smith, CEO
:::

# Agenda
{
    layout: "Title and Content",
    background: "#FFFFFF"
}

:::text[x:1in, y:1.5in, width:8in, height:4in]
{font_size:24, bullet:true}
- Introduction
- Key Points
- Data Analysis
- Conclusion
- Q&A
:::

# Thank You
{
    layout: "Title Slide",
    background: "#0078D7"
}

:::text[x:1in, y:3in, width:8in, height:1.5in]
{font_size:44, font_color:"#FFFFFF", align:center, bold:true}
Thank You!
:::

:::text[x:1in, y:4.5in, width:8in, height:0.5in]
{font_size:24, font_color:"#FFFFFF", align:center}
Questions?
:::
```
"""
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("README.md generated with syntax documentation.")

def main():
    """Main function to process command line arguments and execute the conversion."""
    parser = argparse.ArgumentParser(description='Convert Markdown to PowerPoint')
    parser.add_argument('input_file', help='Input Markdown file')
    parser.add_argument('-o', '--output', help='Output PowerPoint file')
    parser.add_argument('-r', '--readme', action='store_true', 
                        help='Generate README.md with syntax documentation')
    
    args = parser.parse_args()
    
    # Generate README if requested
    if args.readme:
        create_readme()
        if not args.input_file:
            return 0
    
    # Validate input file
    if not os.path.exists(args.input_file):
        print(f"Error: Input file '{args.input_file}' not found.")
        return 1
    
    # Determine output file
    output_file = args.output
    if not output_file:
        input_path = Path(args.input_file)
        output_file = str(input_path.with_suffix('.pptx'))
    
    try:
        # Parse markdown
        parser = MarkdownParser(args.input_file)
        slides_data, global_settings = parser.parse()
        
        # Generate PowerPoint
        generator = PowerPointGenerator(slides_data, global_settings)
        generator.generate()
        generator.save(output_file)
        
        print(f"Successfully converted {args.input_file} to {output_file}")
        return 0
    except Exception as e:
        print(f"Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())