import unittest
from textnode import TextNode, Inline,text_node_to_html_node

class Test_textnode(unittest.TestCase):
    def test_eq(self):
        node1=TextNode("this is node",Inline.BOLD)
        node2=TextNode("this is node",Inline.BOLD)
        self.assertEqual(node1,node2)

    def test_not_eq(self):
        node1=TextNode("this is node",Inline.ITALIC)
        node2=TextNode("this is node",Inline.BOLD)
        self.assertNotEqual(node1,node2)
    def test_diff_url(self):
        node1=TextNode("this is node",Inline.BOLD,"google.com")
        node2=TextNode("this is node",Inline.BOLD)
        self.assertNotEqual(node1,node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", Inline.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", Inline.IMG, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.google.com", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", Inline.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

if __name__ =="__main__":
    unittest.main()
