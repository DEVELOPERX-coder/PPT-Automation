"""
Utility functions for the PowerPoint Generator.

This module provides helper functions and utilities for the PowerPoint Generator.
"""

import os
import re
import logging
from PIL import Image
from pptx.util import Inches

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def get_image_dimensions(image_path):
    """
    Get the dimensions of an image file.
    
    Args:
        image_path (str): Path to the image file.
        
    Returns:
        tuple: (width, height) in inches, or None if the file doesn't exist.
    """
    try:
        if not os.path.exists(image_path):
            logger.warning(f"Image file not found: {image_path}")
            return None
        
        with Image.open(image_path) as img:
            # Get dimensions in pixels
            width_px, height_px = img.size
            
            # Convert to inches (assuming 96 DPI)
            width_in = width_px / 96
            height_in = height_px / 96
            
            return (width_in, height_in)
    except Exception as e:
        logger.error(f"Error getting image dimensions: {e}")
        return None

def calculate_aspect_ratio(width, height, max_width=None, max_height=None):
    """
    Calculate dimensions while preserving aspect ratio.
    
    Args:
        width (float): Original width.
        height (float): Original height.
        max_width (float, optional): Maximum allowed width.
        max_height (float, optional): Maximum allowed height.
        
    Returns:
        tuple: (new_width, new_height) that preserves the aspect ratio.
    """
    aspect_ratio = width / height
    
    if max_width and max_height:
        if width > max_width or height > max_height:
            width_ratio = max_width / width
            height_ratio = max_height / height
            
            # Use the smaller ratio to ensure both dimensions fit within limits
            if width_ratio < height_ratio:
                return (max_width, max_width / aspect_ratio)
            else:
                return (max_height * aspect_ratio, max_height)
    
    elif max_width and width > max_width:
        return (max_width, max_width / aspect_ratio)
    
    elif max_height and height > max_height:
        return (max_height * aspect_ratio, max_height)
    
    return (width, height)

def parse_color(color_str):
    """
    Parse a color string into an RGB tuple.
    
    Args:
        color_str (str): Color string in hex (#RRGGBB) or RGB format.
        
    Returns:
        tuple: (r, g, b) values as integers.
    """
    # Check for hex format (#RRGGBB or #RGB)
    hex_pattern = r'^#([0-9a-fA-F]{3,6})$'
    hex_match = re.match(hex_pattern, color_str)
    
    if hex_match:
        hex_value = hex_match.group(1)
        
        # Convert 3-digit hex to 6-digit
        if len(hex_value) == 3:
            hex_value = ''.join([c*2 for c in hex_value])
        
        # Convert to RGB values
        r = int(hex_value[0:2], 16)
        g = int(hex_value[2:4], 16)
        b = int(hex_value[4:6], 16)
        
        return (r, g, b)
    
    # Check for RGB format (rgb(r,g,b))
    rgb_pattern = r'rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)'
    rgb_match = re.match(rgb_pattern, color_str)
    
    if rgb_match:
        r = int(rgb_match.group(1))
        g = int(rgb_match.group(2))
        b = int(rgb_match.group(3))
        
        return (r, g, b)
    
    # Handle named colors
    named_colors = {
        'red': (255, 0, 0),
        'green': (0, 128, 0),
        'blue': (0, 0, 255),
        'yellow': (255, 255, 0),
        'purple': (128, 0, 128),
        'cyan': (0, 255, 255),
        'magenta': (255, 0, 255),
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'gray': (128, 128, 128),
        'orange': (255, 165, 0)
    }
    
    if color_str.lower() in named_colors:
        return named_colors[color_str.lower()]
    
    # Default to black if unable to parse
    logger.warning(f"Unable to parse color: {color_str}, using black")
    return (0, 0, 0)

def sanitize_filename(filename):
    """
    Sanitize a filename by removing invalid characters.
    
    Args:
        filename (str): The filename to sanitize.
        
    Returns:
        str: Sanitized filename.
    """
    # Remove invalid characters
    invalid_chars = r'[<>:"/\\|?*]'
    sanitized = re.sub(invalid_chars, '_', filename)
    
    # Ensure the filename isn't too long (Windows has a 255 character limit)
    if len(sanitized) > 240:
        base, ext = os.path.splitext(sanitized)
        sanitized = base[:240 - len(ext)] + ext
    
    return sanitized

def ensure_directory_exists(directory_path):
    """
    Ensure a directory exists, creating it if necessary.
    
    Args:
        directory_path (str): Path to the directory.
        
    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            logger.info(f"Created directory: {directory_path}")
        return True
    except Exception as e:
        logger.error(f"Error creating directory {directory_path}: {e}")
        return False