"""
Template Parser Module

This module handles parsing of custom-formatted input files for the PowerPoint Generator.
"""

import os
import re
import yaml
import json

class TemplateParser:
    """
    A class for parsing custom template files for PowerPoint generation.
    
    This parser supports YAML and simple markup formats for defining presentations.
    """
    
    def __init__(self):
        """Initialize the TemplateParser."""
        self.variables = {}
    
    def parse_file(self, file_path):
        """
        Parse a template file into a structured format for the PowerPoint generator.
        
        Args:
            file_path (str): Path to the template file.
            
        Returns:
            dict: Structured presentation data.
        """
        file_ext = os.path.splitext(file_path)[1].lower()
        
        if file_ext == '.yaml' or file_ext == '.yml':
            return self._parse_yaml(file_path)
        elif file_ext == '.json':
            return self._parse_json(file_path)
        elif file_ext == '.txt':
            return self._parse_text(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_ext}")
    
    def _parse_yaml(self, file_path):
        """
        Parse a YAML template file.
        
        Args:
            file_path (str): Path to the YAML file.
            
        Returns:
            dict: Structured presentation data.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            # Process variables if present
            if 'variables' in data:
                self.variables = data['variables']
                # Apply variables throughout the document
                data = self._apply_variables(data)
            
            return data
        except Exception as e:
            raise ValueError(f"Error parsing YAML file: {e}")
    
    def _parse_json(self, file_path):
        """
        Parse a JSON template file.
        
        Args:
            file_path (str): Path to the JSON file.
            
        Returns:
            dict: Structured presentation data.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Process variables if present
            if 'variables' in data:
                self.variables = data['variables']
                # Apply variables throughout the document
                data = self._apply_variables(data)
            
            return data
        except Exception as e:
            raise ValueError(f"Error parsing JSON file: {e}")
    
    def _parse_text(self, file_path):
        """
        Parse a simple text-based template file.
        
        Format:
        # Slide Title
        ## Slide content
        
        - Bullet 1
        - Bullet 2
        
        !image: path/to/image.jpg
        
        ---
        
        Args:
            file_path (str): Path to the text file.
            
        Returns:
            dict: Structured presentation data.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Split into slides based on "---" separator
            slide_contents = content.split('---')
            
            # Process variables first
            variables_section = re.search(r'@variables\s+(.*?)(?=@|\Z)', content, re.DOTALL)
            if variables_section:
                vars_text = variables_section.group(1).strip()
                lines = vars_text.split('\n')
                for line in lines:
                    if ':' in line:
                        key, value = line.split(':', 1)
                        self.variables[key.strip()] = value.strip()
            
            # Create structured presentation data
            presentation_data = {
                'settings': {},
                'slides': []
            }
            
            # Process each slide
            for slide_content in slide_contents:
                if not slide_content.strip():
                    continue
                
                slide_data = self._parse_slide_content(slide_content)
                if slide_data:
                    presentation_data['slides'].append(slide_data)
            
            # Apply variables
            presentation_data = self._apply_variables(presentation_data)
            
            return presentation_data
            
        except Exception as e:
            raise ValueError(f"Error parsing text file: {e}")
    
    def _parse_slide_content(self, content):
        """
        Parse the content of a single slide from text format.
        
        Args:
            content (str): Text content for a single slide.
            
        Returns:
            dict: Structured slide data.
        """
        lines = content.strip().split('\n')
        slide_data = {}
        
        # Determine slide type and title
        title_match = re.search(r'^#+\s+(.+)$', lines[0])
        if title_match:
            slide_data['title'] = title_match.group(1).strip()
            # Determine slide type based on the line starting with '#'
            if lines[0].startswith('# '):
                slide_data['type'] = 'title_slide'
            elif lines[0].startswith('## '):
                slide_data['type'] = 'section'
            else:
                slide_data['type'] = 'title_and_content'
        else:
            slide_data['type'] = 'blank'
        
        # Process content
        content_lines = []
        bullet_points = []
        images = []
        
        in_bullet_list = False
        
        for i, line in enumerate(lines[1:], 1):
            line = line.rstrip()
            
            # Skip empty lines
            if not line:
                continue
            
            # Check for subtitle marker (for title slides)
            if line.startswith('*') and slide_data['type'] == 'title_slide':
                slide_data['subtitle'] = line[1:].strip()
                continue
            
            # Check for image marker
            if line.startswith('!image:'):
                image_path = line[7:].strip()
                images.append({'path': image_path})
                continue
            
            # Check for bullet points
            if line.strip().startswith('- '):
                if not in_bullet_list:
                    in_bullet_list = True
                    bullet_points = []
                bullet_points.append(line.strip()[2:])
                continue
            elif in_bullet_list:
                in_bullet_list = False
            
            # Regular content
            if not line.startswith('#'):  # Ignore heading lines after the first
                content_lines.append(line)
        
        # Set content based on what we found
        if bullet_points:
            slide_data['content'] = bullet_points
        elif content_lines:
            slide_data['content'] = '\n'.join(content_lines)
        
        # Add images if found
        if images:
            if len(images) == 1:
                slide_data['image'] = images[0]
            else:
                slide_data['images'] = images
        
        return slide_data
    
    def _apply_variables(self, data):
        """
        Replace variable placeholders in the data with their values.
        
        Args:
            data: The data structure to process.
            
        Returns:
            The processed data structure with variables replaced.
        """
        if isinstance(data, dict):
            return {k: self._apply_variables(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [self._apply_variables(item) for item in data]
        elif isinstance(data, str):
            # Replace {{variable}} with its value
            for var_name, var_value in self.variables.items():
                placeholder = '{{' + var_name + '}}'
                data = data.replace(placeholder, str(var_value))
            return data
        else:
            return data

def main():
    """
    Example usage of the TemplateParser class.
    """
    parser = TemplateParser()
    
    # Parse a YAML file
    try:
        presentation_data = parser.parse_file('examples/simple_presentation.yaml')
        print("Successfully parsed YAML presentation template.")
        print(f"Number of slides: {len(presentation_data.get('slides', []))}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Parse a text file
    try:
        presentation_data = parser.parse_file('examples/simple_presentation.txt')
        print("Successfully parsed text presentation template.")
        print(f"Number of slides: {len(presentation_data.get('slides', []))}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()