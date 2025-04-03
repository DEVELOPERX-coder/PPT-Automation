"""
Utility functions for md2ppt.
"""

import os
import re
from typing import Optional, Tuple


def ensure_extension(filename: str, extension: str) -> str:
    """
    Ensure a filename has the specified extension.
    
    Args:
        filename: Original filename
        extension: Extension to ensure (including dot)
        
    Returns:
        Filename with the correct extension
    """
    base, ext = os.path.splitext(filename)
    if ext.lower() != extension.lower():
        return f"{base}{extension}"
    return filename


def is_url(text: str) -> bool:
    """
    Check if text is a URL.
    
    Args:
        text: Text to check
        
    Returns:
        True if text is a URL, False otherwise
    """
    url_pattern = re.compile(
        r'^https?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # or IP
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    return bool(url_pattern.match(text))


def is_local_file(path: str) -> bool:
    """
    Check if path points to an existing local file.
    
    Args:
        path: File path to check
        
    Returns:
        True if path is an existing local file, False otherwise
    """
    return os.path.isfile(path)


def extract_dimensions(text: str) -> Optional[Tuple[int, int]]:
    """
    Extract width and height dimensions from text.
    Example input: "width=800,height=600" or "800x600"
    
    Args:
        text: Text containing dimensions
        
    Returns:
        Tuple of (width, height) or None if no dimensions found
    """
    # Check for width=X,height=Y format
    pattern1 = re.compile(r'width=(\d+),height=(\d+)', re.IGNORECASE)
    match = pattern1.search(text)
    if match:
        return (int(match.group(1)), int(match.group(2)))
    
    # Check for WxH format
    pattern2 = re.compile(r'(\d+)x(\d+)', re.IGNORECASE)
    match = pattern2.search(text)
    if match:
        return (int(match.group(1)), int(match.group(2)))
    
    return None


def parse_color(color_str: str) -> Optional[Tuple[int, int, int]]:
    """
    Parse color string in various formats.
    Supports: 
    - Named colors (red, blue, green, etc.)
    - Hex colors (#FF0000, #00FF00, etc.)
    - RGB colors (rgb(255,0,0), rgb(0,255,0), etc.)
    
    Args:
        color_str: Color string
        
    Returns:
        Tuple of (R, G, B) or None if invalid format
    """
    # Named colors dictionary
    named_colors = {
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'yellow': (255, 255, 0),
        'cyan': (0, 255, 255),
        'magenta': (255, 0, 255),
        'gray': (128, 128, 128),
        'grey': (128, 128, 128),
        'lightgray': (211, 211, 211),
        'lightgrey': (211, 211, 211),
        'darkgray': (64, 64, 64),
        'darkgrey': (64, 64, 64),
    }
    
    # Check for named color
    color_str = color_str.lower().strip()
    if color_str in named_colors:
        return named_colors[color_str]
    
    # Check for hex color
    hex_pattern = re.compile(r'^#?([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$', re.IGNORECASE)
    match = hex_pattern.match(color_str)
    if match:
        return (int(match.group(1), 16), int(match.group(2), 16), int(match.group(3), 16))
    
    # Check for RGB color
    rgb_pattern = re.compile(r'rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)', re.IGNORECASE)
    match = rgb_pattern.match(color_str)
    if match:
        return (int(match.group(1)), int(match.group(2)), int(match.group(3)))
    
    return None


def get_animation_properties(animation_str: str) -> dict:
    """
    Parse animation properties from string.
    Example input: "fade,duration=1.5,delay=0.5"
    
    Args:
        animation_str: Animation string
        
    Returns:
        Dictionary of animation properties
    """
    props = {}
    parts = animation_str.split(',')
    
    # First part is animation type
    if parts and parts[0].strip():
        props['type'] = parts[0].strip()
    
    # Process additional properties
    for part in parts[1:]:
        if '=' in part:
            key, value = part.split('=', 1)
            key = key.strip()
            value = value.strip()
            
            # Try to convert numeric values
            try:
                if '.' in value:
                    props[key] = float(value)
                else:
                    props[key] = int(value)
            except ValueError:
                props[key] = value
    
    return props