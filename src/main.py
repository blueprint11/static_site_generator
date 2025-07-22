from textnode import TextNode ,Inline
def main():

    textnode=TextNode("some anchor text",Inline.LINK,"https://www.boot.dev" )
    print(textnode)

main()