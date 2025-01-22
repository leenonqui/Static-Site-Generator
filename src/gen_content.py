import os
from block_markdown import markdown_to_html_node


def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    heads = os.listdir(dir_path_content)

    for head in heads:
        path = os.path.join(dir_path_content, head)

        if os.path.isfile(path) and path.endswith('.md'):
            generate_page(path, template_path, os.path.join(dest_dir_path, head.replace(".md", ".html")))

        elif os.path.isdir(path):
            generate_page_recursive(path, template_path, os.path.join(dest_dir_path, head))


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Get the markdown and template and store them in variables
    with open(from_path) as f:
        md_content = f.read()
    with open(template_path) as f:
        template = f.read()

    # Extract title and content from markdown
    title = extract_title(md_content)
    content = markdown_to_html_node(md_content).to_html()

    # Get the directory path
    directory = os.path.dirname(dest_path)

    # Create directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)

    # Write the full HTML page to dest_path
    with open(dest_path, 'w') as f:
        f.write(template.replace("{{ Title }}", title, 1).replace("{{ Content }}", content, 1))


def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line.lstrip("#").strip()
    raise Exception("No title found")
