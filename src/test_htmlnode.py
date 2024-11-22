import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode()
        self.assertEqual(
            node.props_to_html(),
            ''
        )

    def test_one_property(self):
        node = HTMLNode(
            props={"class": "header"}
        )
        expected_output = ' class="header"'
        self.assertEqual(
            node.props_to_html(),
            expected_output
        )

    def test_more_properties(self):
        node = HTMLNode(
            props={"href": "https://example.com", "target": "_blank"}
        )
        expected_output = ' href="https://example.com" target="_blank"'
        self.assertEqual(
            node.props_to_html(),
            expected_output
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I didn't need to test XD"
        )
        self.assertEqual(
            node.tag,
            'div'
        )
        self.assertEqual(
            node.value,
            "I wish I didn't need to test XD"
        )
        self.assertEqual(
            node.children,
            None
        )
        self.assertEqual(
            node.props,
            None
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})"
        )

    def test_leafnode(self):
        node = LeafNode(
            "p",
            "What a strange test",
            {"href": "https://www.google.com"}
        )
        node2 = LeafNode(
            None,
            "What a strange test"
        )
        self.assertEqual(
            node.tag,
            "p"
        )
        self.assertEqual(
            node.value,
            "What a strange test"
        )
        self.assertEqual(
            node.props,
            {"href": "https://www.google.com"}
        )

        self.assertEqual(
            node2.tag,
            None
        )
        self.assertEqual(
            node2.value,
            "What a strange test"
        )
        self.assertEqual(
            node2.props,
            None
        )

    def test_leaf_to_html(self):
        node = LeafNode(
            None,
            "What a strange test"
        )
        node2 = LeafNode(
            "p",
            "This is a paragraph of text."
        )
        node3 = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com"}
        )

        self.assertEqual(
            node.to_html(),
            "What a strange test"
        )
        self.assertEqual(
            node2.to_html(),
            "<p>This is a paragraph of text.</p>"
        )
        self.assertEqual(
            node3.to_html(),
            '<a href="https://www.google.com">Click me!</a>'
        )

    def test_value_error_to_html(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()


if __name__ == "__main__":
    unittest.main()