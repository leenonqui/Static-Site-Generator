import unittest
from textnode import TextNode, TextType
from util.inline_markdown import split_nodes_delimiter

class TestSplitDelimiter(unittest.TestCase):
    def test(self):
        test_list = [
            TextNode("This is text with a **bolded phrase** in the middle.", TextType.NORMAL),
            TextNode("This is text with a `code block` in it.", TextType.NORMAL)
        ]
        expected_list = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle.", TextType.NORMAL),
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" in it.", TextType.NORMAL),
        ]
        self.assertEqual(
            split_nodes_delimiter(split_nodes_delimiter(test_list,'**', TextType.BOLD),'`', TextType.CODE),
            expected_list
        )

if __name__ == "__main__":
    unittest.main()
