from textnode import TextNode, TextType
from utilities import is_odd, is_delimiter_closed
import re


def text_to_textnodes(text: str) -> list:
    textnode = TextNode(text, TextType.TEXT)
    return (split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(split_nodes_link(split_nodes_image([textnode])), '**'), '*'), '`'))

def split_nodes_delimiter(old_nodes: list, delimiter) -> list:
    # we need to distinguish between delimiters because if I look for italic (*) before looking for bold (**) it would generate a logic error in the code
    match (delimiter):
        case ('**'):
            return split_nodes(old_nodes, delimiter, TextType.BOLD)
        case ('*'):
            return split_nodes(old_nodes, delimiter, TextType.ITALIC)
        case ('`'):
            return split_nodes(old_nodes, delimiter, TextType.CODE)
        case _:
            raise Exception(f"Invalid Markdown syntax: {delimiter} doesn't match any valid delimiter")

def split_nodes(old_nodes: list, delimiter, text_type: TextType) -> list:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        splitted_node = list(old_node.text.split(delimiter))
        if not is_delimiter_closed(splitted_node):
            raise Exception("Invalid Markdown syntax: delimiter not closed")
        if '' in splitted_node :
            index = splitted_node.index('')
            del splitted_node[index]
        new_nodes.extend([TextNode(splitted_node[i],text_type) if is_odd(i) else TextNode(splitted_node[i], TextType.TEXT) for i in range(len(splitted_node))])
    return new_nodes

def split_nodes_image (old_nodes):
    new_nodes = []
    for node in old_nodes:
        if not node.text:
            continue
        extracted_images = extract_markdown_images(node.text)
        if not extracted_images:
            new_nodes.append(node)
            continue
        sections = get_text_sections(node.text, extracted_images, image_splitter)
        new_nodes.extend([TextNode(extracted_images[i//2][0], TextType.IMAGE, extracted_images[i//2][1]) if is_odd(i) else TextNode(sections[i//2], TextType.TEXT) for i in range(len(extracted_images) + len(sections))])
    return new_nodes

def split_nodes_link (old_nodes):
    new_nodes = []
    for node in old_nodes:
        if not node.text:
            continue
        extracted_links = extract_markdown_links(node.text)
        if not extracted_links:
            new_nodes.append(node)
            continue
        sections = get_text_sections(node.text, extracted_links, link_splitter)
        new_nodes.extend([TextNode(extracted_links[i//2][0], TextType.LINK, extracted_links[i//2][1]) if is_odd(i) else TextNode(sections[i//2], TextType.TEXT) for i in range(len(extracted_links) + len(sections))])
    return new_nodes


def extract_markdown_images(text):
    regex_syntax = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(regex_syntax, text)

def extract_markdown_links(text):
    regex_syntax = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(regex_syntax, text)

def get_text_sections(text, tups, splitter_func):
    sections = []
    next_section = text
    section = ''
    if len(tups) == 1:
        return list(splitter_func(next_section, tups[0]))
    for tup in tups:
        temp = splitter_func(next_section, tup)
        if type(temp) == str and temp != '':
           sections.append(temp)
        else:
            section, next_section = temp
            sections.append(section)

    return sections

def link_splitter(text, tup):
    alt, url = tup
    link = f"[{alt}]({url})"
    sections = text.split(link, 1)
    if type(sections) == str:
        return sections
    section, next_section = sections
    return section, next_section

def image_splitter(text, tup):
    alt, url = tup
    link = f"![{alt}]({url})"
    sections = text.split(link, 1)
    if type(sections) == str:
        return sections
    section, next_section = sections
    return section, next_section
