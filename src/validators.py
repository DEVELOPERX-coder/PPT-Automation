"""
Validation Module

This module provides functions for validating YAML input files.
"""

import os
import yaml
import logging
import jsonschema
from jsonschema import validate

logger = logging.getLogger(__name__)

# Define the YAML schema
YAML_SCHEMA = {
    "type": "object",
    "required": ["slides"],
    "properties": {
        "variables": {
            "type": "object",
            "additionalProperties": True
        },
        "settings": {
            "type": "object",
            "properties": {
                "theme": {
                    "type": "object",
                    "properties": {
                        "fonts": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "object",
                                    "properties": {
                                        "name": {"type": "string"},
                                        "size": {"type": "number", "minimum": 1}
                                    }
                                },
                                "subtitle": {
                                    "type": "object",
                                    "properties": {
                                        "name": {"type": "string"},
                                        "size": {"type": "number", "minimum": 1}
                                    }
                                },
                                "body": {
                                    "type": "object",
                                    "properties": {
                                        "name": {"type": "string"},
                                        "size": {"type": "number", "minimum": 1}
                                    }
                                }
                            }
                        },
                        "colors": {
                            "type": "object",
                            "properties": {
                                "background": {"type": ["string", "array"]},
                                "title": {"type": ["string", "array"]},
                                "text": {"type": ["string", "array"]},
                                "accent": {"type": ["string", "array"]}
                            }
                        }
                    }
                },
                "properties": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "author": {"type": "string"},
                        "subject": {"type": "string"},
                        "keywords": {"type": "string"},
                        "comments": {"type": "string"},
                        "category": {"type": "string"}
                    }
                }
            }
        },
        "slides": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["type"],
                "properties": {
                    "type": {
                        "type": "string",
                        "enum": [
                            "title", "title_and_content", "section", "two_content",
                            "comparison", "title_only", "blank", "content_with_caption",
                            "picture_with_caption"
                        ]
                    },
                    "title": {"type": "string"},
                    "subtitle": {"type": "string"},
                    "content": {"type": ["string", "array", "object"]},
                    "left_content": {"type": ["string", "array", "object"]},
                    "right_content": {"type": ["string", "array", "object"]},
                    "background": {
                        "type": "object",
                        "properties": {
                            "color": {"type": ["string", "array"]},
                            "image": {"type": "string"}
                        }
                    },
                    "elements": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "required": ["type"],
                            "properties": {
                                "type": {
                                    "type": "string",
                                    "enum": [
                                        "text_box", "shape", "image", "table",
                                        "chart", "code"
                                    ]
                                },
                                "left": {"type": "number", "minimum": 0},
                                "top": {"type": "number", "minimum": 0},
                                "width": {"type": "number", "minimum": 0},
                                "height": {"type": "number", "minimum": 0},
                                # Additional properties will be validated by element handlers
                                "text": {"type": "string"},
                                "font": {"type": "string"},
                                "size": {"type": "number", "minimum": 1},
                                "color": {"type": ["string", "array"]},
                                "bold": {"type": "boolean"},
                                "italic": {"type": "boolean"},
                                "underline": {"type": "boolean"},
                                "align": {"type": "string"},
                                "shape_type": {"type": "string"},
                                "fill_color": {"type": ["string", "array"]},
                                "line_color": {"type": ["string", "array"]},
                                "line_width": {"type": "number", "minimum": 0},
                                "path": {"type": "string"},
                                "data": {"type": ["array", "object"]},
                                "code": {"type": "string"},
                                "background_color": {"type": ["string", "array"]}
                            }
                        }
                    },
                    "animations": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "target": {"type": "string"},
                                "type": {"type": "string"},
                                "effect": {"type": "string"},
                                "start": {"type": "string"},
                                "duration": {"type": "number"},
                                "delay": {"type": "number"}
                            }
                        }
                    }
                }
            }
        },
        "transitions": {
            "type": "object",
            "properties": {
                "default": {"type": "string"},
                "slides": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "index": {"type": "number"},
                            "type": {"type": "string"},
                            "duration": {"type": "number"}
                        }
                    }
                }
            }
        }
    }
}

def validate_yaml_file(file_path):
    """
    Validate a YAML file against the schema.
    
    Args:
        file_path (str): Path to the YAML file.
        
    Returns:
        dict: A dictionary with 'valid' (bool) and 'errors' (list) keys.
    """
    if not os.path.exists(file_path):
        return {'valid': False, 'errors': [f"File not found: {file_path}"]}
    
    try:
        # Load YAML file
        with open(file_path, 'r', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
        
        # Validate against schema
        validate(instance=yaml_data, schema=YAML_SCHEMA)
        
        # Perform additional validation
        extra_validation = validate_additional_constraints(yaml_data)
        if extra_validation['errors']:
            return extra_validation
        
        return {'valid': True, 'errors': []}
    
    except yaml.YAMLError as e:
        return {'valid': False, 'errors': [f"YAML parsing error: {str(e)}"]}
    
    except jsonschema.exceptions.ValidationError as e:
        return {'valid': False, 'errors': [f"Schema validation error: {e.message}"]}
    
    except Exception as e:
        return {'valid': False, 'errors': [f"Unexpected error: {str(e)}"]}

def validate_additional_constraints(yaml_data):
    """
    Perform additional validation beyond the JSON schema.
    
    Args:
        yaml_data (dict): The parsed YAML data.
        
    Returns:
        dict: A dictionary with 'valid' (bool) and 'errors' (list) keys.
    """
    errors = []
    
    # Check for image paths
    for slide in yaml_data.get('slides', []):
        # Check background image path
        if 'background' in slide and 'image' in slide['background']:
            img_path = slide['background']['image']
            if not os.path.exists(img_path):
                errors.append(f"Background image not found: {img_path}")
        
        # Check image elements
        for element in slide.get('elements', []):
            if element.get('type') == 'image' and 'path' in element:
                img_path = element['path']
                if not os.path.exists(img_path):
                    errors.append(f"Image not found: {img_path}")
    
    # Additional slide-specific validation
    for i, slide in enumerate(yaml_data.get('slides', [])):
        slide_type = slide.get('type', '')
        
        # Title slides should have a title
        if slide_type == 'title' and 'title' not in slide:
            errors.append(f"Slide {i+1}: Title slide should have a title")
        
        # Title and content slides should have title and content
        if slide_type == 'title_and_content':
            if 'title' not in slide:
                errors.append(f"Slide {i+1}: Title and content slide should have a title")
            if 'content' not in slide:
                errors.append(f"Slide {i+1}: Title and content slide should have content")
        
        # Two content slides should have title and at least one content section
        if slide_type == 'two_content':
            if 'title' not in slide:
                errors.append(f"Slide {i+1}: Two content slide should have a title")
            if 'left_content' not in slide and 'right_content' not in slide:
                errors.append(f"Slide {i+1}: Two content slide should have at least one content section")
    
    return {'valid': len(errors) == 0, 'errors': errors}