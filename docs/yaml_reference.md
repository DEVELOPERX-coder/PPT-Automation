# PowerPoint Automation YAML Reference

This document provides a comprehensive reference for the YAML configuration format used by the PowerPoint Automation tool. All available options and their usage are detailed below.

## Table of Contents

- [Top-Level Structure](#top-level-structure)
- [Variables](#variables)
- [Settings](#settings)
  - [Theme Settings](#theme-settings)
  - [Presentation Properties](#presentation-properties)
- [Slides](#slides)
  - [Common Slide Properties](#common-slide-properties)
  - [Slide Types](#slide-types)
- [Elements](#elements)
  - [Text Boxes](#text-boxes)
  - [Shapes](#shapes)
  - [Images](#images)
  - [Tables](#tables)
  - [Charts](#charts)
  - [Code Blocks](#code-blocks)
- [Color Formats](#color-formats)
- [Variable Substitution](#variable-substitution)

## Top-Level Structure

A YAML configuration file consists of three main sections:

```yaml
variables:
  # Variables used throughout the presentation

settings:
  # Presentation-wide settings

slides:
  # Individual slide definitions
```

## Variables

The `variables` section defines values that can be used throughout your presentation. This allows for consistent and easily updatable content.

```yaml
variables:
  company_name: "Acme Corporation"
  presenter: "John Smith"
  primary_color: [0, 112, 192] # RGB Blue
  secondary_color: "#FFC000" # Hex Yellow
  dark_bg: [44, 44, 44] # Dark gray
  current_date: "April 5, 2025"
```

Variables can be referenced elsewhere in the YAML using the `{{variable_name}}` syntax. See [Variable Substitution](#variable-substitution) for details.

## Settings

The `settings` section defines presentation-wide options, divided into `theme` and `properties` subsections.

### Theme Settings

Theme settings control the visual appearance of the presentation:

```yaml
settings:
  theme:
    fonts:
      title:
        name: "Calibri"
        size: 44
      subtitle:
        name: "Calibri"
        size: 32
      body:
        name: "Calibri"
        size: 18

    colors:
      background: "#FFFFFF" # Slide background
      title: [0, 112, 192] # Title text color
      text: [0, 0, 0] # Body text color
      accent: [255, 192, 0] # Accent color for highlights
```

### Presentation Properties

Presentation properties set metadata for the PowerPoint file:

```yaml
settings:
  properties:
    title: "Quarterly Business Report"
    author: "John Smith"
    subject: "Q1 2025 Results"
    keywords: "quarterly, results, business"
    comments: "Internal use only"
    category: "Financial Reports"
```

## Slides

The `slides` section is an array of slide definitions, each with its own type and content.

### Common Slide Properties

All slide types support these properties:

- `type`: The slide layout type (required)
- `title`: Title text for the slide (optional for some types)
- `background`: Background settings (color or image)
- `elements`: Array of custom elements to add to the slide
- `animations`: Animation settings (currently unsupported)

### Slide Types

#### Title Slide (`type: title`)

```yaml
- type: title
  title: "Quarterly Business Report"
  subtitle: "Q1 2025 Results"
  background:
    color: [44, 44, 44]
```

#### Title and Content Slide (`type: title_and_content`)

```yaml
- type: title_and_content
  title: "Agenda"
  content:
    - "Company Overview"
    - "Financial Results"
    - "Future Outlook"
    - "Q&A"
```

Content can also be a string for plain text or a complex object for charts, tables, etc.:

```yaml
- type: title_and_content
  title: "Revenue Growth"
  content:
    type: chart
    chart_type: column
    title: "Quarterly Revenue"
    data:
      categories: ["Q1", "Q2", "Q3", "Q4"]
      series:
        - name: "2024"
          values: [1.2, 1.5, 1.7, 1.9]
        - name: "2025"
          values: [1.4, 1.8, 2.1, 2.3]
```

#### Section Header Slide (`type: section`)

```yaml
- type: section
  title: "Financial Results"
  background:
    color: [44, 44, 44]
```

#### Two Content Slide (`type: two_content`)

```yaml
- type: two_content
  title: "Comparison"
  left_content:
    - "Advantages"
    - "Feature A"
    - "Feature B"
  right_content:
    - "Limitations"
    - "Issue X"
    - "Issue Y"
```

Complex content objects are also supported in each column:

```yaml
- type: two_content
  title: "Product Comparison"
  left_content:
    type: image
    path: "images/product_a.png"
  right_content:
    type: table
    data:
      - ["Feature", "Value"]
      - ["Speed", "120 mph"]
      - ["Weight", "150 lbs"]
```

#### Title Only Slide (`type: title_only`)

```yaml
- type: title_only
  title: "Questions?"
```

#### Blank Slide (`type: blank`)

```yaml
- type: blank
  elements:
    - type: text_box
      left: 1
      top: 1
      width: 10
      height: 1
      text: "Custom Layout"
    # More elements...
```

## Elements

Elements are individual components that can be added to slides, especially useful with blank slides or to augment standard layouts.

Common properties for all elements:

- `type`: Element type (required)
- `left`: Distance from left edge in inches (default: 1)
- `top`: Distance from top edge in inches (default: 1)
- `width`: Width in inches (default varies by element type)
- `height`: Height in inches (default varies by element type)

### Text Boxes

```yaml
- type: text_box
  left: 1
  top: 1
  width: 8
  height: 1
  text: "This is a text box"
  font: "Calibri"
  size: 18
  color: [0, 0, 0]
  bold: false
  italic: false
  underline: false
  align: "left" # left, center, right, justify
```

### Shapes

```yaml
- type: shape
  shape_type: rectangle # see list below
  left: 2
  top: 2
  width: 4
  height: 2
  fill_color: [0, 112, 192]
  line_color: [0, 0, 0]
  line_width: 1
  text: "Text in shape"
  text_color: [255, 255, 255]
  font: "Calibri"
  size: 18
  bold: false
  align: "center"
```

Available shape types:

- Basic shapes: `rectangle`, `rounded_rectangle`, `oval`, `triangle`, `right_triangle`
- Polygons: `pentagon`, `hexagon`, `heptagon`, `octagon`
- Stars: `star`, `star4`, `star5`, `star6`, `star7`, `star8`
- Arrows: `arrow`, `up_arrow`, `down_arrow`, `left_arrow`, `right_arrow`, `left_right_arrow`, `up_down_arrow`
- Special shapes: `cloud`, `heart`, `lightning`, `sun`, `moon`, `smiley`, `no_symbol`, `arc`, `plaque`, `can`, `cube`, `bevel`, `donut`, `pie`, `block_arc`, `folded_corner`, `frame`

### Images

```yaml
- type: image
  path: "images/logo.png"
  left: 2
  top: 2
  width: 4 # Optional, maintains aspect ratio if only one dimension specified
  height: 3 # Optional, maintains aspect ratio if only one dimension specified
```

### Tables

```yaml
- type: table
  left: 1
  top: 2
  width: 8
  height: 4
  has_header: true
  data:
    - ["Name", "Position", "Department"] # Header row
    - ["John Smith", "CEO", "Executive"]
    - ["Jane Doe", "CTO", "Technology"]
    - ["Bob Johnson", "CFO", "Finance"]
  style:
    zebra_striping: true
    alternate_row_color: [245, 245, 245]
```

For complex cell formatting:

```yaml
- type: table
  data:
    - ["Header 1", "Header 2", "Header 3"]
    - [
        "Simple cell",
        {
          "text": "Formatted cell",
          "style":
            {
              "font": "Arial",
              "size": 12,
              "bold": true,
              "color": [255, 0, 0],
              "fill_color": [240, 240, 240],
            },
        },
        "Another cell",
      ]
```

### Charts

```yaml
- type: chart
  chart_type: column # column, bar, line, pie, doughnut, area, scatter, radar
  left: 1
  top: 2
  width: 8
  height: 5
  title: "Sales by Quarter"
  data:
    categories: ["Q1", "Q2", "Q3", "Q4"]
    series:
      - name: "2024"
        values: [1.2, 1.5, 1.7, 1.9]
      - name: "2025"
        values: [1.4, 1.8, 2.1, 2.3]
```

### Code Blocks

```yaml
- type: code
  left: 1
  top: 2
  width: 10
  height: 5
  code: |
    def calculate_sum(a, b):
        """Add two numbers and return the result."""
        return a + b

    result = calculate_sum(5, 10)
    print(f"The sum is {result}")
  font: "Consolas"
  size: 14
  color: [0, 200, 0]
  background: true
  background_color: "#202020"
```

## Color Formats

Colors can be specified in several formats:

1. **RGB Array**: `[r, g, b]` with values from 0-255

   ```yaml
   primary_color: [0, 112, 192] # Blue
   ```

2. **Hex Color**: A string starting with '#' followed by 3 or 6 hex digits

   ```yaml
   highlight_color: "#FF0000" # Red
   ```

3. **Named Color**: Predefined color names

   ```yaml
   background_color: "black"
   ```

   Supported named colors: `black`, `white`, `red`, `green`, `blue`, `yellow`, `purple`, `orange`, `gray`, `light_gray`, `dark_gray`, `cyan`, `magenta`, `pink`, `brown`, `navy`, `teal`

## Variable Substitution

Variables can be referenced using the `{{variable_name}}` syntax:

```yaml
variables:
  company_name: "Acme Corporation"
  primary_color: [0, 112, 192]

slides:
  - type: title
    title: "{{company_name}} Annual Report"
    background:
      color: "{{primary_color}}"
```

Variables work in most string and color fields throughout the YAML configuration.
