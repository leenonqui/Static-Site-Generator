from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes: list, delimiter, text_type: TextType):
    # we need to distinguish between delimiters because if I look for italic (*) before looking for bold (**) it would generate a logic error in the code
    match (delimiter):
        case ('**'):
            return split_nodes(old_nodes, delimiter, text_type)
        case ('*'):
            return split_nodes(old_nodes, delimiter, text_type)
        case ('`'):
            return split_nodes(old_nodes, delimiter, text_type)
        case _:
            raise Exception(f"Invalid Markdown syntax: {delimiter} doesn't match any valid delimiter")

def split_nodes(old_nodes: list, delimiter, text_type: TextType):
    lst = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            lst.append(old_node)
            continue
        splitted_node = old_node.text.split(delimiter)
        if not is_delimiter_closed(splitted_node):
            raise Exception("Invalid Markdown syntax: delimiter not closed")
        lst.extend([TextNode(splitted_node[i],text_type) if is_odd(i) else TextNode(splitted_node[i], TextType.NORMAL) for i in range(len(splitted_node))])
    return lst

def extract_markdown_images(text):
    regex_syntax = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(regex_syntax, text)
def extract_markdown_links(text):
    regex_syntax = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(regex_syntax, text)

def is_odd(n: int):
    return (n%2 == 1)

def is_delimiter_closed(splitted_list: list):
    return (len(splitted_list)%2 == 1)
