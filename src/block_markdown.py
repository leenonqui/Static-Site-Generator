import re
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node


block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_html_node(doc: str):
    blocks = markdown_to_blocks(doc)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode(tag='div', children=children)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def text_to_children(text: str):
    htmlnodes = []
    textnodes = text_to_textnodes(text)
    for textnode in textnodes:
        htmlnodes.append(text_node_to_html_node(textnode))
    return htmlnodes

def markdown_to_blocks (doc: str) -> list[str]:
    return [item.strip() for item in list(doc.split('\n\n')) if item != ''] or []

def block_to_block_type(block: str) -> str:
    if is_heading(block):
        return 'heading'
    if is_code(block):
        return 'code'
    if is_quote(block):
        return 'quote'
    if is_unordered_list(block):
        return 'unordered_list'
    if is_ordered_list(block):
        return 'ordered_list'
    return 'paragraph'

def is_heading(block: str) -> bool:
    return bool(re.match(r"^(#{1,6})\s", block))

def is_code(block: str) -> bool:
    return block.startswith("```") and block.endswith("```")

def is_quote(block: str) -> bool:
    return all(re.match(r"^>", line) for line in block.splitlines())

def is_unordered_list(block: str) -> bool:
    return all(re.match(r"^[*-] ", line) for line in block.splitlines())

def is_ordered_list(block: str) -> bool:
    for i, line in enumerate(block.splitlines(), start=1):
        if not re.match(rf"^{i}\. ", line):
            return False
    return True
