

class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag=tag                            #like p,h1 
        self.value=value                        #string repr.of value of tag like paragraph
        self.children=children                  #list of html node objects tht are children to node
        self.props=props                        #dict of key value pairs for attributes of html tag like <a>href
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        s=""
        if self.props is None:
            return ""
        for key,value in self.props.items():
            s+= f' {key}="{value}"'
        return s
    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},children:{self.children},{self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None,value=None, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value==None:
            raise ValueError
        if self.tag==None:
            return self.value
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        

