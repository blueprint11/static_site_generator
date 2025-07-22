import unittest
from htmlnode import HTMLNode ,LeafNode, ParentNode

class Test_htmlnode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("div","Hello, world!",None,{"class": "greeting", "href": "https://boot.dev"})
        self.assertEqual(node.props_to_html(),' class="greeting" href="https://boot.dev"')
        self.assertEqual(node.tag,"div")

    def test_not_eq(self):
        hnode1=HTMLNode("p","the para is short",None,{"target": "_blank"})
        hnode2=HTMLNode("p","the para is short",None,{"target": "_full"})
        self.assertNotEqual(hnode1,hnode2)

    def test_value(self):
        hnode1=HTMLNode("p","the para is short",None,{"target": "_blank"})
        self.assertEqual(hnode1.value,"the para is short")
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>")

if __name__=="__main__":
    unittest.main()
