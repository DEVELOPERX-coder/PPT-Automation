#!/usr/bin/env python3
"""
md2ppt - Convert Markdown to PowerPoint

Usage:
    md2ppt <input_file> [<output_file>] [--theme=<theme>] [--config=<config_file>]

Options:
    -h --help               Show this help
    --theme=<theme>         Specify a theme [default: default]
    --config=<config_file>  Specify a configuration file
"""

import os
import sys
from docopt import docopt

from .parser import MarkdownParser
from .ppt_generator import PowerPointGenerator
from .styler import PresentationStyler
from .utils import ensure_extension


def main():
    """Main entry point for the application"""
    args = docopt(__doc__)
    
    input_file = args['<input_file>']
    output_file = args['<output_file>']
    theme = args['--theme']
    config_file = args['--config']
    
    # Validate input file
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist")
        sys.exit(1)
    
    # Set default output file if not provided
    if not output_file:
        base_name = os.path.splitext(input_file)[0]
        output_file = ensure_extension(base_name, '.pptx')
    
    # Parse markdown file
    parser = MarkdownParser()
    elements = parser.parse(input_file)
    
    # Create styler
    styler = PresentationStyler(theme, config_file)
    
    # Generate PowerPoint
    generator = PowerPointGenerator(styler)
    presentation = generator.generate(elements)
    
    # Save presentation
    presentation.save(output_file)
    print(f"Presentation saved as '{output_file}'")


if __name__ == '__main__':
    main()