"""
PowerPoint Presentation Generator

This module contains the core functionality for generating PowerPoint presentations
from YAML configuration files.
"""

import os
import logging
import yaml
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

from src.slide_builder import SlideBuilder
from src.utils import apply_theme_settings, resolve_variables

logger = logging.getLogger(__name__)

class PresentationGenerator:
    """
    A class for generating PowerPoint presentations from YAML configuration files.
    """
    
    def __init__(self, template_path=None):
        """
        Initialize the PresentationGenerator with an optional template.
        
        Args:
            template_path (str, optional): Path to a PowerPoint template file.
        """
        if template_path and os.path.exists(template_path):
            self.prs = Presentation(template_path)
            logger.debug(f"Using template: {template_path}")
        else:
            self.prs = Presentation()
            logger.debug("Using blank presentation")
        
        self.slide_builder = SlideBuilder(self.prs)
        self.variables = {}
        self.theme_settings = {
            'title_font': 'Calibri',
            'title_font_size': 44,
            'subtitle_font': 'Calibri',
            'subtitle_font_size': 32,
            'body_font': 'Calibri',
            'body_font_size': 18,
            'background_color': (255, 255, 255),  # White
            'title_color': (0, 0, 0),  # Black
            'text_color': (0, 0, 0),  # Black
            'accent_color': (0, 112, 192)  # Blue
        }
    
    def generate_from_file(self, input_file_path, output_path):
        """
        Generate a PowerPoint presentation from a YAML configuration file.
        
        Args:
            input_file_path (str): Path to the input YAML file.
            output_path (str): Path where the PowerPoint file should be saved.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            # Read and parse the input file
            with open(input_file_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            
            # Process variables
            if 'variables' in config:
                self.variables = config['variables']
                logger.debug(f"Loaded {len(self.variables)} variables")
                
            # Apply presentation-wide settings
            if 'settings' in config:
                self._apply_presentation_settings(config['settings'])
            
            # Process slides
            slides_data = config.get('slides', [])
            for slide_idx, slide_data in enumerate(slides_data):
                logger.debug(f"Processing slide {slide_idx + 1}/{len(slides_data)}")
                
                # Resolve variables in the slide data
                slide_data = resolve_variables(slide_data, self.variables)
                
                # Create the slide
                self.slide_builder.create_slide(slide_data, self.theme_settings)
            
            # Apply presentation-wide theme
            apply_theme_settings(self.prs, self.theme_settings)
            
            # Apply transitions if specified
            if 'transitions' in config:
                self._apply_transitions(config['transitions'])
            
            # Save the presentation
            self.prs.save(output_path)
            logger.info(f"Presentation saved to {output_path}")
            return True
            
        except Exception as e:
            logger.exception(f"Error generating presentation: {e}")
            return False
    
    def _apply_presentation_settings(self, settings):
        """
        Apply presentation-wide settings.
        
        Args:
            settings (dict): Dictionary of presentation settings.
        """
        logger.debug("Applying presentation settings")
        
        # Apply theme settings
        if 'theme' in settings:
            theme = settings['theme']
            
            # Font settings
            if 'fonts' in theme:
                fonts = theme['fonts']
                if 'title' in fonts:
                    self.theme_settings['title_font'] = fonts['title'].get('name', 'Calibri')
                    self.theme_settings['title_font_size'] = fonts['title'].get('size', 44)
                
                if 'subtitle' in fonts:
                    self.theme_settings['subtitle_font'] = fonts['subtitle'].get('name', 'Calibri')
                    self.theme_settings['subtitle_font_size'] = fonts['subtitle'].get('size', 32)
                
                if 'body' in fonts:
                    self.theme_settings['body_font'] = fonts['body'].get('name', 'Calibri')
                    self.theme_settings['body_font_size'] = fonts['body'].get('size', 18)
            
            # Color settings
            if 'colors' in theme:
                colors = theme['colors']
                
                if 'background' in colors:
                    self.theme_settings['background_color'] = self._parse_color(colors['background'])
                
                if 'title' in colors:
                    self.theme_settings['title_color'] = self._parse_color(colors['title'])
                
                if 'text' in colors:
                    self.theme_settings['text_color'] = self._parse_color(colors['text'])
                
                if 'accent' in colors:
                    self.theme_settings['accent_color'] = self._parse_color(colors['accent'])
        
        # Apply any other presentation settings
        if 'properties' in settings:
            props = settings['properties']
            
            if 'title' in props:
                self.prs.core_properties.title = props['title']
            
            if 'author' in props:
                self.prs.core_properties.author = props['author']
            
            if 'subject' in props:
                self.prs.core_properties.subject = props['subject']
            
            if 'keywords' in props:
                self.prs.core_properties.keywords = props['keywords']
            
            if 'comments' in props:
                self.prs.core_properties.comments = props['comments']
            
            if 'category' in props:
                self.prs.core_properties.category = props['category']
    
    def _apply_transitions(self, transitions_config):
        """
        Apply slide transitions based on configuration.
        
        Args:
            transitions_config (dict): Transition configuration.
        """
        # Note: As of my knowledge cutoff, python-pptx doesn't fully support
        # setting transitions programmatically. This is a placeholder for
        # future implementation if the library adds support.
        logger.warning("Slide transitions are not currently supported by python-pptx")
    
    def _parse_color(self, color_value):
        """
        Parse a color value into an RGB tuple.
        
        Args:
            color_value: Color value to parse, can be a string, list, or tuple.
            
        Returns:
            tuple: RGB color values as (r, g, b) tuple.
        """
        if isinstance(color_value, (list, tuple)) and len(color_value) == 3:
            return tuple(color_value)
        
        elif isinstance(color_value, str):
            # Handle hex color
            if color_value.startswith('#'):
                hex_color = color_value.lstrip('#')
                if len(hex_color) == 3:
                    hex_color = ''.join([c+c for c in hex_color])
                return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            
            # Handle named colors
            named_colors = {
                'black': (0, 0, 0),
                'white': (255, 255, 255),
                'red': (255, 0, 0),
                'green': (0, 128, 0),
                'blue': (0, 0, 255),
                'yellow': (255, 255, 0),
                'purple': (128, 0, 128),
                'orange': (255, 165, 0),
                'gray': (128, 128, 128)
            }
            
            color_lower = color_value.lower()
            if color_lower in named_colors:
                return named_colors[color_lower]
        
        # Default to black if parsing fails
        logger.warning(f"Could not parse color value: {color_value}, using black")
        return (0, 0, 0)