import re
import yaml
import sys
from pathlib import Path

def convert_markdown_to_yaml(md_file, yaml_file):
    # Read markdown file
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    slide_size = {'width': 13.33, 'height': 7.5}  # 16:9 ratio
    slides = []
    current_slide = None
    current_section = None
    
    for line in lines:
        line = line.rstrip()
        
        # Look for slide markers
        slide_match = re.match(r'^#\s*SLIDE\s+(\d+):\s*(.+)$', line)
        if slide_match:
            # Save previous slide if exists
            if current_slide:
                slides.append(current_slide)
            
            # Create new slide
            slide_num = slide_match.group(1)
            slide_title = slide_match.group(2).strip()
            current_slide = {
                'layout': 'blank',
                'background': {'color': '#1A1A1A'},  # Dark charcoal
                'title': {
                    'text': slide_title,
                    'left': 1.0,
                    'top': 0.8,
                    'width': 10.0,
                    'height': 1.0,
                    'font_name': 'Segoe UI Light',
                    'font_size': 40,
                    'bold': True,
                    'color': '#00FFFF'  # Cyan
                },
                'elements': [],
                'animations': []
            }
            current_section = None
            continue
        
        # Skip if no current slide
        if not current_slide:
            continue
        
        # Look for section markers
        section_match = re.match(r'^##\s+(.+)$', line)
        if section_match:
            current_section = section_match.group(1).strip()
            continue
        
        # Process content based on section
        if current_section and line.strip():
            # Skip empty lines
            if not line.strip():
                continue
                
            # Process bullet points
            if line.strip().startswith('- ') or line.strip().startswith('* '):
                content = line.strip()[2:].strip()
                
                # Process based on section type
                if "background" in current_section.lower():
                    if "dark charcoal" in content.lower() or "#1A1A1A" in content:
                        current_slide['background']['color'] = '#1A1A1A'
                
                elif "title" in current_section.lower() and "text" in current_section.lower():
                    if "text:" in content.lower():
                        text_match = re.search(r'text:\s*"(.+)"', content, re.IGNORECASE)
                        if text_match:
                            current_slide['title']['text'] = text_match.group(1)
                    elif "font:" in content.lower():
                        font_match = re.search(r'font:\s*([^,]+),\s*(\d+)pt', content, re.IGNORECASE)
                        if font_match:
                            current_slide['title']['font_name'] = font_match.group(1).strip()
                            current_slide['title']['font_size'] = int(font_match.group(2))
                
                elif "subtitle" in current_section.lower():
                    if "text:" in content.lower():
                        text_match = re.search(r'text:\s*"(.+)"', content, re.IGNORECASE)
                        if text_match:
                            subtitle_text = text_match.group(1)
                            current_slide['elements'].append({
                                'type': 'textbox',
                                'text': subtitle_text,
                                'left': 3.5,
                                'top': 4.5,
                                'width': 6.0,
                                'height': 1.0,
                                'font_name': 'Segoe UI',
                                'font_size': 32,
                                'color': '#BB86FC',  # Light Purple
                                'alignment': 'center'
                            })
                
                elif "code" in current_section.lower() and "example" in current_section.lower():
                    # Collect code across multiple lines if needed
                    code_text = content
                    current_slide['elements'].append({
                        'type': 'code',
                        'code': code_text,
                        'left': 1.25,
                        'top': 4.0,
                        'width': 5.0,
                        'height': 1.5,
                        'font_name': 'Consolas',
                        'font_size': 16,
                        'text_color': '#03DAC6',  # Light Green
                        'bg_color': '#252525'  # Very Dark Gray
                    })
                
                elif "section header" in current_section.lower():
                    if "text:" in content.lower():
                        text_match = re.search(r'text:\s*"(.+)"', content, re.IGNORECASE)
                        if text_match:
                            header_text = text_match.group(1)
                            current_slide['elements'].append({
                                'type': 'textbox',
                                'text': header_text,
                                'left': 1.0,
                                'top': 2.0,
                                'width': 10.0,
                                'height': 0.7,
                                'font_name': 'Segoe UI',
                                'font_size': 28,
                                'bold': True,
                                'color': '#03DAC6'  # Light Green
                            })
    
    # Add the last slide if it exists
    if current_slide:
        slides.append(current_slide)
    
    # Create final specification
    spec = {
        'slide_size': slide_size,
        'slides': slides
    }
    
    # Save as YAML
    with open(yaml_file, 'w', encoding='utf-8') as f:
        yaml.dump(spec, f, default_flow_style=False)
    
    print(f"Converted '{md_file}' to '{yaml_file}'")
    if not slides:
        print("WARNING: No slides were found in the Markdown file.")
        print("Make sure your slides use the format: '# SLIDE 1: Title'")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python md_to_ppt.py input.md output.yaml")
    else:
        convert_markdown_to_yaml(sys.argv[1], sys.argv[2])