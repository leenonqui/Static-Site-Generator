import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_no_props(self):
        node = HTMLNode()
        self.assertEqual(
            node.props_to_html(),
            ''
        )

    def test_one_property(self):
        node = HTMLNode(
            props={"class":"header"}
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

if __name__ == "__main__":
    unittest.main()
