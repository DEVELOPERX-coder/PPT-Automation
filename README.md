# PowerPoint Automation Project

A comprehensive Python project for automating the creation of PowerPoint presentations using YAML configuration files. This tool allows you to dynamically generate professionally formatted presentations with full customization of shapes, text, colors, layouts, and other PowerPoint elements.

## 🌟 Features

- **Flexible YAML Configuration**: Define entire presentations with a structured, easy-to-read YAML format
- **Dynamic Templating**: Use variables throughout your presentation for consistent branding and easy updates
- **Rich Element Support**: Create and customize:
  - Various slide layouts (title slides, content slides, section headers, etc.)
  - Shapes with customizable properties (rectangles, ovals, arrows, etc.)
  - Text boxes with rich formatting options
  - Tables and charts for data visualization
  - Code blocks with syntax highlighting
  - Images with automatic sizing and positioning
- **Comprehensive Styling**: Control fonts, colors, alignment, and other visual properties
- **Input Validation**: Robust error checking to ensure your YAML configuration is valid
- **Template-based Design**: Start with pre-built templates for common presentation types

## 📋 Requirements

- Python 3.7 or higher
- Required Python packages (see `requirements.txt`):
  - python-pptx
  - PyYAML
  - jsonschema
  - Pillow (for image processing)

## 🚀 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/ppt-automator.git
   cd ppt-automator
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## 🛠️ Usage

### Basic Usage

Generate a PowerPoint presentation from a YAML file:

```bash
python main.py examples/basic_presentation.yaml
```

### Advanced Options

```bash
python main.py examples/business_report.yaml -o my_report.pptx -t template.pptx -v
```

Options:

- `-o, --output`: Specify the output PowerPoint file path
- `-t, --template`: Use a PowerPoint template file as a base
- `--validate-only`: Only validate the YAML file without generating a presentation
- `-v, --verbose`: Enable verbose logging

### Creating Your Own Presentations

1. Start by examining the example YAML files in the `examples/` directory
2. Copy and modify one of the examples to fit your needs
3. Check the [YAML Reference](docs/yaml_reference.md) for detailed information about available options
4. Validate your YAML file: `python main.py your_file.yaml --validate-only`
5. Generate your presentation: `python main.py your_file.yaml -o your_presentation.pptx`

## 🏗️ Project Structure

```
ppt-automator/
├── src/                      # Source code
│   ├── ppt_generator.py      # Core PowerPoint generation functionality
│   ├── slide_builder.py      # Slide creation and configuration
│   ├── element_factory.py    # Individual element creation
│   ├── validators.py         # YAML validation
│   └── utils.py              # Utility functions
├── examples/                 # Example YAML files
│   ├── basic_presentation.yaml
│   ├── business_report.yaml
│   └── educational_slides.yaml
├── docs/                     # Documentation
│   ├── yaml_reference.md     # Detailed YAML format documentation
│   ├── element_types.md      # Information about supported elements
│   └── troubleshooting.md    # Common issues and solutions
├── main.py                   # Command-line interface
├── requirements.txt          # Project dependencies
└── README.md                 # This file
```

## 📝 YAML Structure

Your YAML file should have the following structure:

```yaml
# Variables for use throughout the presentation
variables:
  company_name: "Acme Corporation"
  primary_color: [0, 112, 192] # RGB values

# Presentation-wide settings
settings:
  theme:
    fonts:
      title:
        name: "Calibri"
        size: 44
      # More font settings...
    colors:
      background: "#FFFFFF"
      # More color settings...
  properties:
    title: "Presentation Title"
    # More properties...

# Slides definition
slides:
  # Title slide
  - type: title
    title: "{{company_name}} Presentation"
    subtitle: "Created with PowerPoint Automator"

  # Content slide
  - type: title_and_content
    title: "Agenda"
    content:
      - "Item 1"
      - "Item 2"
      - "Item 3"

  # Custom slide with elements
  - type: blank
    elements:
      - type: text_box
        left: 1
        top: 1
        width: 8
        height: 1
        text: "Custom Text"
        # More text formatting options...

      - type: shape
        shape_type: rectangle
        left: 2
        top: 3
        width: 4
        height: 2
        fill_color: "{{primary_color}}"
        # More shape options...
```

For complete documentation of all available options, see [YAML Reference](docs/yaml_reference.md).

## 🎨 Customization Options

### Slide Types

- `title`: Title slide with title and subtitle
- `title_and_content`: Standard slide with title and content
- `section`: Section header slide
- `two_content`: Slide with two columns of content
- `title_only`: Slide with only a title
- `blank`: Empty slide for custom elements

### Element Types

- `text_box`: Formatted text
- `shape`: Various shapes with optional text
- `image`: Pictures from local files
- `table`: Tabular data with formatting
- `chart`: Data visualizations
- `code`: Formatted code blocks

For full details on element options, see [Element Types](docs/element_types.md).

## 📊 Example Use Cases

- **Business Reports**: Quarterly/annual reports, financial presentations
- **Educational Content**: Course slides, tutorials, workshops
- **Marketing Materials**: Product presentations, pitch decks
- **Technical Documentation**: Architecture diagrams, process flows
- **Event Programs**: Conference agendas, event schedules

## 🔧 Troubleshooting

If you encounter issues:

1. Check your YAML syntax with `--validate-only`
2. Ensure all referenced files (images, templates) exist and are accessible
3. Review the logs with `-v` for detailed error information
4. Consult the [Troubleshooting Guide](docs/troubleshooting.md)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
