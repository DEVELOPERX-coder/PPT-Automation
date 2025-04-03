# PPT-Automation

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

## Basic Usage

```bash
python md2pptx.py input.md -o output.pptx
```

Options:

- `-o, --output`: Specify the output PowerPoint file name
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

### Element Properties

#### Position and Size

| Property   | Description         | Example Values            |
| ---------- | ------------------- | ------------------------- |
| `x`        | Horizontal position | "1in", "2.54cm", "72pt"   |
| `y`        | Vertical position   | "1in", "2.54cm", "72pt"   |
| `width`    | Element width       | "4in", "10.16cm", "288pt" |
| `height`   | Element height      | "3in", "7.62cm", "216pt"  |
| `rotation` | Rotation angle      | 45, 90, -30               |

#### Text Formatting

| Property         | Description        | Example Values                        |
| ---------------- | ------------------ | ------------------------------------- |
| `font`           | Font family name   | "Arial", "Calibri", "Times New Roman" |
| `font_size`      | Font size          | 24, "24pt"                            |
| `font_color`     | Text color         | "#FF0000", "rgb(255,0,0)", "red"      |
| `bold`           | Bold text          | true, false                           |
| `italic`         | Italic text        | true, false                           |
| `underline`      | Underlined text    | true, false                           |
| `strikethrough`  | Strikethrough text | true, false                           |
| `align`          | Text alignment     | "left", "center", "right", "justify"  |
| `vertical_align` | Vertical alignment | "top", "middle", "bottom"             |
| `line_spacing`   | Line spacing       | 1, 1.5, 2                             |
| `margin_left`    | Left text margin   | "0.1in", "0.25cm"                     |
| `margin_right`   | Right text margin  | "0.1in", "0.25cm"                     |
| `margin_top`     | Top text margin    | "0.1in", "0.25cm"                     |
| `margin_bottom`  | Bottom text margin | "0.1in", "0.25cm"                     |
| `bullet`         | Enable bullets     | true, false                           |
| `bullet_style`   | Bullet style       | "circle", "square", "number", "arrow" |
| `bullet_size`    | Bullet size        | 80, 100, 120                          |
| `bullet_color`   | Bullet color       | "#FF0000", "rgb(255,0,0)", "red"      |

#### Shape Properties

| Property           | Description        | Example Values                                   |
| ------------------ | ------------------ | ------------------------------------------------ |
| `shape_type`       | Shape type         | "rectangle", "oval", "triangle", "diamond", etc. |
| `fill`             | Fill color         | "#0000FF", "rgb(0,0,255)", "blue"                |
| `fill_style`       | Fill style         | "solid", "gradient", "pattern"                   |
| `border_color`     | Border/line color  | "#000000", "rgb(0,0,0)", "black"                 |
| `border_width`     | Border/line width  | "2pt", "1px", "0.03in"                           |
| `border_style`     | Border/line style  | "solid", "dashed", "dotted"                      |
| `transparency`     | Fill transparency  | 0.0, 0.5, 1.0                                    |
| `shadow`           | Enable shadow      | true, false                                      |
| `shadow_color`     | Shadow color       | "#888888", "rgb(136,136,136)", "gray"            |
| `shadow_blur`      | Shadow blur radius | 5, 10, 15                                        |
| `shadow_direction` | Shadow direction   | 0, 45, 90, 135, 180, 225, 270, 315               |
| `shadow_distance`  | Shadow distance    | 3, 5, 10                                         |
| `glow`             | Enable glow effect | true, false                                      |
| `glow_color`       | Glow color         | "#FF00FF", "rgb(255,0,255)", "magenta"           |
| `glow_size`        | Glow size          | 5, 10, 15                                        |

#### Image Properties

| Property       | Description        | Example Values    |
| -------------- | ------------------ | ----------------- |
| `brightness`   | Image brightness   | -0.5, 0, 0.5      |
| `contrast`     | Image contrast     | -0.5, 0, 0.5      |
| `crop_left`    | Left crop          | "0.5in", "1.27cm" |
| `crop_right`   | Right crop         | "0.5in", "1.27cm" |
| `crop_top`     | Top crop           | "0.5in", "1.27cm" |
| `crop_bottom`  | Bottom crop        | "0.5in", "1.27cm" |
| `transparency` | Image transparency | 0.0, 0.5, 1.0     |

#### Table Properties

| Property         | Description                    | Example Values                       |
| ---------------- | ------------------------------ | ------------------------------------ |
| `header_row`     | Style first row as header      | true, false                          |
| `first_column`   | Style first column differently | true, false                          |
| `banded_rows`    | Alternate row styling          | true, false                          |
| `banded_columns` | Alternate column styling       | true, false                          |
| `border_color`   | Table border color             | "#333333", "rgb(51,51,51)", "black"  |
| `border_width`   | Table border width             | "1pt", "2px", "0.03in"               |
| `cell_padding`   | Padding inside cells           | "0.05in", "0.127cm"                  |
| `table_style`    | Named table style              | "Light", "Medium", "Dark", "Accent1" |

#### Chart Properties

| Property          | Description        | Example Values                                    |
| ----------------- | ------------------ | ------------------------------------------------- |
| `chart_type`      | Type of chart      | "bar", "column", "line", "pie", "area", "scatter" |
| `title`           | Chart title        | "Sales Data"                                      |
| `has_legend`      | Show/hide legend   | true, false                                       |
| `legend_position` | Position of legend | "right", "left", "top", "bottom"                  |
| `x_axis_title`    | X-axis title       | "Categories"                                      |
| `y_axis_title`    | Y-axis title       | "Values"                                          |
| `data_labels`     | Show data labels   | true, false                                       |
| `data_table`      | Show data table    | true, false                                       |
| `gridlines`       | Show gridlines     | true, false                                       |

#### Animation Properties

| Property              | Description                      | Example Values                                     |
| --------------------- | -------------------------------- | -------------------------------------------------- |
| `animation`           | Animation type                   | "fade", "wipe", "fly_in", "float", "split", "zoom" |
| `animation_trigger`   | When animation starts            | "on_click", "with_previous", "after_previous"      |
| `animation_direction` | Direction of animation           | "in", "out", "up", "down", "left", "right"         |
| `animation_delay`     | Delay before animation (seconds) | 0, 0.5, 1                                          |
| `animation_duration`  | Animation duration (seconds)     | 0.5, 1, 2                                          |
| `animation_emphasis`  | Emphasis effect                  | "pulse", "color", "grow/shrink", "spin", "teeter"  |

#### Hyperlink Properties

| Property    | Description             | Example Values                                             |
| ----------- | ----------------------- | ---------------------------------------------------------- |
| `hyperlink` | Link destination        | "https://example.com", "slide3", "mailto:user@example.com" |
| `tooltip`   | Text displayed on hover | "Click for more information"                               |
| `action`    | Action when clicked     | "hyperlink", "next_slide", "previous_slide", "run_macro"   |

## Example Markdown File

Here's a complete example of a presentation with multiple slides:

```markdown
---
slide_width: 10in
slide_height: 7.5in
default_font: "Calibri"
default_font_size: 18
company_logo: "company_logo.png"
footer_text: "Company Confidential - 2025"
---

# Quarterly Report

{
layout: "Title Slide",
background: "#003366"
}

:::text[x:1in, y:2.5in, width:8in, height:1.5in]
{font: "Calibri", font_size: 44, font_color: "#FFFFFF", align: center, bold: true}
Q1 2025 Financial Results
:::

:::text[x:1in, y:4in, width:8in, height:1in]
{font: "Calibri", font_size: 28, font_color: "#FFFFFF", align: center}
Presented by: John Smith, CFO
:::

:::image[x:8in, y:0.5in, width:1.5in, height:0.75in]
company_logo.png
:::

# Executive Summary

{
layout: "Title and Content",
background: "#FFFFFF",
transition: "fade"
}

:::text[x:0.5in, y:0.8in, width:9in, height:0.75in]
{font: "Calibri", font_size: 36, font_color: "#003366", bold: true}
Q1 2025 Highlights
:::

:::text[x:0.5in, y:1.75in, width:9in, height:4in]
{font: "Calibri", font_size: 24, bullet: true}

- Record quarterly revenue of $125.7M (↑18% YoY)
- Operating margin increased to 28.3% (↑2.1 points YoY)
- Expanded customer base by 15% in North America
- Successfully launched 3 new product lines
- Completed acquisition of XYZ Technologies
  :::

:::image[x:8in, y:5.5in, width:1.5in, height:0.75in]
company_logo.png
:::

# Financial Results

{
layout: "Title and Content",
background: "#FFFFFF",
transition: "push"
}

:::text[x:0.5in, y:0.8in, width:9in, height:0.75in]
{font: "Calibri", font_size: 36, font_color: "#003366", bold: true}
Financial Performance
:::

:::chart[x:0.5in, y:1.75in, width:4.5in, height:3in]
{
chart_type: "column",
title: "Quarterly Revenue",
has_legend: true,
legend_position: "bottom",
x_axis_title: "Quarter",
y_axis_title: "Revenue ($ millions)"
}
Q1 2024, 106.5
Q2 2024, 110.3
Q3 2024, 118.2
Q4 2024, 122.1
Q1 2025, 125.7
:::

:::chart[x:5.25in, y:1.75in, width:4.25in, height:3in]
{
chart_type: "line",
title: "Operating Margin (%)",
has_legend: false,
x_axis_title: "Quarter",
y_axis_title: "Margin (%)",
data_labels: true
}
Q1 2024, 26.2
Q2 2024, 26.8
Q3 2024, 27.1
Q4 2024, 27.5
Q1 2025, 28.3
:::

:::table[x:0.5in, y:5in, width:9in, height:1.5in]
{
header_row: true,
first_column: true,
banded_rows: true
}
| Metric | Q1 2024 | Q2 2024 | Q3 2024 | Q4 2024 | Q1 2025 | YoY Change |
| Revenue | $106.5M | $110.3M | $118.2M | $122.1M | $125.7M | +18.0% |
| Gross Margin | 68.5% | 69.2% | 69.8% | 70.3% | 71.2% | +2.7pts |
| Op. Margin | 26.2% | 26.8% | 27.1% | 27.5% | 28.3% | +2.1pts |
| Net Income | $22.4M | $23.7M | $25.6M | $26.8M | $28.5M | +27.2% |
:::

# Product Roadmap

{
background: "#FFFFFF",
transition: "fade"
}

:::text[x:0.5in, y:0.8in, width:9in, height:0.75in]
{font: "Calibri", font_size: 36, font_color: "#003366", bold: true}
Product Timeline
:::

:::shape[x:0.5in, y:2in, width:1.5in, height:1.5in]
{
shape_type: "oval",
fill: "#4472C4",
border_color: "#2F528F",
border_width: 2pt,
font_color: "#FFFFFF",
align: "center",
vertical_align: "middle",
font_size: 20,
bold: true
}
Q2 2025
:::

:::shape[x:2.75in, y:2in, width:1.5in, height:1.5in]
{
shape_type: "oval",
fill: "#70AD47",
border_color: "#507E32",
border_width: 2pt,
font_color: "#FFFFFF",
align: "center",
vertical_align: "middle",
font_size: 20,
bold: true
}
Q3 2025
:::

:::shape[x:5in, y:2in, width:1.5in, height:1.5in]
{
shape_type: "oval",
fill: "#ED7D31",
border_color: "#AE5A21",
border_width: 2pt,
font_color: "#FFFFFF",
align: "center",
vertical_align: "middle",
font_size: 20,
bold: true
}
Q4 2025
:::

:::shape[x:7.25in, y:2in, width:1.5in, height:1.5in]
{
shape_type: "oval",
fill: "#5B9BD5",
border_color: "#41719C",
border_width: 2pt,
font_color: "#FFFFFF",
align: "center",
vertical_align: "middle",
font_size: 20,
bold: true
}
Q1 2026
:::

:::text[x:0.25in, y:3.75in, width:2in, height:2in]
{font_size: 16, align: "center"}

- Platform 2.0 Release
- Mobile Integration
- API Expansion
  :::

:::text[x:2.5in, y:3.75in, width:2in, height:2in]
{font_size: 16, align: "center"}

- Cloud Migration
- Enhanced Analytics
- Partner Portal
  :::

:::text[x:4.75in, y:3.75in, width:2in, height:2in]
{font_size: 16, align: "center"}

- AI Features
- Global Expansion
- Enterprise Edition
  :::

:::text[x:7in, y:3.75in, width:2in, height:2in]
{font_size: 16, align: "center"}

- Next-Gen Platform
- Blockchain Integration
- IoT Compatibility
  :::

# Thank You

{
layout: "Title Slide",
background: "#003366",
transition: "fade"
}

:::text[x:1in, y:2.5in, width:8in, height:1.5in]
{font: "Calibri", font_size: 48, font_color: "#FFFFFF", align: center, bold: true}
Thank You!
:::

:::text[x:1in, y:4in, width:8in, height:1in]
{font: "Calibri", font_size: 24, font_color: "#FFFFFF", align: center}
Questions & Answers
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
hyperlink: "mailto:john.smith@company.com",
tooltip: "Send email with questions"
}
Contact: john.smith@company.com
:::
```

## Working with Units

The system supports various units for position and size specifications:

- `in`: Inches (default if no unit specified)
- `cm`: Centimeters
- `pt`: Points (1/72 of an inch)
- `px`: Pixels (approximate conversion)

## Working with Colors

Colors can be specified in multiple formats:

- Hex: `#FF0000`, `#F00`
- RGB: `rgb(255,0,0)`
- Named colors: `red`, `blue`, `green`, etc.

## Tips and Best Practices

1. **Organizing Content**:

   - Use global settings for consistent presentation styles
   - Group related slides with level 2 headings
   - Use comments to mark sections: `<!-- Section: Financial Results -->`

2. **Layout and Positioning**:

   - Use precise coordinates for complex layouts
   - Test your presentation with different screen resolutions
   - Consider using relative positioning for better adaptability

3. **Styling**:

   - Maintain consistent fonts and colors throughout
   - Use the company style guide for visual elements
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

4. **Table layout issues**:
   - Check row/column consistency
   - Adjust table dimensions if content is cut off
   - Use consistent delimiters (commas or pipe characters)

## Known Limitations

- Some advanced PowerPoint features may require post-processing
- Animation effects are limited to basic types
- Chart customization options are more limited than native PowerPoint
- Complex SmartArt is not fully supported
- Embedded video support is limited

## Advanced Features

### Template Support

You can specify a PowerPoint template file as a base:

```markdown
---
template: "company_template.potx"
---
```

### Master Slide Controls

Control which master slides to use:

```markdown
---
master_slides: ["Title Slide", "Content with Caption", "Comparison"]
---
```

### Slide Section Organization

Organize slides into sections:

```markdown
<!-- {section: "Introduction"} -->

# Welcome Slide

<!-- {section: "Financial Data"} -->

# Q1 Results
```

### Smart Art (Basic Support)

Create simple SmartArt diagrams:

```markdown
:::smartart
{
x: 1in,
y: 1in,
width: 8in,
height: 3in,
type: "process",
direction: "horizontal"
}
Step 1, Step 2, Step 3, Step 4
:::
```

### Media Embedding

Embed video or audio (limited support):

```markdown
:::media
{
x: 1in,
y: 1in,
width: 6in,
height: 4in,
type: "video",
autoplay: false
}
/path/to/video.mp4
:::
```

## Contributing

Contributions to improve the conversion tool are welcome. Please submit issues and pull requests to the project repository.

## License

This tool is licensed under the MIT License. See the LICENSE file for details.

---

_This README was generated by the Markdown to PowerPoint Converter tool._
