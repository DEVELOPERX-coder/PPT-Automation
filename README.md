# Markdown to PowerPoint Converter

This tool converts specially formatted Markdown files into feature-rich PowerPoint presentations. It supports a wide range of PowerPoint features including precise element positioning, formatting, animations, and more.

## Installation

### Requirements

- Python 3.6 or higher
- Required Python packages:
  - python-pptx
  - pyyaml

Install the dependencies with:

```bash
pip install python-pptx pyyaml
```

For advanced features (animations, transitions, etc.):

```bash
pip install pywin32
```

## Basic Usage

```bash
python md2pptx.py input.md -o output.pptx
```

Options:

- `-o, --output`: Specify the output PowerPoint file name
- `-b, --backend`: Choose backend (`win32com` or `python-pptx`, default: `win32com`)
- `-g, --generate-readme`: Generate a README file with syntax documentation

## Markdown Syntax Reference

The system uses a specialized Markdown format with YAML-style properties and custom element tags to describe PowerPoint features.

### Global Settings

At the top of your Markdown file, you can specify global presentation settings using YAML frontmatter:

```markdown
---
slide_width: 10in
slide_height: 7.5in
default_font: Arial
default_font_size: 18
default_font_color: "#333333"
company_logo: "path/to/logo.png"
footer_text: "Confidential"
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
transition: "fade",
footer: true,
slide_number: true
}
```

### Elements

Elements are defined using triple colon syntax followed by the element type:

```markdown
:::text
This is a text box
:::
```

Elements can have properties specified in brackets or in a separate property block:

```markdown
:::text[x:1in, y:2in, width:4in, height:2in]
This is a positioned text box
:::

# OR

:::text
{x:1in, y:2in, width:4in, height:2in, font_size:24, font_color:blue}
This is a styled text box
:::
```

## Element Types

### Text

Text elements create text boxes that can be precisely positioned and formatted.

```markdown
:::text
{
x: 1in,
y: 1in,
width: 8in,
height: 2in,
font: "Arial",
font_size: 24,
font_color: "#FF0000",
align: center,
bold: true,
italic: false,
underline: false
}
This is a styled text box with formatting applied.
Multiple paragraphs are supported.
:::
```

### Images

Image elements insert pictures from local or network files.

```markdown
:::image
{
x: 2in,
y: 3in,
width: 4in,
height: 3in,
rotation: 15,
transparency: 0.2,
border_color: "#000000",
border_width: 2pt
}
/path/to/image.jpg
:::
```

### Shapes

Shape elements create geometric shapes that can contain text.

```markdown
:::shape
{
x: 1in,
y: 1in,
width: 2in,
height: 2in,
shape_type: oval,
fill: "#0000FF",
border_color: "#000000",
border_width: 2pt,
transparency: 0.3,
rotation: 45,
shadow: true
}
Text inside shape
:::
```

Available shape types:

- rectangle
- oval
- rounded_rectangle
- triangle
- right_triangle
- diamond
- pentagon
- hexagon
- star
- arrow

### Tables

Table elements create data tables with rows and columns.

```markdown
:::table
{
x: 1in,
y: 1in,
width: 8in,
height: 3in,
header_row: true,
first_column: true,
banded_rows: true,
border_color: "#333333"
}
Header 1, Header 2, Header 3
Cell 1, Cell 2, Cell 3
Cell 4, Cell 5, Cell 6
:::
```

Or using Markdown table syntax:

```markdown
:::table
{
x: 1in,
y: 1in,
width: 8in,
height: 3in
}
| Header 1 | Header 2 | Header 3 |
| Cell 1 | Cell 2 | Cell 3 |
| Cell 4 | Cell 5 | Cell 6 |
:::
```

### Charts

Chart elements create data visualizations.

```markdown
:::chart
{
x: 1in,
y: 1in,
width: 6in,
height: 4in,
chart_type: bar,
title: "Sales Data",
has_legend: true,
legend_position: "bottom",
x_axis_title: "Categories",
y_axis_title: "Values"
}
Category 1, 10
Category 2, 15
Category 3, 7
Category 4, 12
:::
```

Available chart types:

- bar
- column
- line
- pie
- area
- scatter
- doughnut
- radar

### SmartArt

SmartArt elements create diagrams from lists of text items.

```markdown
:::smartart
{
x: 1in,
y: 1in,
width: 8in,
height: 3in,
type: "process"
}
Step 1, Step 2, Step 3, Step 4
:::
```

Available SmartArt types:

- process
- cycle
- hierarchy
- pyramid
- radial
- venn
- matrix
- relationship
- list

## Animation & Transition Effects

You can add animations to any element by adding animation properties:

```markdown
:::text
{
x: 1in,
y: 1in,
width: 4in,
animation: "fade",
animation_trigger: "on_click",
animation_delay: 0.5,
animation_duration: 1.0
}
This text will fade in when clicked.
:::
```

Slide transitions are specified in the slide settings:

```markdown
# Example Slide

{
transition: "fade",
transition_speed: "medium"
}
```

## Property Reference

### Global Settings Properties

| Property             | Description                        | Example Values                      |
| -------------------- | ---------------------------------- | ----------------------------------- |
| `slide_width`        | Width of all slides                | "10in", "25.4cm"                    |
| `slide_height`       | Height of all slides               | "7.5in", "19.05cm"                  |
| `default_font`       | Default font for all text          | "Arial", "Calibri"                  |
| `default_font_size`  | Default font size for all text     | 18, "18pt"                          |
| `default_font_color` | Default font color                 | "#333333", "rgb(51,51,51)", "black" |
| `company_logo`       | Path to company logo for templates | "/path/to/logo.png"                 |
| `footer_text`        | Default footer text for all slides | "Confidential"                      |
| `header_text`        | Default header text for all slides | "Company Name"                      |
| `template`           | PowerPoint template to use         | "template.potx"                     |

### Slide Properties

| Property           | Description                    | Example Values                              |
| ------------------ | ------------------------------ | ------------------------------------------- |
| `layout`           | Slide layout name              | "Title Slide", "Title and Content", "Blank" |
| `background`       | Background color or image path | "#FFFFFF", "/path/to/background.jpg"        |
| `background_style` | Style for background           | "solid", "gradient", "pattern"              |
| `transition`       | Slide transition effect        | "fade", "push", "wipe", "split"             |
| `transition_speed` | Speed of transition            | "slow", "medium", "fast"                    |
| `footer`           | Show/hide footer               | true, false                                 |
| `header`           | Show/hide header               | true, false                                 |
| `slide_number`     | Show/hide slide number         | true, false                                 |
| `notes`            | Speaker notes for the slide    | "Remember to mention key points"            |

### Animation Properties

| Property              | Description                      | Example Values                                     |
| --------------------- | -------------------------------- | -------------------------------------------------- |
| `animation`           | Animation type                   | "fade", "wipe", "fly_in", "float", "split", "zoom" |
| `animation_trigger`   | When animation starts            | "on_click", "with_previous", "after_previous"      |
| `animation_direction` | Direction of animation           | "in", "out", "up", "down", "left", "right"         |
| `animation_delay`     | Delay before animation (seconds) | 0, 0.5, 1                                          |
| `animation_duration`  | Animation duration (seconds)     | 0.5, 1, 2                                          |

## Element Properties

### Position and Size Properties

| Property   | Description         | Example Values            |
| ---------- | ------------------- | ------------------------- |
| `x`        | Horizontal position | "1in", "2.54cm", "72pt"   |
| `y`        | Vertical position   | "1in", "2.54cm", "72pt"   |
| `width`    | Element width       | "4in", "10.16cm", "288pt" |
| `height`   | Element height      | "3in", "7.62cm", "216pt"  |
| `rotation` | Rotation angle      | 45, 90, -30               |

### Working with Units

The system supports various units for position and size specifications:

- `in`: Inches (default if no unit specified)
- `cm`: Centimeters
- `pt`: Points (1/72 of an inch)
- `px`: Pixels (approximate conversion)

### Working with Colors

Colors can be specified in multiple formats:

- Hex: `#FF0000`, `#F00`
- Named colors: `red`, `blue`, `green`, etc.

## Tips and Best Practices

1. **Organizing Content**:

   - Use global settings for consistent presentation styles
   - Group related slides with meaningful titles
   - Use bullet points for lists and organized content

2. **Layout and Positioning**:

   - Use precise coordinates for complex layouts
   - Test your presentation with different screen resolutions
   - Consider using relative positioning for better adaptability

3. **Styling**:

   - Maintain consistent fonts and colors throughout
   - Use company style guides for visual elements
   - Limit animations to avoid distractions

4. **Performance**:
   - Optimize image sizes before embedding
   - Be mindful of the number of elements per slide
   - Split complex presentations into multiple files

## Troubleshooting

### Common Issues

1. **Element not appearing at expected position**:

   - Check units (in, cm, pt) on coordinates
   - Verify slide dimensions match expected size
   - Ensure element is not positioned outside slide boundaries

2. **Formatting not applied**:

   - Check syntax of property specifications
   - Verify property names are spelled correctly
   - Ensure values are in expected formats

3. **Images not displaying**:
   - Verify file paths are correct
   - Check that image files exist and are readable
   - Try using absolute paths if relative paths fail

## Advanced Features

These features are available when using the win32com backend:

- **Animation effects** for element entrance, emphasis, and exit
- **Slide transitions** like fade, push, wipe, etc.
- **SmartArt** diagrams for visual representation of relationships
- **Custom templates** for consistent branding
- **Speaker notes** for presentation guidance

## Contributing

Contributions to improve the conversion tool are welcome. Please submit issues and pull requests to the project repository.

## License

This tool is licensed under the MIT License.

## License

This tool is licensed under the MIT License.

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Complete Example

Here's a complete example markdown file for a simple presentation:

```markdown
---
slide_width: 10in
slide_height: 7.5in
default_font: "Calibri"
default_font_size: 18
company_logo: "logo.png"
footer_text: "Confidential - 2025"
---

# Project Overview

{
layout: "Title Slide",
background: "#003366",
transition: "fade"
}

:::text[x:1in, y:2.5in, width:8in, height:1.5in]
{font: "Calibri", font_size: 44, font_color: "#FFFFFF", align: center, bold: true, animation: "fade", animation_duration: 1.0}
New Product Launch
:::

:::text[x:1in, y:4in, width:8in, height:1in]
{font: "Calibri", font_size: 28, font_color: "#FFFFFF", align: center, animation: "fade", animation_delay: 0.5}
Q2 2025 Roadmap
:::

# Key Objectives

{
layout: "Title and Content",
background: "#FFFFFF",
transition: "push"
}

:::text[x:0.5in, y:0.8in, width:9in, height:0.75in]
{font: "Calibri", font_size: 36, font_color: "#003366", bold: true}
Quarterly Goals
:::

:::text[x:0.5in, y:1.75in, width:9in, height:4in]
{font: "Calibri", font_size: 24, bullet: true, animation: "fly_in", animation_direction: "left", animation_trigger: "on_click"}

- Increase market share by 15%
- Launch mobile platform in 3 new regions
- Improve customer satisfaction scores to 90%+
- Reduce operational costs by 8%
- Complete Phase 1 of digital transformation
  :::

# Financial Projections

{
layout: "Title and Content",
background: "#FFFFFF",
transition: "fade"
}

:::text[x:0.5in, y:0.8in, width:9in, height:0.75in]
{font: "Calibri", font_size: 36, font_color: "#003366", bold: true}
Q2 Forecast
:::

:::chart[x:0.5in, y:1.75in, width:9in, height:4.5in]
{
chart_type: "column",
title: "Revenue by Product Line ($M)",
has_legend: true,
legend_position: "bottom",
x_axis_title: "Product",
y_axis_title: "Revenue",
animation: "fade"
}
Product, Q1 Actual, Q2 Forecast
Product A, 12.4, 14.8
Product B, 8.7, 10.5
Product C, 15.2, 18.6
Product D, 6.9, 11.2
:::

# Implementation Timeline

{
layout: "Title and Content",
background: "#FFFFFF",
transition: "wipe"
}

:::text[x:0.5in, y:0.8in, width:9in, height:0.75in]
{font: "Calibri", font_size: 36, font_color: "#003366", bold: true}
Project Roadmap
:::

:::smartart[x:0.5in, y:1.75in, width:9in, height:4in]
{
type: "process",
animation: "wipe"
}
Planning, Development, Testing, Deployment, Maintenance
:::

# Thank You

{
layout: "Title Slide",
background: "#003366",
transition: "fade"
}

:::text[x:1in, y:2.5in, width:8in, height:1.5in]
{font: "Calibri", font_size: 48, font_color: "#FFFFFF", align: center, bold: true, animation: "zoom"}
Questions?
:::

:::shape[x:3.5in, y:5.5in, width:3in, height:0.75in]
{
shape_type: "rounded_rectangle",
fill: "#4472C4",
border_color: "#2F528F",
border_width: 2pt,
font_color: "#FFFFFF",
align: "center",
vertical_align: "middle",
font_size: 20,
bold: true,
hyperlink: "mailto:contact@example.com",
tooltip: "Send us an email"
}
contact@example.com
:::
```

## Workflow

A typical workflow for using this tool looks like this:

1. **Create a markdown file** using the syntax described in this README
2. **Run the converter**:
   ```bash
   python md2pptx.py presentation.md -o presentation.pptx
   ```
3. **Review and fine-tune** the generated PowerPoint presentation
4. For advanced features (animations, transitions), make sure to use the win32com backend:
   ```bash
   python md2pptx.py presentation.md -o presentation.pptx -b win32com
   ```

## Known Limitations

1. **Python-pptx backend limitations**:

   - Animations and transitions are not supported
   - Some advanced formatting options may be unavailable
   - SmartArt is not fully supported

2. **Win32com backend requirements**:
   - Requires Windows operating system
   - Microsoft PowerPoint must be installed
   - Some features may depend on the PowerPoint version

## Version History

- **1.0.0** (April 2025)
  - Initial release with support for text, shapes, images, tables, and charts
  - Animation and transition support
  - Two backend options: win32com and python-pptx

## Acknowledgments

- [python-pptx](https://python-pptx.readthedocs.io/) for the Python library for creating PowerPoint files
- [PyWin32](https://github.com/mhammond/pywin32) for Windows COM integration
- [PyYAML](https://pyyaml.org/) for YAML parsing

## Contact

For questions, issues, or contributions, please create an issue in the project repository or contact the project maintainer.
