import unittest
from textnode import TextNode, TextType
from src.util.inline_markdown import split_nodes_delimiter
from src.util.inline_markdown import extract_markdown_images
from src.util.inline_markdown import extract_markdown_links

class TestInlineMarkdown(unittest.TestCase):
    def test_split_delimiter(self):
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

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_output = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(
            extract_markdown_images(text),
            expected_output
        )
        text2 = "this is a text without images"
        expected_output2 = []
        self.assertEqual(
            extract_markdown_images(text2),
            expected_output2
        )

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected_output = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(
            extract_markdown_links(text),
            expected_output
        )
        text2 = "this is a text without links"
        expected_output2 = []
        self.assertEqual(
            extract_markdown_links(text2),
            expected_output2
        )

if __name__ == "__main__":
    unittest.main()
