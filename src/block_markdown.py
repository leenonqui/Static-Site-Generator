import re


def markdown_to_blocks (doc: str) -> list[str]:
    return [item.strip() for item in list(doc.split('\n\n')) if item != ''] or []

"""
block_types -> [
    paragraph
    heading
    code
    quote
    unordered_list
    ordered_list
]
"""
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
