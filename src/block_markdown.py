# imports


# code
def markdown_to_blocks (doc: str) -> list[str]:
    return [item.strip(' ') for item in list(doc.split('\n\n'))] or []
