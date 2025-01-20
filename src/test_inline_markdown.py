import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter, split_nodes_image, split_nodes_link, split_nodes
from inline_markdown import extract_markdown_images
from inline_markdown import extract_markdown_links
from inline_markdown import text_to_textnodes

class TestInlineMarkdown(unittest.TestCase):
    def test_split_delimiter(self):
        test_list = [
            TextNode("This is text with a **bolded phrase** in the middle.", TextType.TEXT),
            TextNode("This is text with a `code block` in it.", TextType.TEXT)
        ]
        expected_list = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle.", TextType.TEXT),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" in it.", TextType.TEXT),
        ]
        self.assertEqual(
            split_nodes_delimiter(split_nodes_delimiter(test_list,'**'),'`'),
            expected_list
        )

    def test_bold_text_splitting(self):
        # Arrange
        text = "**I like Tolkien**"
        node = TextNode(text, TextType.TEXT)

        # Act
        result = split_nodes([node], "**", TextType.BOLD)

        # Debug prints
        print("\nOriginal text split:", text.split("**"))
        print("Result nodes:", result)

        # Assert
        expected = [
            TextNode("", TextType.TEXT),
            TextNode("I like Tolkien", TextType.BOLD),
            TextNode("", TextType.TEXT)
        ]
        self.assertEqual(result, expected)

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

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        expected_output = [
            TextNode("This is text with a link ", TextType.TEXT, None),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT, None),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
        self.assertEqual(
            split_nodes_link([node]),
            expected_output
        )

        nodes = [
            TextNode(
                "This is text with a link [to boot dev](https://www.boot.dev).",
                TextType.TEXT
            ),
            TextNode(
                "This is text with a link [to youtube](https://www.youtube.com/@bootdotdev).",
                TextType.TEXT
            )
        ]
        expected_output_nodes = [
            TextNode("This is text with a link ", TextType.TEXT, None),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(".", TextType.TEXT, None),
            TextNode("This is text with a link ", TextType.TEXT, None),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            TextNode(".", TextType.TEXT, None)
        ]
        self.assertEqual(
            split_nodes_link(nodes),
            expected_output_nodes
        )

    def test_split_node_image(self):
        node = TextNode(
            "This is text with an image ![of boot](https://www.boot.dev) and ![of youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )

        expected_output = [
            TextNode("This is text with an image ", TextType.TEXT, None),
            TextNode("of boot", TextType.IMAGE, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT, None),
            TextNode("of youtube", TextType.IMAGE, "https://www.youtube.com/@bootdotdev"),
        ]

        self.assertEqual(
            split_nodes_image([node]),
            expected_output
        )

        text_node = TextNode(
            "Simply Text",
            TextType.TEXT
        )
        expected_output = [
            TextNode("Simply Text", TextType.TEXT)
        ]

        self.assertEqual(
            split_nodes_image([text_node]),
            expected_output
        )


    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected_output = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertEqual(
            text_to_textnodes(text),
            expected_output
        )

        text = "Simply Text"
        expected_output = [
            TextNode("Simply Text", TextType.TEXT)
        ]

        self.assertEqual(
            text_to_textnodes(text),
            expected_output
        )


if __name__ == "__main__":
    unittest.main()
