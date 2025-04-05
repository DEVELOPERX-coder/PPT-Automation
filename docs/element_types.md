# Element Types Reference

This document provides detailed information about the various element types supported by the PowerPoint Automation tool, including their properties, usage examples, and best practices.

## Table of Contents

- [Text Boxes](#text-boxes)
- [Shapes](#shapes)
- [Images](#images)
- [Tables](#tables)
- [Charts](#charts)
- [Code Blocks](#code-blocks)

## Text Boxes

Text boxes are flexible elements for displaying formatted text anywhere on a slide.

### Properties

| Property       | Type         | Default    | Description                                                   |
| -------------- | ------------ | ---------- | ------------------------------------------------------------- |
| `type`         | string       | (required) | Must be `"text_box"`                                          |
| `left`         | number       | 1          | Distance from left edge in inches                             |
| `top`          | number       | 1          | Distance from top edge in inches                              |
| `width`        | number       | 4          | Width in inches                                               |
| `height`       | number       | 1          | Height in inches                                              |
| `text`         | string       | ""         | The text content                                              |
| `font`         | string       | "Calibri"  | Font family name                                              |
| `size`         | number       | 18         | Font size in points                                           |
| `color`        | string/array | [0,0,0]    | Text color (see color formats)                                |
| `bold`         | boolean      | false      | Whether text is bold                                          |
| `italic`       | boolean      | false      | Whether text is italic                                        |
| `underline`    | boolean      | false      | Whether text is underlined                                    |
| `align`        | string       | "left"     | Text alignment (`"left"`, `"center"`, `"right"`, `"justify"`) |
| `line_spacing` | number       | 1.0        | Line spacing multiplier                                       |

### Example

```yaml
- type: text_box
  left: 1
  top: 2
  width: 10
  height: 1.5
  text: "Important Information\nThis is a second line of text."
  font: "Arial"
  size: 24
  color: [0, 112, 192]
  bold: true
  align: "center"
```

### Best Practices

- For longer text, increase the height to ensure all content is visible
- Use line breaks (`\n`) to create multi-line text
- Consider using variables for consistent text styling across slides
- Limit width to around 10 inches for readability (standard slide width is 13.33 inches)

## Shapes

Shapes provide visual elements like rectangles, circles, arrows, etc., optionally with text.

### Properties

| Property     | Type         | Default       | Description                       |
| ------------ | ------------ | ------------- | --------------------------------- |
| `type`       | string       | (required)    | Must be `"shape"`                 |
| `shape_type` | string       | "rectangle"   | Type of shape (see list below)    |
| `left`       | number       | 1             | Distance from left edge in inches |
| `top`        | number       | 1             | Distance from top edge in inches  |
| `width`      | number       | 2             | Width in inches                   |
| `height`     | number       | 1             | Height in inches                  |
| `fill_color` | string/array | [255,255,255] | Shape fill color                  |
| `line_color` | string/array | [0,0,0]       | Border line color                 |
| `line_width` | number       | 1             | Border line width in points       |
| `text`       | string       | ""            | Text inside the shape             |
| `text_color` | string/array | [0,0,0]       | Color of text inside the shape    |
| `font`       | string       | "Calibri"     | Font for text inside shape        |
| `size`       | number       | 18            | Font size for text inside shape   |
| `bold`       | boolean      | false         | Whether text is bold              |
| `italic`     | boolean      | false         | Whether text is italic            |
| `align`      | string       | "center"      | Text alignment inside shape       |

### Available Shape Types

**Basic Shapes:**

- `rectangle` - Standard rectangle
- `rounded_rectangle` - Rectangle with rounded corners
- `oval` - Oval or circle (depending on dimensions)
- `triangle` - Triangle
- `right_triangle` - Right-angled triangle

**Polygons:**

- `pentagon` - 5-sided polygon
- `hexagon` - 6-sided polygon
- `heptagon` - 7-sided polygon
- `octagon` - 8-sided polygon

**Stars:**

- `star` - 5-pointed star (same as `star5`)
- `star4` - 4-pointed star
- `star5` - 5-pointed star
- `star6` - 6-pointed star
- `star7` - 7-pointed star
- `star8` - 8-pointed star

**Arrows:**

- `arrow` - Standard arrow (right pointing)
- `up_arrow` - Upward pointing arrow
- `down_arrow` - Downward pointing arrow
- `left_arrow` - Left pointing arrow
- `right_arrow` - Right pointing arrow
- `left_right_arrow` - Two-headed horizontal arrow
- `up_down_arrow` - Two-headed vertical arrow

**Special Shapes:**

- `cloud` - Cloud shape
- `heart` - Heart shape
- `lightning` - Lightning bolt
- `sun` - Sun
- `moon` - Crescent moon
- `smiley` - Smiley face
- `no_symbol` - 'Prohibited' symbol (circle with slash)
- `arc` - Arc
- `plaque` - Plaque or sign
- `can` - Cylindrical shape
- `cube` - 3D cube
- `bevel` - Beveled rectangle
- `donut` - Ring/donut shape
- `pie` - Pie/wedge shape
- `block_arc` - Block arc
- `folded_corner` - Rectangle with folded corner
- `frame` - Picture frame

### Example

```yaml
- type: shape
  shape_type: rounded_rectangle
  left: 2
  top: 3
  width: 4
  height: 2
  fill_color: [0, 112, 192]
  line_color: [0, 64, 128]
  line_width: 2
  text: "Key Insight"
  text_color: "white"
  font: "Arial"
  size: 20
  bold: true
  align: "center"
```

### Best Practices

- For shapes with text, ensure dimensions are large enough for the text to be readable
- Use consistent colors for similar types of shapes across your presentation
- Consider using shapes without text as decorative elements or dividers
- For arrow shapes, adjust the dimensions to control the arrow proportions

## Images

Images allow you to incorporate visual content from local files.

### Properties

| Property | Type   | Default    | Description                       |
| -------- | ------ | ---------- | --------------------------------- |
| `type`   | string | (required) | Must be `"image"`                 |
| `path`   | string | (required) | Path to the image file            |
| `left`   | number | 1          | Distance from left edge in inches |
| `top`    | number | 1          | Distance from top edge in inches  |
| `width`  | number | (auto)     | Width in inches                   |
| `height` | number | (auto)     | Height in inches                  |

### Example

```yaml
- type: image
  path: "images/product_photo.jpg"
  left: 2
  top: 2
  width: 6 # If only width is specified, height will be calculated to maintain aspect ratio
```

### Best Practices

- Image paths are relative to the directory where you run the script
- For best results, use high-resolution images (at least 150 DPI)
- If you specify only one dimension (width or height), the other will be calculated automatically to maintain the image's aspect ratio
- PowerPoint works best with common image formats: JPG, PNG, GIF, BMP
- Consider organizing images in an `images/` subdirectory for better project structure

## Tables

Tables display structured data in rows and columns.

### Properties

| Property     | Type    | Default    | Description                       |
| ------------ | ------- | ---------- | --------------------------------- |
| `type`       | string  | (required) | Must be `"table"`                 |
| `left`       | number  | 1          | Distance from left edge in inches |
| `top`        | number  | 1          | Distance from top edge in inches  |
| `width`      | number  | 8          | Width in inches                   |
| `height`     | number  | (auto)     | Height in inches                  |
| `data`       | array   | (required) | 2D array of table data            |
| `has_header` | boolean | true       | Whether the first row is a header |
| `style`      | object  | {}         | Table styling options             |

#### Style Object Properties

| Property              | Type         | Default       | Description              |
| --------------------- | ------------ | ------------- | ------------------------ |
| `zebra_striping`      | boolean      | false         | Alternate row colors     |
| `alternate_row_color` | string/array | [245,245,245] | Color for alternate rows |

### Example

```yaml
- type: table
  left: 1
  top: 2
  width: 10
  height: 4
  has_header: true
  data:
    - ["Product", "Q1 Sales", "Q2 Sales", "Q3 Sales", "Q4 Sales"]
    - ["Product A", "$10,500", "$12,300", "$14,700", "$15,200"]
    - ["Product B", "$8,200", "$9,100", "$11,500", "$13,800"]
    - ["Product C", "$5,300", "$6,700", "$7,200", "$8,500"]
    - ["Product D", "$3,100", "$3,800", "$4,500", "$5,200"]
  style:
    zebra_striping: true
    alternate_row_color: [240, 240, 240]
```

#### Example with Complex Cell Formatting

```yaml
- type: table
  left: 1
  top: 2
  width: 10
  data:
    - ["Metric", "Current Value", "Status"]
    - [
        "Revenue",
        "$1.2M",
        {
          "text": "Above Target",
          "style":
            {
              "font": "Arial",
              "size": 14,
              "bold": true,
              "color": [0, 128, 0],
              "fill_color": [220, 255, 220],
            },
        },
      ]
    - [
        "Expenses",
        "$0.8M",
        {
          "text": "Below Target",
          "style":
            {
              "font": "Arial",
              "size": 14,
              "bold": true,
              "color": [128, 0, 0],
              "fill_color": [255, 220, 220],
            },
        },
      ]
```

### Best Practices

- Keep tables simple and readable - avoid too many columns or excessive text
- Use the `has_header` option to properly style the header row
- Consider using zebra striping for better readability of multi-row tables
- Cell content is automatically wrapped if it doesn't fit, but keep text concise
- For numeric data, ensure consistent formatting (e.g., all currency with same decimal places)

## Charts

Charts visualize data relationships and trends.

### Properties

| Property     | Type   | Default    | Description                        |
| ------------ | ------ | ---------- | ---------------------------------- |
| `type`       | string | (required) | Must be `"chart"`                  |
| `chart_type` | string | "column"   | Type of chart (see list below)     |
| `left`       | number | 1          | Distance from left edge in inches  |
| `top`        | number | 1          | Distance from top edge in inches   |
| `width`      | number | 8          | Width in inches                    |
| `height`     | number | 5          | Height in inches                   |
| `title`      | string | ""         | Chart title                        |
| `data`       | object | (required) | Chart data (categories and series) |

#### Chart Data Object

| Property     | Type  | Default | Description                                    |
| ------------ | ----- | ------- | ---------------------------------------------- |
| `categories` | array | []      | Labels for data points (x-axis in most charts) |
| `series`     | array | []      | Array of data series objects                   |

#### Series Object

| Property | Type   | Default | Description                          |
| -------- | ------ | ------- | ------------------------------------ |
| `name`   | string | ""      | Name of the data series (for legend) |
| `values` | array  | []      | Numeric values for the series        |

### Available Chart Types

- `column` - Vertical bar chart (clustered)
- `stacked_column` - Stacked vertical bar chart
- `bar` - Horizontal bar chart (clustered)
- `stacked_bar` - Stacked horizontal bar chart
- `line` - Line chart
- `pie` - Pie chart
- `doughnut` - Doughnut chart
- `area` - Area chart
- `scatter` - Scatter plot
- `radar` - Radar/spider chart

### Example

```yaml
- type: chart
  chart_type: line
  left: 1
  top: 2
  width: 8
  height: 5
  title: "Monthly Sales Trends"
  data:
    categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    series:
      - name: "2024"
        values: [12.5, 13.8, 14.2, 15.1, 16.5, 17.2]
      - name: "2025"
        values: [13.2, 14.5, 16.0, 17.8, 19.2, 21.0]
```

### Best Practices

- Choose the appropriate chart type for your data:
  - Use `column`/`bar` for comparing discrete categories
  - Use `line` for showing trends over time
  - Use `pie`/`doughnut` for showing parts of a whole
  - Use `scatter` for showing correlations between variables
- Limit the number of data series to maintain readability (usually 3-5 maximum)
- Provide clear, concise labels for categories and series
- Ensure data values use consistent units and scales
- Consider adjusting width and height based on the complexity of your chart

## Code Blocks

Code blocks display formatted programming code with syntax highlighting.

### Properties

| Property           | Type         | Default    | Description                       |
| ------------------ | ------------ | ---------- | --------------------------------- |
| `type`             | string       | (required) | Must be `"code"`                  |
| `left`             | number       | 1          | Distance from left edge in inches |
| `top`              | number       | 1          | Distance from top edge in inches  |
| `width`            | number       | 8          | Width in inches                   |
| `height`           | number       | 4          | Height in inches                  |
| `code`             | string       | (required) | The code content                  |
| `font`             | string       | "Consolas" | Monospace font for code           |
| `size`             | number       | 14         | Font size in points               |
| `color`            | string/array | [0,200,0]  | Text color for code               |
| `background`       | boolean      | true       | Whether to show background        |
| `background_color` | string/array | [32,32,32] | Background color for code block   |

### Example

```yaml
- type: code
  left: 1
  top: 2
  width: 10
  height: 5
  code: |
    # Python example
    def fibonacci(n):
        """Generate the first n Fibonacci numbers."""
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib[:n]

    numbers = fibonacci(10)
    print(f"First 10 Fibonacci numbers: {numbers}")
  font: "Consolas"
  size: 16
  color: [0, 230, 0]
  background: true
  background_color: "#202020"
```

### Best Practices

- Use monospace fonts for better code readability (e.g., "Consolas", "Courier New")
- Ensure the code block dimensions are large enough for your code to be readable
- Use the pipe character (`|`) in YAML for multi-line strings to preserve formatting
- Add comments to explain complex code segments
- Keep code examples concise and focused on the key concepts
- Use syntax highlighting colors that have good contrast with the background
- Consider using a slightly larger font size than typical code editors for better visibility during presentations
