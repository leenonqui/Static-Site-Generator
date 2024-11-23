import unittest

from htmlnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_texttype(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node(self):
        err_node = TextNode("This is a text node", TextType)
        with self.assertRaises(Exception):
            text_node_to_html_node(err_node)
        node = TextNode("This is a normal text node", TextType.NORMAL)
        self.assertEqual(
            text_node_to_html_node(node),
            LeafNode(None, node.text,)
        )
        b_node = TextNode("This is a bold text node", TextType.BOLD)
        self.assertEqual(
            text_node_to_html_node(b_node),
            LeafNode('b', b_node.text,)
        )
        i_node = TextNode("This is an italic text node", TextType.ITALIC)
        self.assertEqual(
            text_node_to_html_node(i_node),
            LeafNode('i', i_node.text,)
        )
        code_node = TextNode("This is a code text node", TextType.CODE)
        self.assertEqual(
            text_node_to_html_node(code_node),
            LeafNode('code', code_node.text,)
        )
        a_node = TextNode("This is a link text node", TextType.LINKS)
        self.assertEqual(
            text_node_to_html_node(a_node),
            LeafNode('a', a_node.text, {"href": f"{a_node.url}"})
        )
        img_node = TextNode("This is an image text node", TextType.IMAGES)
        self.assertEqual(
            text_node_to_html_node(img_node),
            LeafNode('img', '', {"src": f"{img_node.url}",
                                 "alt": f"{img_node.text}"}
                     )
        )


if __name__ == "__main__":
    unittest.main()
