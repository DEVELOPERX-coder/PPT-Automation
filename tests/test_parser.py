"""
Tests for the Markdown parser module.
"""

import os
import unittest
from tempfile import NamedTemporaryFile

from md2ppt.parser import MarkdownParser, SlideExtractor


class TestSlideExtractor(unittest.TestCase):
    """Tests for the SlideExtractor class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.extractor = SlideExtractor()
    
    def test_extract_metadata(self):
        """Test extracting metadata from comments."""
        raw_markdown = "<!-- theme: dark -->\n<!-- transition: fade -->"
        metadata = self.extractor._extract_metadata(raw_markdown)
        
        self.assertIn('theme', metadata)
        self.assertEqual(metadata['theme'], 'dark')
        self.assertIn('transition', metadata)
        self.assertEqual(metadata['transition'], 'fade')
    
    def test_parse_properties(self):
        """Test parsing properties string."""
        props_str = "transition=fade, duration=1.0, direction=left"
        props = self.extractor._parse_properties(props_str)
        
        self.assertIn('transition', props)
        self.assertEqual(props['transition'], 'fade')
        self.assertIn('duration', props)
        self.assertEqual(props['duration'], '1.0')
        self.assertIn('direction', props)
        self.assertEqual(props['direction'], 'left')


class TestMarkdownParser(unittest.TestCase):
    """Tests for the MarkdownParser class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.parser = MarkdownParser()
    
    def test_parse_simple_markdown(self):
        """Test parsing simple markdown."""
        # Create a temporary markdown file
        with NamedTemporaryFile(mode='w+', suffix='.md', delete=False) as f:
            f.write("# Slide Title\n\nThis is a paragraph.")
            temp_path = f.name
        
        try:
            # Parse the file
            slides = self.parser.parse(temp_path)
            
            # Check result
            self.assertEqual(len(slides), 1)
            self.assertEqual(slides[0]['title'], "Slide Title")
            self.assertEqual(len(slides[0]['elements']), 1)
            self.assertEqual(slides[0]['elements'][0]['type'], 'paragraph')
            self.assertEqual(slides[0]['elements'][0]['content'], "This is a paragraph.")
        finally:
            # Clean up
            os.unlink(temp_path)
    
    def test_parse_multiple_slides(self):
        """Test parsing markdown with multiple slides."""
        # Create a temporary markdown file
        with NamedTemporaryFile(mode='w+', suffix='.md', delete=False) as f:
            f.write("# Slide 1\n\nContent for slide 1.\n\n# Slide 2\n\nContent for slide 2.")
            temp_path = f.name
        
        try:
            # Parse the file
            slides = self.parser.parse(temp_path)
            
            # Check result
            self.assertEqual(len(slides), 2)
            self.assertEqual(slides[0]['title'], "Slide 1")
            self.assertEqual(slides[1]['title'], "Slide 2")
        finally:
            # Clean up
            os.unlink(temp_path)
    
    def test_parse_with_metadata(self):
        """Test parsing markdown with metadata."""
        # Create a temporary markdown file
        with NamedTemporaryFile(mode='w+', suffix='.md', delete=False) as f:
            f.write("<!-- theme: dark -->\n# Slide Title\n\n<!-- slide: transition=fade -->")
            temp_path = f.name
        
        try:
            # Parse the file
            slides = self.parser.parse(temp_path)
            
            # Check result
            self.assertEqual(len(slides), 1)
            self.assertEqual(slides[0]['title'], "Slide Title")
            # Check if metadata was extracted
            self.assertIn('properties', slides[0])
            self.assertIn('theme', slides[0]['properties'])
            self.assertEqual(slides[0]['properties']['theme'], 'dark')
        finally:
            # Clean up
            os.unlink(temp_path)


if __name__ == '__main__':
    unittest.main()