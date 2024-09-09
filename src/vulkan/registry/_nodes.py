tags = {}
nodes = {}
category_name_map = {
    'alias': set(),
    'type': set(),
    'struct': set(),
    'union': set(),
    'define': set(),
    'enum': set(),
    'bitmask': set(),
    'value': set(),
    'handle': set(),
    'callback': set(),
    'command': set(),
}
enum_bit_map = {}
bit_enum_map = {}
enum_value_map = {}
value_enum_map = {}

def __init__():
    global tags, nodes, enum_bit_map, bit_enum_map, category_name_map
    from .repository import update as update_files
    from .xml_parser import parse_xml
    import pathlib
    from logging import getLogger
    logger = getLogger('vulkan.registry')
    registry_dir = pathlib.Path(__file__).resolve().parent
    registry_files = update_files(registry_dir)

    def append_node(name, node):
        if name not in nodes:
            nodes[name] = set()
        nodes[name].add(node)

    def is_vulkan_api(node):
        if node.has_attribute('api'):
            api_set = { x.strip().lower() for x in node.get_attribute('api').split(',') }
            if 'vulkan' not in api_set:
                return False
        return True

    for registry_file in registry_files:
        xml = parse_xml(registry_file, is_file=True)
        # parse (vendor) tags separately
        # parse all type
        for tags_node in xml.get_all('tags'):
            for tag_node in tags_node.get_all('tag'):
                if not is_vulkan_api(tag_node):
                    continue
                if not tag_node.has_attribute('name'):
                    logger.warning(f'xml:{tag_node.file_path}: skipping, missing attribute @name')
                    continue
                name = tag_node.get_attribute('name')
                if name not in nodes:
                    tags[name] = set()
                tags[name].add(tag_node)
        for types_node in xml.get_all('types'):
            if not is_vulkan_api(types_node):
                continue
            for type_node in types_node.get_all('type'):
                if not is_vulkan_api(type_node):
                    continue
                category = None
                if type_node.has_attribute('category'):
                    category = type_node.get_attribute('category')
                # Exclude categories that do not define vulkan names
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
                    category_name_map['alias'].add(name)
                else:
                    if category == 'bitmask':
                        mask_name = None
                        if type_node.has_attribute('bitvalues'):
                            mask_name = type_node.get_attribute('bitvalues')
                        elif type_node.has_attribute('requires'):
                            mask_name = type_node.get_attribute('requires')
                        if mask_name is not None:
                            if name in enum_bit_map and enum_bit_map[name] != mask_name:
                                logger.warning(f'xml:{type_node.file_path}: bitmask {name!r} refer to bits {mask_name!r}, but reference to different bits already exists: {enum_bit_map[name]!r}')
                            else:
                                enum_bit_map[name] = mask_name
                            if mask_name in bit_enum_map and bit_enum_map[mask_name] != name:
                                logger.warning(f'xml:{type_node.file_path}: bits {mask_name!r} refer to enum {name!r}, but reference to different enum already exists: {bit_enum_map[mask_name]!r}')
                            else:
                                bit_enum_map[mask_name] = name
                        category_name_map['bitmask'].add(name)
                    elif category == 'funcpointer':
                        category_name_map['callback'].add(name)
                    elif category in ['struct', 'union', 'enum', 'handle', 'define']:
                        category_name_map[category].add(name)
                append_node(name, type_node)
        for enums_node in xml.get_all('enums'):
            if not is_vulkan_api(enums_node):
                continue
            enum_name = None
            if enums_node.has_attribute('name') and (enums_node.has_attribute('alias') or enums_node.has_attribute('type') and enums_node.get_attribute('type') in ['enum', 'bitmask']):
                enum_name = enums_node.get_attribute('name')
                if enums_node.has_attribute('alias'):
                    category_name_map['alias'].add(enum_name)
                else:
                    category_name_map['enum'].add(enum_name)
                    category_name_map['type'].add(enum_name)
                    if enum_name not in enum_value_map:
                        enum_value_map[enum_name] = set()
                append_node(enum_name, enums_node)
            for enum_node in enums_node.get_all('enum'):
                if not is_vulkan_api(enum_node):
                    continue
                if not enum_node.has_attribute('name'):
                    logger.warning(f'xml:{enum_node.file_path}: skipping, missing attribute @name')
                    continue
                name = enum_node.get_attribute('name')
                if type_node.has_attribute('alias'):
                    category_name_map['alias'].add(name)
                else:
                    category_name_map['value'].add(name)
                if enum_name is not None:
                    enum_value_map[enum_name].add(name)
                    value_enum_map[name] = enum_name
                append_node(name, enum_node)
        for commands_node in xml.get_all('commands'):
            if not is_vulkan_api(commands_node):
                continue
            for command_node in commands_node.get_all('command'):
                if not is_vulkan_api(command_node):
                    continue
                if command_node.has_attribute('name'):
                    name = command_node.get_attribute('name')
                elif 'proto' in command_node.children and 'name' in command_node.get('proto').children:
                    name = command_node.get('proto').get('name').get_text()
                else:
                    logger.warning(f'xml:{command_node.file_path}: skipping, missing attribute @name or child <name>')
                    continue
                if command_node.has_attribute('alias'):
                    category_name_map['alias'].add(name)
                else:
                    category_name_map['command'].add(name)
                append_node(name, command_node)
        for feature_node in xml.get_all('feature'):
            if not is_vulkan_api(feature_node):
                continue
            for require_node in feature_node.get_all('require'):
                if not is_vulkan_api(require_node):
                    continue
                for node_type in ['type', 'enum', 'command']:
                    for node in require_node.get_all(node_type):
                        if not is_vulkan_api(node):
                            continue
                        if not node.has_attribute('name'):
                            logger.warning(f'xml:{node.file_path}: skipping, missing attribute @name')
                            continue
                        name = node.get_attribute('name')
                        if node.has_attribute('alias') or name in category_name_map['alias']:
                            category_name_map['alias'].add(name)
                            if node_type == 'enum':
                                alias_name = node.get_attribute('alias')
                                if alias_name in value_enum_map:
                                    value_enum_map[name] = value_enum_map[alias_name]
                                    enum_value_map[value_enum_map[alias_name]].add(name)
                        elif node_type == 'enum':
                            category_name_map['value'].add(name)
                            if node.has_attribute('extends'):
                                enum_name = node.get_attribute('extends')
                                if enum_name not in enum_value_map:
                                    enum_value_map[enum_name] = set()
                                enum_value_map[enum_name].add(name)
                        append_node(name, node)
                    
        for extensions_node in xml.get_all('extensions'):
            if not is_vulkan_api(extensions_node):
                continue
            for extension_node in extensions_node.get_all('extension'):
                if not is_vulkan_api(extension_node):
                    continue
                for require_node in extension_node.get_all('require'):
                    if not is_vulkan_api(require_node):
                        continue
                    for node_type in ['type', 'enum', 'command']:
                        for node in require_node.get_all(node_type):
                            if not is_vulkan_api(node):
                                continue
                            if not node.has_attribute('name'):
                                logger.warning(f'xml:{node.file_path}: skipping, missing attribute @name')
                                continue
                            name = node.get_attribute('name')
                            if node.has_attribute('alias') or name in category_name_map['alias']:
                                category_name_map['alias'].add(name)
                                if node_type == 'enum':
                                    alias_name = node.get_attribute('alias')
                                    if alias_name in value_enum_map:
                                        value_enum_map[name] = value_enum_map[alias_name]
                                        enum_value_map[value_enum_map[alias_name]].add(name)
                            elif node_type == 'enum':
                                category_name_map['value'].add(name)
                                if node.has_attribute('extends'):
                                    enum_name = node.get_attribute('extends')
                                    if enum_name not in enum_value_map:
                                        enum_value_map[enum_name] = set()
                                    enum_value_map[enum_name].add(name)
                            append_node(name, node)

__init__()
del __init__
