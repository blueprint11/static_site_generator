import unittest
from textnode import TextNode, Inline

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

if __name__ =="__main__":
    unittest.main()
