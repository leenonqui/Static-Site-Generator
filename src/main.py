# imports
from textnode import TextType, TextNode

# code
def main():
    myTextNode = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(myTextNode.__repr__())

if __name__ == '__main__':
    main()
