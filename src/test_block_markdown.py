import unittest

from block_markdown import markdown_to_blocks


class TestInlineMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        doc = "# This is a heading \n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item "
        expected_output = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
            '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ]

        self.assertEqual(
            markdown_to_blocks(doc),
            expected_output
        )
