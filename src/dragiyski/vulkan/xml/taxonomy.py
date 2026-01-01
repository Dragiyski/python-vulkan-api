from logging import getLogger
from pathlib import Path
from .node import Node, parse_xml

logger = getLogger('vulkan.registry')

_default_files = [
    Path(__file__).resolve().parent.joinpath('registry', 'vk.xml'),
    Path(__file__).resolve().parent.joinpath('registry', 'video.xml'),
]


class _TaxonomyDefault:
    __slots__ = tuple()

    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        value = instance(*_default_files)
        setattr(instance, 'default', value)
        return value


class _TaxonomyType(type):
    default = _TaxonomyDefault()


class Taxonomy(metaclass=_TaxonomyType):
    def __init__(self, *entries):
        self.tags = {}
        self.nodes = {}
        self.category = {
            'alias': set(),
            'type': set(),
            'external_type': set(),
            'basetype': set(),
            'struct': set(),
            'union': set(),
            'complex': set(),
            'define': set(),
            'enum': set(),
            'bitmask': set(),
            'value': set(),
            'handle': set(),
            'callback': set(),
            'command': set(),
        }
        self.group_bit_map = {}
        self.bit_group_map = {}
        self.group_value_map = {}
        self.value_group_map = {}

        for entry in entries:
            if isinstance(entry, str):
                entry = Path(entry).resolve()
            if isinstance(entry, Path):
                entry = parse_xml(entry, is_file=True)
            if not isinstance(entry, Node):
                raise ValueError('Expected `entry` to be a `str`, `pathlib.Path` or `Node` instance')
            self.add_root(entry)

    def register_node(self, name: str, node: Node):
        if name not in self.nodes:
            self.nodes[name] = set()
        self.nodes[name].add(node)

    @staticmethod
    def is_vulkan_api(node: Node) -> bool:
        if node.has_attribute('api'):
            api_set = {x.strip().lower() for x in node.get_attribute('api').split(',')}
            if 'vulkan' not in api_set:
                return False
        return True

    def finalize(self):
        self.category['enum'].difference_update(self.bit_group_map.keys())

    def add_root(self, root: Node):
        for tags_node in root.get_all('tags'):
            for tag_node in tags_node.get_all('tag'):
                if not self.is_vulkan_api(tag_node):
                    continue
                if not tag_node.has_attribute('name'):
                    logger.warning(f'xml:{tag_node.file_path}: skipping, missing attribute @name')
                    continue
                name = tag_node.get_attribute('name')
                if name not in self.tags:
                    self.tags[name] = set()
                self.tags[name].add(tag_node)
        for types_node in root.get_all('types'):
            if not self.is_vulkan_api(types_node):
                continue
            for type_node in types_node.get_all('type'):
                if not self.is_vulkan_api(type_node):
                    continue
                category = None
                if type_node.has_attribute('category'):
                    category = type_node.get_attribute('category')
                if category == 'include':
                    continue
                if type_node.has_attribute('name'):
                    name = type_node.get_attribute('name')
                elif 'name' in type_node.children:
                    name = type_node.get('name').get_text()
                else:
                    logger.warning(f'xml:{tag_node.file_path}: skipping, missing attribute @name or child <name>')
                    continue
                if type_node.has_attribute('alias'):
                    self.category['alias'].add(name)
                else:
                    if category == 'bitmask':
                        mask_name = None
                        if type_node.has_attribute('bitvalues'):
                            mask_name = type_node.get_attribute('bitvalues')
                        elif type_node.has_attribute('requires'):
                            mask_name = type_node.get_attribute('requires')
                        if mask_name is not None:
                            if name in self.group_bit_map and self.group_bit_map[name] != mask_name:
                                logger.warning(f'xml:{type_node.file_path}: bitmask {name!r} refer to bits {mask_name!r}, but reference to different bits already exists: {self.group_bit_map[name]!r}')
                            else:
                                self.group_bit_map[name] = mask_name
                            if mask_name in self.bit_group_map and self.bit_group_map[mask_name] != name:
                                logger.warning(f'xml:{type_node.file_path}: bits {mask_name!r} refer to enum {name!r}, but reference to different enum already exists: {self.bit_group_map[mask_name]!r}')
                            else:
                                self.bit_group_map[mask_name] = name
                        self.category['bitmask'].add(name)
                    elif category == 'funcpointer':
                        self.category['callback'].add(name)
                    elif category in ['struct', 'union', 'enum', 'handle', 'define', 'basetype']:
                        self.category[category].add(name)
                    elif category is None:
                        self.category['external_type'].add(name)
                    if category in ['struct', 'union']:
                        self.category['complex'].add(name)
                self.register_node(name, type_node)
        for enums_node in root.get_all('enums'):
            if not self.is_vulkan_api(enums_node):
                continue
            enum_name = None
            if enums_node.has_attribute('name') and (enums_node.has_attribute('alias') or enums_node.has_attribute('type') and enums_node.get_attribute('type') in ['enum', 'bitmask']):
                enum_name = enums_node.get_attribute('name')
                if enums_node.has_attribute('alias'):
                    self.category['alias'].add(enum_name)
                else:
                    self.category['enum'].add(enum_name)
                    self.category['type'].add(enum_name)
                    if enum_name not in self.group_value_map:
                        self.group_value_map[enum_name] = set()
                self.register_node(enum_name, enums_node)
            for enum_node in enums_node.get_all('enum'):
                if not self.is_vulkan_api(enum_node):
                    continue
                if not enum_node.has_attribute('name'):
                    logger.warning(f'xml:{enum_node.file_path}: skipping, missing attribute @name')
                    continue
                name = enum_node.get_attribute('name')
                if enum_node.has_attribute('alias'):
                    self.category['alias'].add(name)
                else:
                    self.category['value'].add(name)
                if enum_name is not None:
                    if enum_name not in self.group_value_map:
                        self.group_value_map[enum_name] = set()
                    self.group_value_map[enum_name].add(name)
                    self.value_group_map[name] = enum_name
                self.register_node(name, enum_node)
        for commands_node in root.get_all('commands'):
            if not self.is_vulkan_api(commands_node):
                continue
            for command_node in commands_node.get_all('command'):
                if not self.is_vulkan_api(command_node):
                    continue
                if command_node.has_attribute('name'):
                    name = command_node.get_attribute('name')
                elif 'proto' in command_node.children and 'name' in command_node.get('proto').children:
                    name = command_node.get('proto').get('name').get_text()
                else:
                    logger.warning(f'xml:{command_node.file_path}: skipping, missing attribute @name or child <name>')
                    continue
                if command_node.has_attribute('alias'):
                    self.category['alias'].add(name)
                else:
                    self.category['command'].add(name)
                self.register_node(name, command_node)
        for feature_node in root.get_all('feature'):
            if not self.is_vulkan_api(feature_node):
                continue
            for require_node in feature_node.get_all('require'):
                if not self.is_vulkan_api(require_node):
                    continue
                for node_type in ['type', 'enum', 'command']:
                    for node in require_node.get_all(node_type):
                        if not self.is_vulkan_api(node):
                            continue
                        if not node.has_attribute('name'):
                            logger.warning(f'xml:{node.file_path}: skipping, missing attribute @name')
                            continue
                        name = node.get_attribute('name')
                        if node.has_attribute('alias') or name in self.category['alias']:
                            self.category['alias'].add(name)
                            if node_type == 'enum':
                                alias_name = node.get_attribute('alias')
                                if alias_name in self.value_group_map:
                                    self.value_group_map[name] = self.value_group_map[alias_name]
                                    self.group_value_map[self.value_group_map[alias_name]].add(name)
                        elif node_type == 'enum':
                            self.category['value'].add(name)
                            if node.has_attribute('extends'):
                                enum_name = node.get_attribute('extends')
                                if enum_name not in self.group_value_map:
                                    self.group_value_map[enum_name] = set()
                                self.group_value_map[enum_name].add(name)
                                self.value_group_map[name] = enum_name
                        self.register_node(name, node)
        for extensions_node in root.get_all('extensions'):
            if not self.is_vulkan_api(extensions_node):
                continue
            for extension_node in extensions_node.get_all('extension'):
                if not self.is_vulkan_api(extension_node):
                    continue
                for require_node in extension_node.get_all('require'):
                    if not self.is_vulkan_api(require_node):
                        continue
                    for node_type in ['type', 'enum', 'command']:
                        for node in require_node.get_all(node_type):
                            if not self.is_vulkan_api(node):
                                continue
                            if not node.has_attribute('name'):
                                logger.warning(f'xml:{node.file_path}: skipping, missing attribute @name')
                                continue
                            name = node.get_attribute('name')
                            if node.has_attribute('alias') or name in self.category['alias']:
                                self.category['alias'].add(name)
                                if node_type == 'enum':
                                    alias_name = node.get_attribute('alias')
                                    if alias_name in self.value_group_map:
                                        self.value_group_map[name] = self.value_group_map[alias_name]
                                        self.group_value_map[self.value_group_map[alias_name]].add(name)
                            elif node_type == 'enum':
                                self.category['value'].add(name)
                                if node.has_attribute('extends'):
                                    enum_name = node.get_attribute('extends')
                                    if enum_name not in self.group_value_map:
                                        self.group_value_map[enum_name] = set()
                                    self.group_value_map[enum_name].add(name)
                                    self.value_group_map[name] = enum_name
                            self.register_node(name, node)
