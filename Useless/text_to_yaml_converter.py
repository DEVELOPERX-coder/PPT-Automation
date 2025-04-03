import re
import yaml
import argparse
from pathlib import Path


class PPTSpecificationParser:
    """Parser to convert detailed text specifications to YAML format for PPT automation"""
    
    def __init__(self):
        self.current_slide = None
        self.slides = []
        self.slide_size = {'width': 13.33, 'height': 7.5}  # 16:9 ratio
        self.default_background = '#1A1A1A'  # Dark charcoal
        
    def parse_file(self, file_path):
        """Parse a text specification file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return self.parse_text(content)
    
    def parse_text(self, text):
        """Parse text specification content"""
        # Split into lines and process
        lines = text.split('\n')
        i = 0
        
        # Process presentation setup if present
        if 'PRESENTATION SETUP' in text:
            i = self._process_presentation_setup(lines, i)
        
        # Process slides
        while i < len(lines):
            if lines[i].strip().startswith('SLIDE '):
                i = self._process_slide(lines, i)
            else:
                i += 1
        
        # Return the complete specification
        return {
            'slide_size': self.slide_size,
            'slides': self.slides
        }
    
    def _process_presentation_setup(self, lines, start_idx):
        """Process presentation setup section"""
        i = start_idx
        
        while i < len(lines) and not lines[i].strip().startswith('SLIDE '):
            line = lines[i].strip()
            
            # Check for slide size
            if 'Slide Size:' in line and 'Widescreen' in line:
                # Already set to 16:9
                pass
            
            # Check for custom theme setup
            if 'Set background to Dark charcoal' in line:
                # Extract color code if available
                color_match = re.search(r'#([0-9A-Fa-f]{6})', line)
                if color_match:
                    self.default_background = f'#{color_match.group(1)}'
            
            i += 1
        
        return i
    
    def _process_slide(self, lines, start_idx):
        """Process a single slide specification"""
        i = start_idx
        line = lines[i].strip()
        
        # Extract slide number and title
        slide_match = re.match(r'SLIDE (\d+):(.*)', line)
        if slide_match:
            slide_num = int(slide_match.group(1))
            slide_title = slide_match.group(2).strip()
        else:
            slide_match = re.match(r'SLIDE (\d+): (.*)', line)
            if slide_match:
                slide_num = int(slide_match.group(1))
                slide_title = slide_match.group(2).strip()
            else:
                slide_parts = line.split(':')
                if len(slide_parts) > 1:
                    slide_title = slide_parts[1].strip()
                else:
                    slide_title = ""
                slide_num = len(self.slides) + 1
        
        # Create new slide
        self.current_slide = {
            'layout': 'blank',
            'background': {'color': self.default_background},
            'elements': [],
            'animations': []
        }
        
        # Process slide content
        i += 1
        section = None
        
        while i < len(lines):
            line = lines[i].strip()
            
            # Check if we've reached the next slide
            if line.startswith('SLIDE '):
                break
            
            # Skip empty lines
            if not line:
                i += 1
                continue
            
            # Check for section headers
            if line.endswith(':') and not line.startswith('•') and not line.startswith('-'):
                section = line[:-1].lower()
                i += 1
                continue
            
            # Process background setup
            if ('background' in line.lower() and 'dark charcoal' in line.lower()) or ('Apply dark charcoal background' in line):
                # Extract color code if available
                color_match = re.search(r'#([0-9A-Fa-f]{6})', line)
                if color_match:
                    self.current_slide['background']['color'] = f'#{color_match.group(1)}'
                i += 1
                continue
            
            # Process title
            if section == 'title text' or ('Title:' in line and i < start_idx + 10):
                # Look for multiple lines defining the title properties
                title_data = {'text': '', 'left': 1.0, 'top': 0.8, 'width': 10.0, 'height': 1.0, 
                             'font_name': 'Segoe UI Light', 'font_size': 40, 'bold': True, 'color': '#00FFFF'}
                
                while i < len(lines) and not lines[i].startswith('SLIDE ') and not ':' in lines[i].strip()[-1:]:
                    line = lines[i].strip()
                    
                    # Extract title text
                    if 'Text:' in line:
                        text_match = re.search(r'Text: "(.*)"', line)
                        if text_match:
                            title_data['text'] = text_match.group(1)
                        else:
                            # Try without quotes
                            text_match = re.search(r'Text: (.*)', line)
                            if text_match:
                                title_data['text'] = text_match.group(1)
                    
                    # Extract font info
                    if 'Font:' in line:
                        font_match = re.search(r'Font: ([^,]+), (\d+)pt', line)
                        if font_match:
                            title_data['font_name'] = font_match.group(1)
                            title_data['font_size'] = int(font_match.group(2))
                            if 'Bold' in line:
                                title_data['bold'] = True
                    
                    # Extract position
                    if 'Position:' in line and 'from top' in line:
                        pos_match = re.search(r'(\d+\.?\d*)"? from top', line)
                        if pos_match:
                            title_data['top'] = float(pos_match.group(1))
                    
                    # Extract color
                    color_match = re.search(r'#([0-9A-Fa-f]{6})', line)
                    if color_match:
                        title_data['color'] = f'#{color_match.group(1)}'
                    
                    # Check for gradient
                    if 'gradient' in line.lower():
                        title_data['gradient'] = {
                            'color1': '#00FFFF',  # Cyan
                            'color2': '#00BFFF',  # Light Blue
                            'direction': 'horizontal'
                        }
                    
                    i += 1
                
                # Add title to slide
                self.current_slide['title'] = title_data
                continue
            
            # Process subtitle
            if section == 'subtitle text':
                subtitle_data = {'type': 'textbox', 'text': '', 'left': 3.5, 'top': 4.5, 'width': 6.0, 'height': 1.0,
                                'font_name': 'Segoe UI', 'font_size': 32, 'color': '#BB86FC', 'alignment': 'center'}
                
                while i < len(lines) and not lines[i].startswith('SLIDE ') and not ':' in lines[i].strip()[-1:]:
                    line = lines[i].strip()
                    
                    # Extract subtitle text
                    if 'Text:' in line:
                        text_match = re.search(r'Text: "(.*)"', line)
                        if text_match:
                            subtitle_data['text'] = text_match.group(1)
                        else:
                            # Try without quotes
                            text_match = re.search(r'Text: (.*)', line)
                            if text_match:
                                subtitle_data['text'] = text_match.group(1)
                    
                    # Extract font info
                    if 'Font:' in line:
                        font_match = re.search(r'Font: ([^,]+), (\d+)pt', line)
                        if font_match:
                            subtitle_data['font_name'] = font_match.group(1)
                            subtitle_data['font_size'] = int(font_match.group(2))
                    
                    # Extract color
                    color_match = re.search(r'#([0-9A-Fa-f]{6})', line)
                    if color_match:
                        subtitle_data['color'] = f'#{color_match.group(1)}'
                    
                    i += 1
                
                # Add subtitle to slide elements
                self.current_slide['elements'].append(subtitle_data)
                continue
            
            # Process code examples
            if 'code example' in line.lower() or section == 'code example':
                code_data = {'type': 'code', 'code': '', 'left': 1.25, 'top': 4.0, 'width': 5.0, 'height': 1.5,
                            'font_name': 'Consolas', 'font_size': 16, 'text_color': '#03DAC6', 'bg_color': '#252525'}
                
                code_text = []
                i += 1  # Move to the next line where code starts
                
                # Collect code lines
                while i < len(lines) and not lines[i].startswith('SLIDE ') and not ':' in lines[i].strip()[-1:]:
                    line = lines[i].strip()
                    
                    # Check if this is a code line or a property
                    if 'Text:' in line:
                        code_match = re.search(r'Text: (.*)', line)
                        if code_match:
                            code_text.append(code_match.group(1))
                    elif 'Font:' in line or 'Position:' in line or 'Size:' in line:
                        # Process properties
                        pass
                    elif 'Background:' in line:
                        # Extract background color
                        color_match = re.search(r'#([0-9A-Fa-f]{6})', line)
                        if color_match:
                            code_data['bg_color'] = f'#{color_match.group(1)}'
                    elif 'Text color:' in line:
                        # Extract text color
                        color_match = re.search(r'#([0-9A-Fa-f]{6})', line)
                        if color_match:
                            code_data['text_color'] = f'#{color_match.group(1)}'
                    else:
                        # Assume it's a code line
                        code_text.append(line)
                    
                    i += 1
                
                code_data['code'] = '\n'.join(code_text)
                self.current_slide['elements'].append(code_data)
                continue
            
            # Process section headers
            if 'section header' in line.lower():
                header_data = {'type': 'textbox', 'text': '', 'left': 1.0, 'top': 2.0, 'width': 10.0, 'height': 0.7,
                              'font_name': 'Segoe UI', 'font_size': 28, 'bold': True, 'color': '#03DAC6'}
                
                # Find the header text
                while i < len(lines) and 'Text:' not in lines[i]:
                    i += 1
                
                if i < len(lines):
                    text_match = re.search(r'Text: "(.*)"', lines[i])
                    if text_match:
                        header_data['text'] = text_match.group(1)
                    else:
                        # Try without quotes
                        text_match = re.search(r'Text: (.*)', lines[i])
                        if text_match:
                            header_data['text'] = text_match.group(1)
                
                self.current_slide['elements'].append(header_data)
                i += 1
                continue
            
            # Process animations
            if section == 'animation sequence':
                while i < len(lines) and not lines[i].startswith('SLIDE ') and not ':' in lines[i].strip()[-1:]:
                    line = lines[i].strip()
                    
                    if line.startswith('1.') or line.startswith('-') or line.startswith('•'):
                        # This is an animation item
                        animation_data = {'type': '', 'element': '', 'duration': 1.0}
                        
                        # Extract animation type
                        if 'Animation:' in line:
                            anim_match = re.search(r'Animation: ([^>]+)> ([^$]+)', line)
                            if anim_match:
                                animation_data['type'] = anim_match.group(2).strip()
                        
                        # Look for details in subsequent lines
                        j = i + 1
                        while j < len(lines) and (lines[j].strip().startswith('•') or not lines[j].strip()):
                            detail_line = lines[j].strip()
                            
                            if 'Start:' in detail_line:
                                animation_data['timing'] = detail_line.split('Start:')[1].strip()
                            elif 'Duration:' in detail_line:
                                dur_match = re.search(r'Duration: ([\d\.]+)', detail_line)
                                if dur_match:
                                    animation_data['duration'] = float(dur_match.group(1))
                            elif 'Direction:' in detail_line:
                                animation_data['direction'] = detail_line.split('Direction:')[1].strip()
                            elif 'Delay:' in detail_line:
                                delay_match = re.search(r'Delay: ([\d\.]+)', detail_line)
                                if delay_match:
                                    animation_data['delay'] = float(delay_match.group(1))
                            
                            j += 1
                        
                        # Assign a target element
                        if 'title' in line.lower():
                            animation_data['element'] = 'Title'
                        elif 'subtitle' in line.lower():
                            animation_data['element'] = 'Subtitle'
                        else:
                            animation_data['element'] = f'Element {len(self.current_slide["animations"]) + 1}'
                        
                        self.current_slide['animations'].append(animation_data)
                    
                    i += 1
                continue
            
            # Process bullet points
            if line.startswith('•') or (i+1 < len(lines) and lines[i+1].strip().startswith('•')):
                bullet_section = True
                bullet_data = {'type': 'textbox', 'text': '', 'left': 1.0, 'top': 2.8, 'width': 5.0, 'height': 2.0,
                              'font_name': 'Segoe UI', 'font_size': 18, 'color': '#E0E0E0'}
                
                bullet_points = []
                
                while i < len(lines) and not lines[i].startswith('SLIDE '):
                    line = lines[i].strip()
                    
                    if line.startswith('•'):
                        bullet_points.append(line[1:].strip())
                    elif 'Position:' in line or 'Font:' in line or 'Text color:' in line:
                        # Process formatting
                        if 'Position:' in line:
                            pos_match = re.search(r'(\d+\.?\d*)"? from left, (\d+\.?\d*)', line)
                            if pos_match:
                                bullet_data['left'] = float(pos_match.group(1))
                                bullet_data['top'] = float(pos_match.group(2))
                    else:
                        # End of bullet points
                        if bullet_points:  # Only break if we've found some bullets
                            break
                    
                    i += 1
                
                if bullet_points:
                    bullet_data['text'] = '\n'.join([f"• {point}" for point in bullet_points])
                    self.current_slide['elements'].append(bullet_data)
                    continue
            
            # Just advance if we haven't handled this line
            i += 1
        
        # Add the processed slide
        self.slides.append(self.current_slide)
        
        return i
    
    def save_yaml(self, output_file):
        """Save the parsed specification as YAML"""
        spec = {
            'slide_size': self.slide_size,
            'slides': self.slides
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            yaml.dump(spec, f, default_flow_style=False, sort_keys=False)
        
        return spec


def main():
    parser = argparse.ArgumentParser(description='Convert PPT text specification to YAML format')
    parser.add_argument('input_file', help='Text specification file to convert')
    parser.add_argument('--output', '-o', default=None, help='Output YAML file (default: inputname.yaml)')
    
    args = parser.parse_args()
    
    # Set default output file name if not specified
    if not args.output:
        input_path = Path(args.input_file)
        args.output = str(input_path.with_suffix('.yaml'))
    
    # Parse the specification
    spec_parser = PPTSpecificationParser()
    spec = spec_parser.parse_file(args.input_file)
    spec_parser.save_yaml(args.output)
    
    print(f"Specification converted and saved to {args.output}")


if __name__ == "__main__":
    main()