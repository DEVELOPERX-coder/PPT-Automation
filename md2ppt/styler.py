"""
Styling module for md2ppt.
"""

import os
import json
from typing import Dict, Any, Optional

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor


class PresentationStyler:
    """
    Styler for PowerPoint presentations.
    """
    
    DEFAULT_THEME = {
        "name": "default",
        "slide_width": 9,
        "slide_height": 6.75,
        "colors": {
            "background": [255, 255, 255],
            "title": [0, 0, 0],
            "heading": [0, 0, 0],
            "body": [0, 0, 0],
            "accent1": [68, 114, 196],
            "accent2": [237, 125, 49],
            "accent3": [165, 165, 165]
        },
        "fonts": {
            "title": {
                "name": "Calibri",
                "size": 44,
                "bold": True,
                "italic": False
            },
            "heading2": {
                "name": "Calibri",
                "size": 32,
                "bold": True,
                "italic": False
            },
            "heading3": {
                "name": "Calibri",
                "size": 28,
                "bold": True,
                "italic": False
            },
            "heading4": {
                "name": "Calibri",
                "size": 24,
                "bold": True,
                "italic": False
            },
            "body": {
                "name": "Calibri",
                "size": 18,
                "bold": False,
                "italic": False
            },
            "code": {
                "name": "Courier New",
                "size": 14,
                "bold": False,
                "italic": False
            }
        },
        "slide_layouts": {
            "title": 0,
            "title_and_content": 1,
            "section": 2,
            "two_content": 3,
            "title_only": 5,
            "blank": 6
        },
        "default_transitions": {
            "type": "fade",
            "duration": 1.0
        },
        "default_animations": {
            "type": "fade",
            "duration": 0.5,
            "delay": 0.2
        }
    }
    
    def __init__(self, theme_name: str = "default", config_file: Optional[str] = None):
        """
        Initialize the presentation styler.
        
        Args:
            theme_name: Name of the theme to use
            config_file: Path to a JSON configuration file (optional)
        """
        self.theme = self.DEFAULT_THEME.copy()
        
        # Load custom theme if provided
        if config_file and os.path.exists(config_file):
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    custom_theme = json.load(f)
                    self.theme.update(custom_theme)
            except Exception as e:
                print(f"Error loading theme file: {e}")
    
    def create_presentation(self) -> Presentation:
        """
        Create a new presentation with the current theme.
        
        Returns:
            A new PowerPoint presentation
        """
        prs = Presentation()
        
        # Set slide dimensions
        prs.slide_width = Inches(self.theme["slide_width"])
        prs.slide_height = Inches(self.theme["slide_height"])
        
        return prs
    
    def get_slide_layout(self, presentation: Presentation, properties: Dict[str, str]) -> Any:
        """
        Get the slide layout based on properties.
        
        Args:
            presentation: PowerPoint presentation
            properties: Slide properties dictionary
            
        Returns:
            PowerPoint slide layout
        """
        layout_name = properties.get('layout', 'title_and_content')
        layout_idx = self.theme["slide_layouts"].get(layout_name, 1)  # Default to title and content
        
        # Some presentations might not have all layouts
        max_layouts = len(presentation.slide_layouts) - 1
        if layout_idx > max_layouts:
            layout_idx = min(1, max_layouts)  # Fallback to title and content or first available
        
        return presentation.slide_layouts[layout_idx]
    
    def style_title(self, title_shape, properties: Dict[str, str]) -> None:
        """
        Style the title shape.
        
        Args:
            title_shape: PowerPoint title shape
            properties: Slide properties dictionary
        """
        if not title_shape:
            return
        
        # Apply font styling
        font = title_shape.text_frame.paragraphs[0].runs[0].font
        font_settings = self.theme["fonts"]["title"]
        
        font.name = font_settings["name"]
        font.size = Pt(font_settings["size"])
        font.bold = font_settings["bold"]
        font.italic = font_settings["italic"]
        
        # Apply color
        rgb = self.theme["colors"]["title"]
        font.color.rgb = RGBColor(rgb[0], rgb[1], rgb[2])
    
    def style_body_text(self, text_run) -> None:
        """
        Style body text run.
        
        Args:
            text_run: PowerPoint text run
        """
        font_settings = self.theme["fonts"]["body"]
        
        text_run.font.name = font_settings["name"]
        if not text_run.font.size:  # Only set if not already set
            text_run.font.size = Pt(font_settings["size"])
        
        # Apply color if not already set
        if not hasattr(text_run.font.color, 'rgb') or not text_run.font.color.rgb:
            rgb = self.theme["colors"]["body"]
            text_run.font.color.rgb = RGBColor(rgb[0], rgb[1], rgb[2])
    
    def style_quote(self, text_run) -> None:
        """
        Style quote text run.
        
        Args:
            text_run: PowerPoint text run
        """
        # Use body text styling as base
        self.style_body_text(text_run)
        
        # Add quote-specific styling
        text_run.font.italic = True
        
        # Use accent color
        rgb = self.theme["colors"]["accent3"]
        text_run.font.color.rgb = RGBColor(rgb[0], rgb[1], rgb[2])
    
    def get_heading_size(self, level: int) -> Pt:
        """
        Get font size for a heading level.
        
        Args:
            level: Heading level (2-6)
            
        Returns:
            Font size as Pt
        """
        heading_key = f"heading{level}"
        if heading_key in self.theme["fonts"]:
            font_size = self.theme["fonts"][heading_key]["size"]
        else:
            # Fallback calculation
            base_size = self.theme["fonts"]["heading2"]["size"]
            font_size = base_size - (level - 2) * 4
            
        # Ensure the font size is valid
        if isinstance(font_size, int) and font_size > 0:
            return Pt(font_size)
        else:
            # Default to 24pt if there's any issue
            return Pt(24)
    
    def get_body_font_size(self) -> Pt:
        """
        Get body text font size.
        
        Returns:
            Font size as Pt
        """
        font_size = self.theme["fonts"]["body"]["size"]
        # Make sure we're returning a valid Pt value (100-400000)
        # Pt value is 100 times the point size in PowerPoint
        if isinstance(font_size, int) and font_size > 0:
            # Converting to Pt here ensures it's properly formatted for PowerPoint
            return Pt(font_size)
        else:
            # Default to 18pt if there's any issue
            return Pt(18)
    
    def apply_background(self, slide, background_color=None):
        """
        Apply background color to a slide.
        
        Args:
            slide: PowerPoint slide
            background_color: RGB color tuple or None for theme default
        """
        if background_color is None:
            background_color = self.theme["colors"]["background"]
        
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = RGBColor(background_color[0], background_color[1], background_color[2])