"""
Markdown parser module for md2ppt using python-markdown.
"""

import re
import os
import html
import xml.etree.ElementTree as ET
from typing import List, Dict, Any, Union

import markdown
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor


class SlideExtractor:
    """Extract slides and elements from HTML produced by markdown parser."""
    
    def __init__(self):
        self.slides = []
        self.current_slide = None
        self._reset_slide()
    
    def _reset_slide(self):
        """Reset current slide data."""
        self.current_slide = {
            'title': None,
            'elements': [],
            'properties': {},
        }
    
    def extract_slides(self, html_content, raw_markdown):
        """Extract slides from HTML content."""
        # Create root element for parsing
        root = ET.fromstring(f"<root>{html_content}</root>")
        
        # First, extract global metadata from comments
        metadata = self._extract_metadata(raw_markdown)
        
        # Process the HTML tree
        self._process_elements(root)
        
        # Add any global metadata to the first slide
        if self.slides and metadata:
            for key, value in metadata.items():
                self.slides[0]['properties'][key] = value
        
        return self.slides
    
    def _extract_metadata(self, raw_markdown):
        """Extract global metadata from HTML comments."""
        metadata = {}
        metadata_pattern = r'<!--\s*(.+?):(.*?)\s*-->'
        matches = re.findall(metadata_pattern, raw_markdown)
        
        for key, value in matches:
            key = key.strip()
            value = value.strip()
            
            # Store special metadata
            if key == 'theme' or key == 'transition':
                metadata[key] = value
        
        return metadata
    
    def _process_elements(self, root):
        """Process HTML elements to build slides."""
        # Process all top-level elements
        for elem in root:
            if elem.tag == 'h1':
                # New slide with title
                if self.current_slide['title'] or self.current_slide['elements']:
                    self.slides.append(self.current_slide)
                    self._reset_slide()
                
                self.current_slide['title'] = self._get_element_text(elem)
                
                # Check for animation or properties
                self._process_comments(elem)
            else:
                # Add elements to current slide
                self._process_element(elem)
        
        # Add the last slide if it has content
        if self.current_slide['title'] or self.current_slide['elements']:
            self.slides.append(self.current_slide)
    
    def _process_element(self, elem):
        """Process a single HTML element."""
        if elem.tag == 'h2':
            # Subheading
            self.current_slide['elements'].append({
                'type': 'heading',
                'content': self._get_element_text(elem),
                'level': 2
            })
            self._process_comments(elem)
        elif elem.tag == 'h3':
            # Sub-subheading
            self.current_slide['elements'].append({
                'type': 'heading',
                'content': self._get_element_text(elem),
                'level': 3
            })
            self._process_comments(elem)
        elif elem.tag == 'p':
            # Paragraph or image
            img = elem.find('img')
            if img is not None:
                # Image
                self.current_slide['elements'].append({
                    'type': 'image',
                    'src': img.get('src', ''),
                    'alt': img.get('alt', ''),
                    'title': img.get('title', '')
                })
            else:
                # Regular paragraph
                self.current_slide['elements'].append({
                    'type': 'paragraph',
                    'content': self._get_element_text(elem)
                })
            self._process_comments(elem)
        elif elem.tag == 'pre':
            # Code block
            code = elem.find('code')
            if code is not None:
                language = None
                classes = code.get('class', '')
                if classes:
                    # Extract language from class like "language-python"
                    lang_match = re.search(r'language-(\w+)', classes)
                    if lang_match:
                        language = lang_match.group(1)
                
                self.current_slide['elements'].append({
                    'type': 'code_block',
                    'content': self._get_element_text(code),
                    'language': language
                })
            self._process_comments(elem)
        elif elem.tag == 'blockquote':
            # Blockquote
            self.current_slide['elements'].append({
                'type': 'quote',
                'content': self._get_element_text(elem)
            })
            self._process_comments(elem)
        elif elem.tag in ('ul', 'ol'):
            # List
            list_type = 'ordered_list' if elem.tag == 'ol' else 'unordered_list'
            items = []
            for li in elem.findall('li'):
                items.append({
                    'type': 'list_item',
                    'content': self._get_element_text(li),
                    'level': 1
                })
                self._process_comments(li)
            
            self.current_slide['elements'].append({
                'type': list_type,
                'content': items,
                'level': 1
            })
            self._process_comments(elem)
        elif elem.tag == 'table':
            # Table
            header = []
            body = []
            
            # Process header (first tr in thead)
            thead = elem.find('thead')
            if thead is not None:
                tr = thead.find('tr')
                if tr is not None:
                    for th in tr.findall('th'):
                        header.append(self._get_element_text(th))
            
            # Process body rows
            tbody = elem.find('tbody')
            if tbody is not None:
                for tr in tbody.findall('tr'):
                    row = []
                    for td in tr.findall('td'):
                        row.append(self._get_element_text(td))
                    body.append(row)
            
            self.current_slide['elements'].append({
                'type': 'table',
                'header': header,
                'body': body
            })
            self._process_comments(elem)
        # Process comments directly in the markup
        elif elem.tag is ET.Comment:
            self._process_comment(elem.text)
    
    def _get_element_text(self, elem):
        """Get text content from an element, preserving HTML formatting."""
        if elem.text is None:
            text = ""
        else:
            text = elem.text
        
        for child in elem:
            if child.tag == 'strong' or child.tag == 'b':
                content = self._get_element_text(child)
                text += f"**{content}**"
            elif child.tag == 'em' or child.tag == 'i':
                content = self._get_element_text(child)
                text += f"*{content}*"
            elif child.tag == 'code':
                content = self._get_element_text(child)
                text += f"`{content}`"
            elif child.tag == 'a':
                content = self._get_element_text(child)
                href = child.get('href', '')
                text += f"[{content}]({href})"
            else:
                text += self._get_element_text(child)
            
            if child.tail:
                text += child.tail
        
        return text
    
    def _process_comments(self, elem):
        """Process comments that might be attached to an element."""
        # Check if there's a comment directly after this element
        if elem.tail and '<!--' in elem.tail:
            comment_match = re.search(r'<!--\s*(.*?)\s*-->', elem.tail)
            if comment_match:
                comment_text = comment_match.group(1)
                self._process_comment(comment_text)
    
    def _process_comment(self, comment_text):
        """Process a comment for metadata or animation."""
        if not comment_text:
            return
            
        comment_text = comment_text.strip()
        
        # Check for slide properties
        if comment_text.startswith('slide:'):
            props_str = comment_text[6:].strip()
            props = self._parse_properties(props_str)
            self.current_slide['properties'].update(props)
        # Check for animation directive
        elif comment_text.startswith('animation:'):
            animation_str = comment_text[10:].strip()
            # Apply to the last element
            if self.current_slide['elements']:
                self.current_slide['elements'][-1]['animation'] = animation_str
        # Check for other metadata properties
        elif ':' in comment_text:
            key, value = comment_text.split(':', 1)
            self.current_slide['properties'][key.strip()] = value.strip()
    
    def _parse_properties(self, props_str):
        """Parse properties from string like 'key1=value1, key2=value2'."""
        result = {}
        if not props_str:
            return result
            
        parts = props_str.split(',')
        for part in parts:
            if '=' in part:
                key, value = part.split('=', 1)
                result[key.strip()] = value.strip()
        
        return result


class CommentPreservationExtension(Extension):
    """Markdown extension to preserve HTML comments."""
    
    def extendMarkdown(self, md):
        md.treeprocessors.register(CommentPreservationProcessor(md), 'comment_preservation', 175)


class CommentPreservationProcessor(Treeprocessor):
    """Processor that preserves HTML comments."""
    
    def run(self, root):
        return root


class MarkdownParser:
    """
    Parser for converting markdown files to a structured format
    that can be used to generate PowerPoint presentations.
    """
    
    def __init__(self):
        """Initialize the parser."""
        self.markdown = markdown.Markdown(extensions=[
            'markdown.extensions.tables',
            'markdown.extensions.fenced_code',
            CommentPreservationExtension()
        ])
        self.extractor = SlideExtractor()
    
    def parse(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Parse a markdown file and return a structured representation.
        
        Args:
            file_path: Path to the markdown file
            
        Returns:
            A list of slide dictionaries
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Convert markdown to HTML
        html_content = self.markdown.convert(content)
        
        # Extract slides from HTML
        slides = self.extractor.extract_slides(html_content, content)
        
        # Process slide properties and metadata
        self._process_metadata(slides, content)
        
        return slides
    
    def _process_metadata(self, slides: List[Dict[str, Any]], content: str) -> None:
        """
        Process slide metadata and properties from comments and attributes.
        
        Args:
            slides: List of slide dictionaries
            content: Raw markdown content
        """
        # Extract metadata from HTML comments
        metadata_pattern = r'<!--\s*slide:\s*(.+?)\s*-->'
        slide_matches = re.findall(metadata_pattern, content)
        
        # Map slide-specific metadata to appropriate slides
        slide_idx = 0
        content_lines = content.split('\n')
        
        for i, line in enumerate(content_lines):
            if line.startswith('# '):
                # Found a slide title, move to next slide index
                if slide_idx < len(slides):
                    slide_idx += 1
            
            # Check for slide-specific properties
            match = re.search(metadata_pattern, line)
            if match and slide_idx < len(slides):
                props_str = match.group(1)
                if '=' in props_str:
                    key, value = props_str.split('=', 1)
                    slides[slide_idx]['properties'][key.strip()] = value.strip()