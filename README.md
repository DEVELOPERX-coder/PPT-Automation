# md2ppt: Markdown to PowerPoint Converter

A powerful Python package that converts Markdown files into feature-rich Microsoft PowerPoint presentations.

## Features

- Convert Markdown files to PowerPoint presentations
- Support for advanced PowerPoint features:
  - Animations
  - Transitions
  - Styling (fonts, colors, formatting)
  - Layout control
  - Size adjustments
  - And more!
- Customizable themes
- Command-line interface
- Extensive markdown support

## Installation

```bash
# Install from PyPI
pip install md2ppt

# Install from source
git clone https://github.com/yourusername/md2ppt.git
cd md2ppt
pip install -e .
```

## Quick Start

Convert a markdown file to PowerPoint:

```bash
md2ppt example.md
```

This will create `example.pptx` in the same directory.

With a custom theme:

```bash
md2ppt example.md --theme=professional --config=custom_theme.json
```

## Markdown Syntax

md2ppt supports standard Markdown syntax with special annotations for PowerPoint features.

### Slides and Headers

Each level 1 heading (`#`) creates a new slide with the heading text as the title:

```markdown
# Slide Title

Content goes here

# Next Slide Title

More content
```

Level 2+ headings (`##`, `###`, etc.) create headings within a slide.

### Text Formatting

Standard Markdown formatting is supported:

- **Bold text**: `**bold**`
- _Italic text_: `*italic*`
- ~~Strikethrough~~: `~~strikethrough~~`
- `Code`: `` `code` ``
- [Links](https://example.com): `[Links](https://example.com)`

### Lists

Both ordered and unordered lists work as expected:

```markdown
- Unordered item 1
- Unordered item 2
  - Nested item

1. Ordered item 1
2. Ordered item 2
```

### Images

Include images in your slides:

```markdown
![Alt text](path/to/image.jpg)
```

### Code Blocks

Code blocks are styled with syntax highlighting:

````markdown
```python
def hello_world():
    print("Hello, world!")
```
````

### Tables

Tables are supported:

```markdown
| Header 1 | Header 2 |
| -------- | -------- |
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |
```

### Block Quotes

```markdown
> This is a blockquote
> It can span multiple lines
```

## PowerPoint Features

### Slide Properties

Control slide properties with HTML comments:

```markdown
<!-- slide: transition=fade, background_color=lightblue -->

# Slide with Custom Properties
```

### Global Properties

Set global presentation properties at the beginning of the file:

```markdown
<!-- theme: professional -->
<!-- transition: fade -->

# First Slide
```

### Animations

Add animations to slide elements:

```markdown
- This item will fade in <!-- animation: fade, duration=0.5, delay=0.2 -->
- This item will fly in from the left <!-- animation: fly_in, direction=left -->
```

### Supported Animations

- `fade`: Fade in/out
- `appear`: Appear
- `fly_in`: Fly in effect
- `float_in`: Float in effect
- `split`: Split effect
- `wipe`: Wipe effect
- `zoom`: Zoom effect
- `grow`: Grow effect
- `spin`: Spin effect
- `swivel`: Swivel effect
- `pulse`: Pulse effect
- `bounce`: Bounce effect

### Supported Transitions

- `fade`: Fade transition
- `push`: Push transition
- `wipe`: Wipe transition
- `split`: Split transition
- `cut`: Cut transition
- `random`: Random transition
- `shape`: Shape transition
- `blinds`: Blinds transition
- `checker`: Checker transition
- `comb`: Comb transition
- `dissolve`: Dissolve transition
- `zoom`: Zoom transition

## Customization

### Theme Files

Create custom themes by defining a JSON file:

```json
{
  "name": "professional",
  "slide_width": 10,
  "slide_height": 7.5,
  "colors": {
    "background": [255, 255, 255],
    "title": [0, 51, 102],
    "heading": [0, 102, 153],
    "body": [0, 0, 0]
  },
  "fonts": {
    "title": {
      "name": "Arial",
      "size": 44,
      "bold": true
    },
    "body": {
      "name": "Arial",
      "size": 20
    }
  }
}
```

### Command Line Options

```
Usage:
    md2ppt <input_file> [<output_file>] [--theme=<theme>] [--config=<config_file>]

Options:
    -h --help               Show this help
    --theme=<theme>         Specify a theme [default: default]
    --config=<config_file>  Specify a configuration file
```

## Examples

Check the `examples/` directory for example Markdown files and themes.

## Markdown to PowerPoint Mapping

| Markdown Element  | PowerPoint Element      |
| ----------------- | ----------------------- |
| # Heading 1       | New slide with title    |
| ## Heading 2      | Heading (large)         |
| ### Heading 3     | Heading (medium)        |
| #### Heading 4    | Heading (small)         |
| Paragraph         | Text box                |
| \* Unordered list | Bullet list             |
| 1. Ordered list   | Numbered list           |
| ![Image](src)     | Image                   |
| > Blockquote      | Quote box with styling  |
| `code`            | Code block with styling |
| \|table\|         | Table                   |
| [Link](url)       | Hyperlink               |
| **Bold**          | Bold text               |
| _Italic_          | Italic text             |
| ~~Strikethrough~~ | Strikethrough text      |
| `Inline code`     | Monospace text          |
| HTML comments     | Slide properties        |

## Development

### Project Structure

```
md2ppt/
│
├── md2ppt/
│   ├── __init__.py
│   ├── main.py          # Command-line entry point
│   ├── parser.py        # Markdown parsing logic
│   ├── ppt_generator.py # PowerPoint generation
│   ├── styler.py        # Presentation styling
│   ├── utils.py         # Utility functions
│   └── advanced_features.py # Advanced PowerPoint features
│
├── tests/               # Unit tests
├── examples/            # Example files
├── README.md            # Project documentation
├── requirements.txt     # Dependencies
└── setup.py             # Installation script
```

### Running Tests

```bash
python -m unittest discover -s tests
```

## Requirements

- Python 3.6+
- python-pptx
- mistune
- docopt
- requests

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

This project uses:

- [python-pptx](https://python-pptx.readthedocs.io/) for PowerPoint file manipulation
- [mistune](https://mistune.readthedocs.io/) for Markdown parsing
- [docopt](http://docopt.org/) for command-line interface
