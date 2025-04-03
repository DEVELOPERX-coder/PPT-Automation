#!/usr/bin/env python3
"""
PowerPoint Animation Handler (win32com Extension)

This module extends the Markdown to PowerPoint converter with animation capabilities
using the win32com library to interact directly with PowerPoint.
"""

import os
import time
import json
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('pptx_animation')

try:
    import win32com.client
    from win32com.client import constants
    ANIMATION_SUPPORTED = True
except ImportError:
    ANIMATION_SUPPORTED = False
    logger.warning("win32com not found. Animation features will not be available.")
    logger.warning("To install, run: pip install pywin32")

# PowerPoint animation effect mappings
# These map our Markdown animation names to PowerPoint COM constants
ENTRANCE_EFFECTS = {
    "appear": 0,                  # msoAnimEffectAppear
    "fade": 1,                    # msoAnimEffectFade
    "fly_in": 4,                  # msoAnimEffectFly
    "float": 5,                   # msoAnimEffectFloat
    "split": 6,                   # msoAnimEffectSplit
    "wipe": 7,                    # msoAnimEffectWipe
    "zoom": 9,                    # msoAnimEffectZoom
    "random": 10,                 # msoAnimEffectRandom
    "wheel": 11,                  # msoAnimEffectWheel
    "swivel": 12,                 # msoAnimEffectSwivel 
    "bounce": 13,                 # msoAnimEffectBounce
    "grow": 14,                   # msoAnimEffectGrowShrink
    "shape": 16,                  # msoAnimEffectShape
    "blinds": 25,                 # msoAnimEffectBlinds
    "box": 26,                    # msoAnimEffectBox
    "checkerboard": 27,           # msoAnimEffectCheckerboard
    "circle": 28,                 # msoAnimEffectCircle
    "crawl": 30,                  # msoAnimEffectCrawl
    "diamond": 31,                # msoAnimEffectDiamond
    "dissolve": 32,               # msoAnimEffectDissolve
    "peek": 34,                   # msoAnimEffectPeek
    "plus": 35,                   # msoAnimEffectPlus
    "random_bars": 36,            # msoAnimEffectRandomBars
    "spiral": 37,                 # msoAnimEffectSpiral
    "stretch": 38,                # msoAnimEffectStretch
    "strips": 39,                 # msoAnimEffectStrips
    "wedge": 40,                  # msoAnimEffectWedge
    "wheel_reverse": 41,          # msoAnimEffectWheel
    "curve_up": 43,               # msoAnimEffectCurveUp
    "curve_down": 44,             # msoAnimEffectCurveDown
    "drape": 45,                  # msoAnimEffectDrape
    "curtains": 46,               # msoAnimEffectCurtains
    "flash": 47,                  # msoAnimEffectFlash
    "lines": 49,                  # msoAnimEffectLines
}

EMPHASIS_EFFECTS = {
    "pulse": 15,                  # msoAnimEffectPulse
    "color": 18,                  # msoAnimEffectColor
    "brush": 19,                  # msoAnimEffectBrush 
    "teeter": 20,                 # msoAnimEffectTeeter
    "wave": 21,                   # msoAnimEffectWave
    "spin": 22,                   # msoAnimEffectSpin
    "grow_with_color": 23,        # msoAnimEffectGrowWithColor
    "desaturate": 24,             # msoAnimEffectDesaturate
    "darken": 50,                 # msoAnimEffectDarken
    "lighten": 51,                # msoAnimEffectLighten
    "transparency": 52,           # msoAnimEffectTransparency
    "object_color": 53,           # msoAnimEffectObjectColor
    "complementary_color": 54,    # msoAnimEffectComplementaryColor
    "change_line_color": 55,      # msoAnimEffectChangeLineColor
    "change_fill_color": 56,      # msoAnimEffectChangeFillColor
}

EXIT_EFFECTS = {
    "fade_out": 2,                # msoAnimEffectFade (exit)
    "fly_out": 4,                 # msoAnimEffectFly (exit) 
    "float_out": 5,               # msoAnimEffectFloat (exit)
    "split_out": 6,               # msoAnimEffectSplit (exit)
    "wipe_out": 7,                # msoAnimEffectWipe (exit)
    "zoom_out": 9,                # msoAnimEffectZoom (exit)
}

DIRECTION_MAP = {
    "in": 0,                      # msoAnimDirectionIn
    "out": 1,                     # msoAnimDirectionOut
    "up": 3,                      # msoAnimDirectionUp
    "down": 4,                    # msoAnimDirectionDown
    "left": 5,                    # msoAnimDirectionLeft 
    "right": 6,                   # msoAnimDirectionRight
    "down_left": 7,               # msoAnimDirectionDownLeft
    "up_left": 8,                 # msoAnimDirectionUpLeft
    "down_right": 9,              # msoAnimDirectionDownRight
    "up_right": 10,               # msoAnimDirectionUpRight
    "horizontal": 16,             # msoAnimDirectionHorizontal
    "vertical": 17,               # msoAnimDirectionVertical
    "across": 18,                 # msoAnimDirectionAcross
}

TRIGGER_MAP = {
    "on_click": 1,                # msoAnimTriggerOnClick
    "with_previous": 2,           # msoAnimTriggerWithPrevious
    "after_previous": 3,          # msoAnimTriggerAfterPrevious
    "on_page_click": 7,           # msoAnimTriggerOnPageClick
    "on_media_complete": 8,       # msoAnimTriggerOnMediaBookmark
    "time_absolute": 9,           # msoAnimTriggerTimeAbsolute
}

# PowerPoint slide transition mappings
SLIDE_TRANSITIONS = {
    "none": 0,                    # ppTransitionNone
    "cut": 1,                     # ppTransitionCut
    "fade": 2,                    # ppTransitionFade
    "push": 3,                    # ppTransitionPush
    "wipe": 4,                    # ppTransitionWipe
    "split": 5,                   # ppTransitionSplit
    "reveal": 6,                  # ppTransitionReveal
    "random": 7,                  # ppTransitionRandom
    "checkerboard": 8,            # ppTransitionCheckerboard
    "blinds": 9,                  # ppTransitionBlinds
    "clock": 10,                  # ppTransitionClock
    "dissolve": 11,               # ppTransitionDissolve
    "wheel": 12,                  # ppTransitionWheel
    "random_bars": 13,            # ppTransitionRandomBars
    "zoom": 15,                   # ppTransitionZoom
    "orbit": 19,                  # ppTransitionOrbit
    "fly_through": 20,            # ppTransitionFlyThrough
    "flash": 21,                  # ppTransitionFlash
    "shred": 22,                  # ppTransitionShred
    "shapes": 27,                 # ppTransitionShapes
    "switch": 29,                 # ppTransitionSwitch
    "flip": 30,                   # ppTransitionFlip
    "ripple": 31,                 # ppTransitionRipple
    "honeycomb": 32,              # ppTransitionHoneycomb
    "cube": 33,                   # ppTransitionCube
    "box": 34,                    # ppTransitionBox
    "rotate": 35,                 # ppTransitionCoverflow
    "doors": 36,                  # ppTransitionDoors
    "window": 37,                 # ppTransitionWindow
    "page_curl": 38,              # ppTransitionPageCurl
    "morph": 41,                  # ppTransitionMorph
}

class ComAnimationHandler:
    """Handles PowerPoint animations and advanced features using COM automation."""
    
    def __init__(self):
        """Initialize the animation handler."""
        self.ppt_app = None
        self.presentation = None
        self.is_connected = False
        self.element_map = {}  # Maps between our element IDs and PPT shape indices
        self.animation_data = []  # Stores animation instructions
    
    def is_supported(self):
        """Check if animation is supported on this system."""
        return ANIMATION_SUPPORTED
    
    def connect(self, pptx_path):
        """Connect to PowerPoint application and open the presentation."""
        if not ANIMATION_SUPPORTED:
            logger.error("Animation not supported. Install pywin32 first.")
            return False
        
        try:
            self.ppt_app = win32com.client.Dispatch("PowerPoint.Application")
            # Uncomment to see PowerPoint while processing (for debugging)
            # self.ppt_app.Visible = True
            
            # Convert to absolute path
            abs_path = os.path.abspath(pptx_path)
            logger.info(f"Opening presentation: {abs_path}")
            
            # Open presentation
            self.presentation = self.ppt_app.Presentations.Open(abs_path)
            self.is_connected = True
            logger.info(f"Successfully opened presentation with {self.presentation.Slides.Count} slides")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to PowerPoint: {str(e)}")
            return False
    
    def add_animation_data(self, slide_index, element_index, animation_props):
        """Store animation data for later processing."""
        self.animation_data.append({
            'slide_index': slide_index,
            'element_index': element_index,
            'props': animation_props
        })
    
    def map_effect_value(self, effect_name, effect_type='entrance'):
        """Map the effect name to PowerPoint's effect value."""
        effect_name = effect_name.lower()
        
        if effect_type == 'entrance':
            return ENTRANCE_EFFECTS.get(effect_name, 0)  # Default to "appear"
        elif effect_type == 'emphasis':
            return EMPHASIS_EFFECTS.get(effect_name, 15)  # Default to "pulse"
        elif effect_type == 'exit':
            return EXIT_EFFECTS.get(effect_name, 2)      # Default to "fade_out"
        else:
            return 0  # Default to "appear"
    
    def map_direction_value(self, direction_name):
        """Map the direction name to PowerPoint's direction value."""
        direction_name = direction_name.lower() if direction_name else 'in'
        return DIRECTION_MAP.get(direction_name, 0)  # Default to "in"
    
    def map_trigger_value(self, trigger_name):
        """Map the trigger name to PowerPoint's trigger value."""
        trigger_name = trigger_name.lower() if trigger_name else 'on_click'
        return TRIGGER_MAP.get(trigger_name, 1)  # Default to "on_click"
    
    def apply_animations(self):
        """Apply all stored animations to the presentation."""
        if not self.is_connected or not self.animation_data:
            return False
        
        logger.info(f"Applying {len(self.animation_data)} animations")
        
        for anim_info in self.animation_data:
            slide_index = anim_info['slide_index']
            element_index = anim_info['element_index']
            props = anim_info['props']
            
            if slide_index <= 0 or slide_index > self.presentation.Slides.Count:
                logger.warning(f"Slide index out of bounds: {slide_index}")
                continue
            
            try:
                slide = self.presentation.Slides(slide_index)
                
                # Check if element index is valid
                if element_index <= 0 or element_index > slide.Shapes.Count:
                    logger.warning(f"Shape index out of bounds: {element_index} on slide {slide_index}")
                    continue
                
                shape = slide.Shapes(element_index)
                
                # Get animation type and parameters
                anim_type = props.get('animation_type', 'entrance')
                anim_effect = props.get('animation', 'fade')
                anim_direction = props.get('animation_direction', 'in')
                anim_trigger = props.get('animation_trigger', 'on_click')
                anim_delay = float(props.get('animation_delay', 0))
                anim_duration = float(props.get('animation_duration', 0.5))
                
                # Map values to PowerPoint constants
                effect_value = self.map_effect_value(anim_effect, anim_type)
                direction_value = self.map_direction_value(anim_direction)
                trigger_value = self.map_trigger_value(anim_trigger)
                
                # Add the animation effect
                effect = slide.TimeLine.MainSequence.AddEffect(
                    shape,          # Shape to animate
                    effect_value,   # Animation effect
                    0,              # Animation level (0 = shape level)
                    trigger_value   # Trigger type
                )
                
                # Set timing properties
                if effect:
                    if anim_delay > 0:
                        effect.Timing.TriggerDelayTime = anim_delay
                    
                    if anim_duration > 0:
                        effect.Timing.Duration = anim_duration
                    
                    # Set direction if applicable
                    try:
                        if direction_value != 0:
                            effect.EffectParameters.Direction = direction_value
                    except:
                        logger.warning(f"Could not set direction for animation on slide {slide_index}")
                
                logger.info(f"Added {anim_type} animation '{anim_effect}' to shape {element_index} on slide {slide_index}")
            
            except Exception as e:
                logger.error(f"Error applying animation on slide {slide_index}: {str(e)}")
        
        return True
    
    def apply_slide_transitions(self, transitions_data):
        """Apply transitions to slides."""
        if not self.is_connected:
            return False
        
        logger.info(f"Applying {len(transitions_data)} slide transitions")
        
        for trans_info in transitions_data:
            slide_index = trans_info['slide_index']
            props = trans_info['props']
            
            if slide_index <= 0 or slide_index > self.presentation.Slides.Count:
                logger.warning(f"Slide index out of bounds: {slide_index}")
                continue
            
            try:
                slide = self.presentation.Slides(slide_index)
                
                # Get transition type and parameters
                trans_type = props.get('transition', 'fade')
                trans_speed = props.get('transition_speed', 'medium').lower()
                trans_duration = float(props.get('transition_duration', 1.0))
                
                # Map transition type to PowerPoint constant
                trans_value = SLIDE_TRANSITIONS.get(trans_type, 2)  # Default to "fade"
                
                # Map transition speed
                speed_value = 2  # Medium
                if trans_speed == 'fast':
                    speed_value = 1
                elif trans_speed == 'slow':
                    speed_value = 3
                
                # Apply transition
                slide.SlideShowTransition.EntryEffect = trans_value
                slide.SlideShowTransition.Speed = speed_value
                
                # Set optional duration (if PowerPoint version supports it)
                try:
                    slide.SlideShowTransition.Duration = trans_duration
                except:
                    pass
                
                # Set optional auto-advance
                if 'advance_time' in props:
                    try:
                        advance_time = float(props['advance_time'])
                        slide.SlideShowTransition.AdvanceOnTime = True
                        slide.SlideShowTransition.AdvanceTime = advance_time
                    except:
                        pass
                
                logger.info(f"Added '{trans_type}' transition to slide {slide_index}")
            
            except Exception as e:
                logger.error(f"Error applying transition on slide {slide_index}: {str(e)}")
        
        return True
    
    def apply_advanced_features(self):
        """Apply other advanced PowerPoint features not supported by python-pptx."""
        # Additional advanced features can be implemented here
        # Examples: slide transitions, audio, video settings, etc.
        return True
    
    def save_and_close(self):
        """Save and close the presentation."""
        if not self.is_connected:
            return False
        
        try:
            logger.info("Saving presentation")
            self.presentation.Save()
            self.presentation.Close()
            self.ppt_app.Quit()
            self.is_connected = False
            logger.info("Presentation saved and closed")
            return True
        except Exception as e:
            logger.error(f"Error saving presentation: {str(e)}")
            return False


def apply_animations_to_presentation(pptx_path, animation_data, transition_data=None):
    """
    Apply animations to an existing PowerPoint presentation.
    
    Args:
        pptx_path: Path to the PowerPoint file
        animation_data: List of animation instructions
        transition_data: List of transition instructions
        
    Returns:
        bool: True if successful, False otherwise
    """
    handler = ComAnimationHandler()
    
    # Check if animations are supported
    if not handler.is_supported():
        logger.error("Animations not supported on this system. Install pywin32 first.")
        return False
    
    # Connect to PowerPoint
    if not handler.connect(pptx_path):
        return False
    
    # Store animation data
    for anim in animation_data:
        handler.add_animation_data(
            anim['slide_index'],
            anim['element_index'],
            anim['props']
        )
    
    # Apply animations
    handler.apply_animations()
    
    # Apply transitions if provided
    if transition_data:
        handler.apply_slide_transitions(transition_data)
    
    # Apply any other advanced features
    handler.apply_advanced_features()
    
    # Save and close
    return handler.save_and_close()


if __name__ == "__main__":
    # Example usage as standalone script
    import argparse
    
    parser = argparse.ArgumentParser(description='Apply animations to PowerPoint presentation')
    parser.add_argument('pptx_file', help='PowerPoint file path')
    parser.add_argument('-a', '--animation-data', help='JSON file with animation data')
    parser.add_argument('-t', '--transition-data', help='JSON file with transition data')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.pptx_file):
        print(f"Error: PowerPoint file not found: {args.pptx_file}")
        exit(1)
    
    # Load animation data
    anim_data = []
    if args.animation_data and os.path.exists(args.animation_data):
        with open(args.animation_data, 'r') as f:
            anim_data = json.load(f)
    
    # Load transition data
    trans_data = []
    if args.transition_data and os.path.exists(args.transition_data):
        with open(args.transition_data, 'r') as f:
            trans_data = json.load(f)
    
    # Apply animations
    success = apply_animations_to_presentation(args.pptx_file, anim_data, trans_data)
    
    if success:
        print("Animations successfully applied!")
    else:
        print("Failed to apply animations.")