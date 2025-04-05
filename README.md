# PowerPoint Automation Project

A Python-based tool for automating the creation of PowerPoint presentations from custom-formatted input files.

## Features

- Convert YAML, JSON, or simple text files into professional PowerPoint presentations
- Support for various slide types (title, content, two-column, section headers, etc.)
- Variable substitution for dynamic content
- Custom styling and theming
- Image and shape support
- Command-line interface for easy integration into workflows

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/ppt-automator.git
   cd ppt-automator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

Generate a PowerPoint presentation from an input file:

```bash
python main.py path/to/input_file.yaml
```

### Advanced Options

```bash
python main.py path/to/input_file.yaml -o output.pptx -t template.pptx -v
```

Options:

- `-o, --output`: Specify the output PowerPoint file path
- `-t, --template`: Use a PowerPoint template file as a base
- `-v, --verbose`: Enable verbose logging

## Input File Format

The tool supports three input formats: YAML, JSON, and simple text. YAML is the recommended format for its readability and structure.

### YAML Format

```yaml
# Define variables that can be referenced throughout the document
variables:
  company_name: "Acme Corporation"
  presenter: "John Smith"
  date: "April 5, 2025"

# Presentation-wide settings
settings:
  style:
    title_font: "Calibri"
    title_size: 44
    body_font: "Calibri"
    body_size: 18
    theme_color: [41, 105, 176] # RGB values for primary color

# Slides definition
slides:
  # Title slide
  - type: title_slide
    title: "{{company_name}} Quarterly Report"
    subtitle: "Presented by {{presenter}} | {{date}}"

  # Content slide with bullets
  - type: title_and_content
    title: "Agenda"
    content:
      - "Item 1"
      - "Item 2"
      - "Item 3"

  # Slide with an image
  - type: title_and_content
    title: "Product Highlights"
    content: "This is our flagship product."
    image:
      path: "path/to/image.png"
      left: 5
      top: 2.5
      width: 4
      height: 3
```

### Text Format

Simple text format is also supported:

```
# Main Presentation Title
* Presented by John Smith

---

## Agenda

- Item 1
- Item 2
- Item 3

---

## Product Highlights

This is our flagship product.

!image: path/to/image.jpg
```

## Supported Slide Types

| Type                | Description                          |
| ------------------- | ------------------------------------ |
| `title_slide`       | Title slide with optional subtitle   |
| `title_and_content` | Title with content (text or bullets) |
| `section`           | Section header slide                 |
| `two_content`       | Slide with two columns of content    |
| `title_only`        | Slide with title and custom elements |
| `blank`             | Blank slide with custom elements     |

## Variables

You can define variables at the top of your input file and reference them throughout using the `{{variable_name}}` syntax. This is useful for:

- Company names, presenter information, dates
- Repeated values or data points
- Ensuring consistency across the presentation

## Custom Elements

For `title_only` and `blank` slide types, you can add custom elements:

```yaml
elements:
  - type: text_box
    left: 1
    top: 2
    width: 8
    height: 1
    text: "Custom text box"
    font: "Calibri"
    size: 20

  - type: shape
    shape_type: star
    left: 5
    top: 3
    width: 2
    height: 2
    fill_color: [255, 215, 0] # Gold
    text: "93%"
```

## Formatting Guidelines

### Position and Size

All position and size values are specified in inches:

- `left`: Distance from the left edge of the slide
- `top`: Distance from the top edge of the slide
- `width`: Width of the element
- `height`: Height of the element

### Colors

Colors can be specified in several formats:

- RGB array: `[255, 0, 0]` (red)
- Hex: `"#FF0000"` (red)
- Named color: `"red"`

## Examples

Check the `examples/` directory for sample input files and their corresponding PowerPoint outputs.

## Best Practices

1. **Start with a template**: Create a YAML file based on the examples provided in the `examples/` directory.

2. **Use variables**: Define variables for any repeated content to ensure consistency.

3. **Organize with sections**: Use section slides to create a clear structure in your presentation.

4. **Test incrementally**: Start with a few slides and add more as you verify the output.

5. **Custom styling**: Define presentation-wide styling in the `settings` section.

## Troubleshooting

### Common Issues

- **Images not appearing**: Ensure image paths are correct and accessible.
- **Variable not replacing**: Check for typos in variable names. Variable references are case-sensitive.
- **Slide layout issues**: Verify positioning values (left, top, width, height) are appropriate.

### Error Messages

- "Image not found": Check that the image file exists at the specified path.
- "Error parsing YAML file": Validate your YAML syntax using an online YAML validator.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
