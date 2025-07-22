import unittest
from htmlnode import HTMLNode

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

if __name__=="__main__":
    unittest.main()
