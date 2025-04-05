#!/usr/bin/env python3
"""
PowerPoint Presentation Generator

This script automates the creation of PowerPoint presentations from
YAML configuration files with comprehensive customization options.
"""

import os
import sys
import argparse
import logging
from datetime import datetime

# Import project modules
from src.ppt_generator import PresentationGenerator
from src.validators import validate_yaml_file

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def parse_args():
    """
    Parse command line arguments.
    
    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description='Generate PowerPoint presentations from YAML configuration files.'
    )
    
    parser.add_argument(
        'input_file',
        help='Path to the input YAML file'
    )
    
    parser.add_argument(
        '-o', '--output',
        help='Path to save the generated PowerPoint file'
    )
    
    parser.add_argument(
        '-t', '--template',
        help='Path to a PowerPoint template file to use as a base'
    )
    
    parser.add_argument(
        '--validate-only',
        action='store_true',
        help='Only validate the YAML file without generating the presentation'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    
    return parser.parse_args()

def main():
    """
    Main function to run the PowerPoint generation process.
    """
    # Parse command line arguments
    args = parse_args()
    
    # Set logging level based on verbosity
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Validate input file
    if not os.path.exists(args.input_file):
        logger.error(f"Input file not found: {args.input_file}")
        sys.exit(1)
    
    # Determine output file path if not specified
    if not args.output:
        input_base = os.path.splitext(os.path.basename(args.input_file))[0]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        args.output = f"{input_base}_{timestamp}.pptx"
    
    # Ensure output directory exists
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        logger.debug(f"Created output directory: {output_dir}")
    
    try:
        # Validate the YAML file
        logger.info(f"Validating YAML file: {args.input_file}")
        validation_result = validate_yaml_file(args.input_file)
        
        if not validation_result['valid']:
            logger.error(f"YAML validation failed: {validation_result['errors']}")
            sys.exit(1)
        
        logger.info("YAML validation successful")
        
        # If only validation is requested, exit successfully
        if args.validate_only:
            logger.info("Validation complete. Exiting as requested.")
            return 0
        
        # Create PowerPoint generator with optional template
        generator = PresentationGenerator(template_path=args.template)
        
        # Generate the presentation
        logger.info(f"Generating PowerPoint presentation: {args.output}")
        success = generator.generate_from_file(args.input_file, args.output)
        
        if success:
            logger.info(f"Successfully generated presentation: {args.output}")
            return 0
        else:
            logger.error("Failed to generate presentation")
            return 1
            
    except Exception as e:
        logger.exception(f"Error during presentation generation: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())