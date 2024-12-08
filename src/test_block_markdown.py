import unittest

from block_markdown import markdown_to_blocks


class TestInlineMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""
        blocks = [
            '# This is a heading',
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
            '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ]

        self.assertEqual(
            markdown_to_blocks(md),
            blocks
        )

    def test_multiple_newlines(self):
        md = """
# This is a heading



This is a paragraph of text. It has some **bold** and *italic* words inside of it.

"""
        blocks = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it."
        ]

        self.assertEqual(
            markdown_to_blocks(md),
            blocks
        )


if __name__ == "__main__":
    unittest.main()
