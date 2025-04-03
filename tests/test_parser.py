"""
Tests for the Markdown parser module.
"""

import os
import unittest
from tempfile import NamedTemporaryFile

from md2ppt.parser import MarkdownParser, PPTRenderer


class TestPPTRenderer(unittest.TestCase):
    """Tests for the PPTRenderer class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.renderer = PPTRenderer()
    
    def test_heading_level1_creates_new_slide(self):
        """Test that level 1 heading creates a new slide."""
        # Process a heading
        self.renderer.heading("Slide Title", 1)
        
        # Check that current slide has the title
        self.assertEqual(self.renderer.current_slide['title'], "Slide Title")
        self.assertEqual(len(self.renderer.current_elements), 0)
    
    def test_paragraph_adds_to_current_slide(self):
        """Test that paragraph adds to current slide elements."""
        # Process a paragraph
        self.renderer.paragraph("This is a paragraph.")
        
        # Check that element was added
        self.assertEqual(len(self.renderer.current_elements), 1)
        self.assertEqual(self.renderer.current_elements[0]['type'], 'paragraph')
        self.assertEqual(self.renderer.current_elements[0]['content'], "This is a paragraph.")
    
    def test_list_adds_to_current_slide(self):
        """Test that list adds to current slide elements."""
        # Create list items
        item1 = self.renderer.list_item("Item 1")
        item2 = self.renderer.list_item("Item 2")
        
        # Process a list with the items
        self.renderer.list([item1, item2], ordered=False)
        
        # Check that element was added
        self.assertEqual(len(self.renderer.current_elements), 1)
        self.assertEqual(self.renderer.current_elements[0]['type'], 'unordered_list')
        self.assertEqual(len(self.renderer.current_elements[0]['content']), 2)
    
    def test_finalize_returns_slides(self):
        """Test that finalize returns slides."""
        # Set up slides
        self.renderer.heading("Slide 1", 1)
        self.renderer.paragraph("Paragraph on slide 1.")
        
        self.renderer.heading("Slide 2", 1)
        self.renderer.paragraph("Paragraph on slide 2.")
        
        # Finalize to get slides
        slides = self.renderer.finalize(None)
        
        # Check slides
        self.assertEqual(len(slides), 2)
        self.assertEqual(slides[0]['title'], "Slide 1")
        self.assertEqual(slides[1]['title'], "Slide 2")
        self.assertEqual(slides[0]['elements'][0]['content'], "Paragraph on slide 1.")
        self.assertEqual(slides[1]['elements'][0]['content'], "Paragraph on slide 2.")


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
        finally:
            # Clean up
            os.unlink(temp_path)


if __name__ == '__main__':
    unittest.main()