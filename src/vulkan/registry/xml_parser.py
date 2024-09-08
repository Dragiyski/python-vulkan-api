from xml.parsers import expat


class Node:
    def __init__(self, node_name: str, node_value: str, node_type: str, attributes: dict = {}):
        self.child_nodes = []
        self.children = {}
        self.parent_node = None
        self.parent_index = None
        self.parent_name_index = None
        self.node_name = node_name
        self.attributes = dict(attributes)
        self.node_type = node_type
        self.node_value = node_value

    def has_attribute(self, name: str):
        return name in self.attributes

    def get_attribute(self, name: str, default=None):
        if self.has_attribute(name):
            return self.attributes[name]
        return default

    def set_attribute(self, name: str, value, override=True):
        if override or not self.has_attribute(name):
            self.attributes[name] = value

    def get(self, name: str, default=None):
        if name not in self.children:
            return default
        node_list = self.children[name]
        assert len(node_list) == 1, f'{get_error_prefix(self)}: Expected 1 child with name "{name}", got {len(node_list)} children'
        return node_list[0]

    def get_all(self, name: str) -> 'list[Node]':
        if name not in self.children:
            return []
        return self.children[name]

    def append_child(self, node):
        if node.node_name not in self.children:
            self.children[node.node_name] = []
        child_index = len(self.child_nodes)
        child_name_index = len(self.children[node.node_name])
        node.parent_node = self
        node.parent_index = child_index
        node.parent_name_index = child_name_index
        self.child_nodes.append(node)
        self.children[node.node_name].append(node)

    def get_text_nodes(self, *, skip_comments = True):
        for child in self.child_nodes:
            if child.node_type == 'text':
                yield child
            elif child.node_type == 'element':
                if skip_comments and child.node_name == 'comment':
                    continue
                yield from child.get_text_nodes()

    def get_text(self, *, skip_comments = True):
        if self.node_type == 'text':
            return self.node_value
        elif self.node_type == 'element':
            return ''.join([x.node_value for x in self.get_text_nodes(skip_comments=skip_comments)])
        else:
            return ''
        
    def get_path(self):
        return (self.parent_node.get_path() if self.parent_node is not None else []) + [self.node_name]

    def get_text_nodes_before(self, node):
        items = []
        self._get_text_nodes_before(node, items)
        return items

    def get_text_nodes_after(self, node):
        items = []
        self._get_text_nodes_after(node, items)
        return items
    
    def get_text_before(self, node, *, skip_comments = True):
        return ''.join([n.get_text() for n in self.get_text_nodes_before(node, skip_comments=skip_comments)])
    
    def get_text_after(self, node, *, skip_comments = True):
        return ''.join([n.get_text() for n in self.get_text_nodes_after(node, skip_comments=skip_comments)])

    def _get_text_nodes_before(self, node, items, *, skip_comments = True):
        return_value = True
        for child in self.child_nodes:
            if not return_value:
                break
            if child is node:
                return False
            if child.node_type == 'text':
                items.append(child)
            elif child.node_type == 'element':
                if skip_comments and child.node_name == 'comment':
                    continue
                return_value = child._get_text_nodes_before(node, items)
        return return_value

    def _get_text_nodes_after(self, node, items, *, skip_comments = True):
        return_value = True
        for child in reversed(self.child_nodes):
            if not return_value:
                break
            if child is node:
                return False
            if child.node_type == 'text':
                items.insert(0, child)
            elif child.node_type == 'element':
                if skip_comments and child.node_name == 'comment':
                    continue
                return_value = child._get_text_nodes_before(node, items)
        return return_value

    @property
    def previous_sibling(self):
        if self.parent_node is None:
            return None
        assert isinstance(self.parent_index, int)
        if self.parent_index <= 0:
            return None
        return self.parent_node.child_nodes[self.parent_index - 1]

    @property
    def next_sibling(self):
        if self.parent_node is None:
            return None
        assert isinstance(self.parent_index, int)
        try:
            return self.parent_node.child_nodes[self.parent_index + 1]
        except IndexError:
            return None
        
    @property
    def root(self):
        if self.parent_node is None:
            return self
        return self.parent_node.root
    
    @property
    def file_path(self):
        return f'{self.root.file}:{self.line}:{self.column}'


def parse_xml(document, *, is_file=False):
    root = None
    parent = None

    filename = document
    if not is_file:
        filename = f'document:{hash(document)}'

    def on_xml_root_start(name, attributes):
        nonlocal root
        nonlocal parent
        nonlocal xml_element_start_parser
        nonlocal parser
        root = parent = Node(name, None, 'element', attributes)
        setattr(root, 'file', filename)
        setattr(root, 'line', parser.CurrentLineNumber)
        setattr(root, 'column', parser.CurrentColumnNumber)
        setattr(root, 'file_offset', parser.CurrentByteIndex)
        xml_element_start_parser = on_xml_non_root_start

    def on_xml_non_root_start(name, attributes):
        nonlocal parent
        nonlocal parser
        element = Node(name, None, 'element', attributes)
        setattr(element, 'line', parser.CurrentLineNumber)
        setattr(element, 'column', parser.CurrentColumnNumber)
        setattr(element, 'file_offset', parser.CurrentByteIndex)
        parent.append_child(element)
        parent = element

    def on_xml_element_end(name):
        nonlocal parent
        assert parent is not None and isinstance(parent, Node)
        assert parent.node_name == name
        parent = parent.parent_node

    def on_xml_character_data(data):
        nonlocal parent
        nonlocal parser
        node = Node('#text', data, 'text')
        setattr(node, 'line', parser.CurrentLineNumber)
        setattr(node, 'column', parser.CurrentColumnNumber)
        setattr(node, 'file_offset', parser.CurrentByteIndex)
        parent.append_child(node)

    def on_xml_element_start(*args, **kwargs):
        nonlocal xml_element_start_parser
        return xml_element_start_parser(*args, **kwargs)

    xml_element_start_parser = on_xml_root_start
    parser = expat.ParserCreate(encoding='utf-8')
    parser.StartElementHandler = on_xml_element_start
    parser.EndElementHandler = on_xml_element_end
    parser.CharacterDataHandler = on_xml_character_data
    
    if is_file:
        with open(document, 'rb') as file:
            parser.ParseFile(file)
    else:
        parser.Parse(document)
    
    return root

def get_error_prefix(node):
    while node.parent_node is not None:
        node = node.parent_node
    return f'XMLError in {node.file}'