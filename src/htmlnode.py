class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ''
        list = map(lambda key: f'{key}="{self.props[key]}"', self.props)
        return ' ' + ' '.join(list)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        else:
            if self.props is None:
                return f'<{self.tag}>{self.value}</{self.tag}>'
            return f'<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag can't be of value None")
        if self.children is None:
            raise ValueError("parent node children can't be of value None")
        if self.props is None:
            return f"<{self.tag}>{''.join(map(lambda c: c.to_html(), self.children))}</{self.tag}>"
        return f"<{self.tag}{super().props_to_html()}>{''.join(map(lambda c: c.to_html(), self.children))}</{self.tag}>"
