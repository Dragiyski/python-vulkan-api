import re
import pycparser
import pycparser.c_ast
import pycparser.c_generator
from .xml_parser import Node, parse_xml
from .code import get_preprocessor_lines
from .platform import basic_ctypes, platform_ctypes, object_macro_map, func_macro_map, ctypes_map, handle_type_map, CType, CComplexType, CFunctionPointerType


class Generator:
    class Error(RuntimeError):
        def __init__(self, *args, **kwargs):
            super().__init__(*args)
            self.__dict__.update(**kwargs)

    class Code(pycparser.c_ast.Node):
        __slots__ = ('code', 'coord', '__weakref__')

        def __init__(self, code):
            self.code = code

    class CGenerator(pycparser.c_generator.CGenerator):
        def visit_Code(self, node):
            return node.code

    def __init__(self):
        self.ctypes_map = {**basic_ctypes, **platform_ctypes}

        class CParser(pycparser.CParser):
            def _lex_type_lookup_func(parser, name):
                if super()._lex_type_lookup_func(name):
                    return True
                return name in self.ctypes_map

        self.object_macro_map = dict(object_macro_map)
        self.func_macro_map = dict(func_macro_map)
        self.root_node_list = []
        self.alias_map = {}
        self.value_map = {}
        self.value_enum_map = {}
        self.enum_node_map = {}
        self.enums_node_map = {}
        self.value_node_map = {}
        self.bitmask_node_map = {}
        self.handle_node_map = {}
        self.struct_node_map = {}
        self.union_node_map = {}
        self.callback_node_map = {}
        self.command_node_map = {}
        self.enum_value_map = {}
        self.const_map = {}
        self.bit_map = {}
        self.cparser = CParser()
        self.cgenerator = Generator.CGenerator()

    def make_path(self, node):
        names = []
        while node is not None:
            names.append('<%s>' % node.node_name)
            node = node.parent_node
        return '/'.join(names)

    def multiple_children_error(self, node, child_name):
        child_count = len(node.children[child_name])
        return Generator.Error('In %s: Expected a single child <%s>, but found %d children' % (self.make_path(node), child_name, child_count), node=node)

    def get_node_name(self, node):
        if node.has_attribute('name'):
            return node.get_attribute('name')
        if 'name' in node.children:
            if len(node.children['name']) > 1:
                raise self.multiple_children_error(node, 'name')
            return node.get('name').get_text()
        raise Generator.Error('In %s: Missing name' % self.make_path(node), node=node)

    def get_node_name_from_children(self, node):
        if 'name' not in node.children:
            raise Generator.Error('In %s: Missing child <name>' % self.make_path(node), node=node)
        if len(node.children['name']) > 1:
            raise self.multiple_children_error(node, 'name')
        return node.get('name').get_text()

    def get_node_name_from_attribute(self, node):
        if not node.has_attribute('name'):
            raise Generator.Error('In %s: Missing attribute @name' % self.make_path(node), node=node)
        return node.get_attribute('name')

    def save_alias(self, name, alias):
        if name in self.alias_map:
            if self.alias_map[name] != alias:
                raise Generator.Error('Duplicate alias "%s": The referred alias "%s" does not match previously defined value "%s"' % (name, alias, self.alias_map[alias]))
        else:
            self.alias_map[name] = alias

    def save_node_in_map(self, target_map, name, node):
        if name in target_map:
            map_name = None
            for key in dir(self):
                if getattr(self, key) is target_map:
                    map_name = key
                    break
            else:
                raise Generator.Error('In %s: Duplicate key "%s"' % (self.make_path(node), name), node=node)
            raise Generator.Error('In %s: Duplicate key "%s" in self.%s' % (self.make_path(node), name, map_name), node=node)
        target_map[name] = node

    def save_value_in_map(self, target_map, name, value):
        if name in target_map:
            map_name = None
            for key in dir(self):
                if getattr(self, key) is target_map:
                    map_name = key
                    break
            else:
                raise Generator.Error('Duplicate key "%s"' % (name))
            raise Generator.Error('Duplicate key "%s" in self.%s' % (name, map_name))
        target_map[name] = value

    def process_alias_node(self, node):
        assert node.has_attribute('alias')
        name = self.get_node_name_from_attribute(node)
        alias = node.get_attribute('alias')
        self.save_alias(name, alias)

    def add_xml_file(self, file):
        root_node = parse_xml(file, is_file=True)
        self.root_node_list.append(root_node)

        for types_node in root_node.get_all('types'):
            for type_node in types_node.get_all('type'):
                category = type_node.get_attribute('category')
                if category == 'define':
                    name = self.get_node_name(type_node)
                    code = type_node.get_text()
                    code = get_preprocessor_lines(code)
                    if len(code) > 1:
                        continue
                        # raise Generator.Error('In %s: found %d preprocessor lines in <type category="define">' % (self.make_path(type_node), len(code)))
                    if len(code) < 1:
                        # Note: Some <type category="define"> nodes might be present but commented out.
                        continue
                    code = code[0]
                    func_macro = re.fullmatch(r'\s*#\s*define\s+(\w+)\(([^)]+)\)(.*)', code)
                    if func_macro is not None:
                        macro_name = func_macro.group(1)
                        if macro_name != name:
                            raise Generator.Error('In %s: Parsing definition "%s" found a macro with different name "%s"' % (self.make_path(type_node), name, macro_name))
                        args = [arg.strip() for arg in func_macro.group(2).split(',')]
                        code = func_macro.group(3)
                        code = [re.split(r'\b', x) for x in code.split('##')]
                        template = []
                        for words in code:
                            for word in words:
                                template.append(word)
                        index = 0
                        while index < len(template):
                            word = template[index]
                            if word in args:
                                if index > 0 and template[index - 1] == '#':
                                    template[index] = {
                                        'name': word,
                                        'index': args.index(word),
                                        'string': True
                                    }
                                    template.pop(index - 1)
                                    continue
                                template[index] = {
                                    'name': word,
                                    'index': args.index(word),
                                    'string': False
                                }
                            index += 1
                        if name in self.func_macro_map or name in self.object_macro_map:
                            raise Generator.Error('In %s: Duplicate preprocessor #define "%s"' % (self.make_path(type_node), name))
                        self.func_macro_map[name] = {
                            'arguments': args,
                            'template': template
                        }
                    else:
                        object_macro = re.fullmatch('\s*#\s*define\s+(\w+)\s+(.*)', code)
                        if object_macro is None:
                            raise Generator.Error('In %s: Unable to parse preprocessor #define' % (self.make_path(type_node)))
                        macro_name = object_macro.group(1)
                        if macro_name != name:
                            raise Generator.Error('In %s: Parsing definition "%s" found a macro with different name "%s"' % (self.make_path(type_node), name, macro_name))
                        code = object_macro.group(2)
                        if name in self.func_macro_map or name in self.object_macro_map:
                            raise Generator.Error('In %s: Duplicate preprocessor #define "%s"' % (self.make_path(type_node), name))
                        self.object_macro_map[name] = code
                    continue

                elif category == 'basetype':
                    if type_node.has_attribute('alias'):
                        self.process_alias_node(type_node)
                    else:
                        name = self.get_node_name(type_node)
                        if name in self.ctypes_map:
                            continue
                        words = [x.strip() for x in re.split(r'\b', ''.join([x.node_value for x in type_node.get_text_nodes_before(type_node.get('name'))]))]
                        words = [x for x in words if x]
                        if 'typedef' not in words:
                            if words[-1] == 'struct':
                                self.ctypes_map[name] = CType()
                                continue
                            raise Generator.Error('In %s: Basetype "%s" not a typedef or struct' % (self.make_path(type_node), name))
                        words = words[len(words) - words[::-1].index('typedef'):]
                        ctype = ' '.join(words).strip()
                        ptr_count = 0
                        while ctype.endswith('*'):
                            ctype = ctype[:-1].strip()
                            ptr_count += 1
                        if 'struct' in words:
                            ctype = CType()
                        elif ctype in self.ctypes_map:
                            ctype = self.ctypes_map[ctype]
                        else:
                            raise Generator.Error('In %s: Basetype "%s" is a typedef to an unknown type "%s"' % (self.make_path(type_node), name, ctype))
                        while ptr_count > 0:
                            ctype = ctype.pointer()
                            ptr_count -= 1
                        self.ctypes_map[name] = ctype
                        continue

                # Note on bitmask: The bitmask define a type and potential aliases, but they do not define any values.
                # The values are defined by enum name referred by <enums type="bitmask"> node.
                # For example: <type category="bitmask" requires="VkQueryControlFlagBits">...<name>VkQueryControlFlags</name></type>
                # "VkQueryControlFlags" is a type, but not enum. An enum "VkQueryControlFlagBits" defines the values:
                # There will be <type name="VkQueryControlFlagBits" category="enum"/>
                # And there will be <enums name="VkQueryControlFlagBits" type="bitmask">
                # Not every mask will have associated enum to it (some bitmask are types with no bits, but reserved for future use)
                # When it has bits they will be defined in @bitvalues or @requires attribute, specifying enum name

                elif category == 'bitmask':
                    if type_node.has_attribute('alias'):
                        self.process_alias_node(type_node)
                    else:
                        name = self.get_node_name_from_children(type_node)
                        self.save_node_in_map(self.bitmask_node_map, name, type_node)

                elif category == 'handle':
                    if type_node.has_attribute('alias'):
                        self.process_alias_node(type_node)
                    else:
                        name = self.get_node_name_from_children(type_node)
                        self.save_node_in_map(self.handle_node_map, name, type_node)

                elif category == 'enum':
                    if type_node.has_attribute('alias'):
                        self.process_alias_node(type_node)
                    else:
                        name = self.get_node_name_from_attribute(type_node)
                        self.save_node_in_map(self.enum_node_map, name, type_node)

                elif category == 'struct':
                    if type_node.has_attribute('alias'):
                        self.process_alias_node(type_node)
                    else:
                        name = self.get_node_name_from_attribute(type_node)
                        self.save_node_in_map(self.struct_node_map, name, type_node)

                elif category == 'union':
                    if type_node.has_attribute('alias'):
                        self.process_alias_node(type_node)
                    else:
                        name = self.get_node_name_from_attribute(type_node)
                        self.save_node_in_map(self.union_node_map, name, type_node)

                elif category == 'funcpointer':
                    if type_node.has_attribute('alias'):
                        self.process_alias_node(type_node)
                    else:
                        name = self.get_node_name_from_children(type_node)
                        self.save_node_in_map(self.callback_node_map, name, type_node)

        for enums_node in root_node.get_all('enums'):
            enums_name = self.get_node_name_from_attribute(enums_node)
            enums_type = enums_node.get_attribute('type')
            if enums_type in ['enum', 'bitmask']:
                is_in_enum = True
            elif enums_type is None:
                is_in_enum = False
            else:
                raise Generator.Error('In %s: Enum values for name "%s" is of unknown type "%s"' % (self.make_path(enums_node), enums_name, enums_type))
            for enum_node in enums_node.get_all('enum'):
                enum_name = self.get_node_name_from_attribute(enum_node)
                if enum_node.has_attribute('alias'):
                    self.process_alias_node(enum_node)
                else:
                    if enum_name in self.enum_value_map:
                        raise Generator.Error('In %s: Duplicate <enums> with name "%s"' % enum_name)
                    self.enum_value_map[enum_name] = {
                        'value_node': enum_node
                    }
                    if is_in_enum:
                        self.enum_value_map[enum_name]['enum_node'] = enums_node
                        self.enum_value_map[enum_name]['enum_name'] = enums_name
            self.save_node_in_map(self.enums_node_map, enums_name, enums_node)

        for commands_node in root_node.get_all('commands'):
            for command_node in commands_node.get_all('command'):
                if command_node.has_attribute('alias'):
                    self.process_alias_node(command_node)
                else:
                    if 'proto' not in command_node.children:
                        raise Generator.Error('In %s: Missing child <proto>' % self.make_path(command_node), node=command_node)
                    if len(command_node.children['proto']) > 1:
                        raise self.multiple_children_error(command_node, 'proto')
                    proto_node = command_node.get('proto')
                    name = self.get_node_name_from_children(proto_node)
                    self.save_node_in_map(self.command_node_map, name, command_node)

    def compile(self):
        self.compile_handle_node_map()
        self.compile_enum_node_map()
        self.compile_enum_value_map()
        self.compile_feature_enum_values()
        # feature nodes have two major roles:
        # - organize everything specified in <types> and <enums> into relevant block for the specified version.
        # For exmaple: VK_VERSION_1_0 will include everything in the core vulkan API, VK_VERSION_1_1 will include only stuff
        # defined from API version 1.1.0 forward, etc.
        # - feature will perform the same task as extension, extending certain values only specified in that version and referenced by extensions.
        # For exmaple: VK_FORMAT_G8B8G8R8_422_UNORM will be defined in feature as:
        # <enum extends="VkFormat" extnumber="157" offset="0" name="VK_FORMAT_G8B8G8R8_422_UNORM"/>
        # and in extension as:
        # <enum extends="VkFormat" name="VK_FORMAT_G8B8G8R8_422_UNORM_KHR" alias="VK_FORMAT_G8B8G8R8_422_UNORM"/>
        #
        # This will happen often, as Vulkan minor version often adapt something previously specified as an extension,
        # in this case VK_KHR_sampler_ycbcr_conversion defining YcBcR color space as extension becomes supported natively in version 1.1.
        # The value is preserved, the suffixed name is preserved as alias to non-suffixed name.

        self.compile_ext_enum_values()

    def compile_handle_node_map(self):
        for name, node in self.handle_node_map.items():
            typedef = node.get('type').get_text()
            ctype = handle_type_map[typedef]
            self.save_value_in_map(self.ctypes_map, name, ctype)

    def compile_enum_value_map(self):
        for name, source_map in self.enum_value_map.items():
            value = self.get_enum_value(source_map['value_node'])
            if 'enum_node' not in source_map:
                node = source_map['value_node']
                ctype = node.get_attribute('type')
                if ctype is None:
                    raise Generator.Error('Missing type for const node "%s"' % (name))
                if ctype not in basic_ctypes:
                    raise Generator.Error('Invalid type "%s" for const node "%s", not in basic C types' % (ctype, name))
                ctype = basic_ctypes[ctype]
                value = ctype.make_python_value(value)
            else:
                assert 'enum_name' in source_map
                assert source_map['enum_name'] in self.ctypes_map
                self.ctypes_map[source_map['enum_name']].make_python_value(value)
                self.value_enum_map[name] = source_map['enum_name']
            source_map['value'] = value
            self.save_value_in_map(self.value_map, name, value)

    def compile_enum_node_map(self):
        for name, node in self.bitmask_node_map.items():
            if 'type' not in node.children:
                raise Generator.Error('In %s: Missing child <type>' % self.make_path(node), node=node)
            if len(node.children['type']) > 1:
                raise self.multiple_children_error(node, 'type')
            ctype = node.get('type').get_text()
            if ctype not in self.ctypes_map:
                raise Generator.Error('In %s, name="%s": Child <type> not in the basetypes' % (self.make_path(node), name), node=node)
            ctype = self.ctypes_map[ctype]
            self.save_value_in_map(self.ctypes_map, name, ctype)
            bit_name = None
            if node.has_attribute('bitvalues'):
                bit_name = node.get_attribute('bitvalues')
            elif node.has_attribute('requires'):
                bit_name = node.get_attribute('requires')
            if bit_name is not None:
                if bit_name in self.bit_map:
                    raise Generator.Error('In %s, name="%s": Bitmask assigns "%s" enum, already assigned by another bitmask "%s"' % (self.make_path(node), name, bit_name, bit_map[bit_name]))
                self.bit_map[bit_name] = name
        for name, node in self.enum_node_map.items():
            if name in self.bit_map:
                assert self.bit_map[name] in self.ctypes_map
                ctype = self.ctypes_map[self.bit_map[name]]
            else:
                ctype = ctypes_map['c_int']
            assert isinstance(ctype, CType)
            self.save_value_in_map(self.ctypes_map, name, ctype)
    
    def compile_feature_enum_values(self):
        for root_node in self.root_node_list:
            for feature_node in root_node.get_all('feature'):
                feature_name = self.get_node_name_from_attribute(feature_node)
                for require_node in feature_node.get_all('require'):
                    for enum_node in require_node.get_all('enum'):
                        if enum_node.has_attribute('alias'):
                            self.process_alias_node(enum_node)
                            continue
                        enum_name = self.get_node_name_from_attribute(enum_node)
                        extend_name = None
                        if enum_node.has_attribute('extends'):
                            extend_name = enum_node.get_attribute('extends')
                            if extend_name not in self.enum_node_map:
                                raise Generator.Error('In %s, extension "%s", enum "%s": Extending non-existent enum "%s"' % (self.make_path(enum_node), ext_name, enum_name, extend_name))
                        value = self.get_feature_enum_value(enum_node, feature_node)
                        if value is None:
                            continue
                        if enum_name in self.value_map:
                            if self.value_map[enum_name] != value:
                                raise Generator.Error('In %s, extension "%s", enum "%s" = (%r) is already defined in value map with different value (%r)' % (self.make_path(enum_node), feature_name, enum_name, value, self.value_map[enum_name]))
                            if extend_name is not None and not enum_node.has_attribute('extnumber'):
                                assert enum_name in self.enum_value_map
                                self.enum_value_map[enum_name]['value_node'] = enum_node
                                self.enum_value_map[enum_name]['feature_node'] = feature_node
                                if 'ext_node' in self.enum_value_map[enum_name]:
                                    del self.enum_value_map[enum_name]['ext_node']
                        else:
                            assert enum_name not in self.enum_value_map
                            assert enum_name not in self.value_enum_map
                            self.value_map[enum_name] = value
                            self.enum_value_map[enum_name] = {
                                'value_node': enum_node,
                                'feature_node': feature_node
                            }
                            if extend_name is not None:
                                self.enum_value_map[enum_name]['enum_name'] = extend_name
                                self.enum_value_map[enum_name]['enum_node'] = self.enum_node_map[extend_name]
                                self.value_enum_map[enum_name] = extend_name

    def compile_ext_enum_values(self):
        for root_node in self.root_node_list:
            for extensions_node in root_node.get_all('extensions'):
                for ext_node in extensions_node.get_all('extension'):
                    ext_name = self.get_node_name_from_attribute(ext_node)
                    for require_node in ext_node.get_all('require'):
                        for enum_node in require_node.get_all('enum'):
                            if enum_node.has_attribute('alias'):
                                self.process_alias_node(enum_node)
                                continue
                            enum_name = self.get_node_name_from_attribute(enum_node)
                            extend_name = None
                            if enum_node.has_attribute('extends'):
                                extend_name = enum_node.get_attribute('extends')
                                if extend_name not in self.enum_node_map:
                                    raise Generator.Error('In %s, extension "%s", enum "%s": Extending non-existent enum "%s"' % (self.make_path(enum_node), ext_name, enum_name, extend_name))
                            value = self.get_ext_enum_value(enum_node, ext_node)
                            if value is None:
                                continue
                            if enum_name in self.value_map:
                                if self.value_map[enum_name] != value:
                                    raise Generator.Error('In %s, extension "%s", enum "%s" = (%r) is already defined in value map with different value (%r)' % (self.make_path(enum_node), ext_name, enum_name, value, self.value_map[enum_name]))
                                if extend_name is not None and not enum_node.has_attribute('extnumber'):
                                    # Foreign extension reference is accepted by first extension found,
                                    # but it will be overridden if found with the extension with matching number.
                                    # For example:
                                    # <enum offset="0" extends="VkIndexType" extnumber="166" name="VK_INDEX_TYPE_NONE_KHR"/>
                                    # defined in:
                                    # <extension name="VK_KHR_acceleration_structure" number="151">
                                    # can be specified again as:
                                    # <enum offset="0" extends="VkIndexType" name="VK_INDEX_TYPE_NONE_KHR"/>
                                    # in:
                                    # <extension name="VK_NV_ray_tracing" number="166"/>
                                    # or it can be skipped, while aliased:
                                    # <enum extends="VkIndexType" name="VK_INDEX_TYPE_NONE_NV" alias="VK_INDEX_TYPE_NONE_KHR"/>
                                    # In the former case: enum_node will be overridden and extnumber node ignored.
                                    # In the latter case: enum_node with @extnumber will be stored as value_node
                                    assert enum_name in self.enum_value_map
                                    self.enum_value_map[enum_name]['value_node'] = enum_node
                                    self.enum_value_map[enum_name]['ext_node'] = ext_node
                                    if 'feature_node' in self.enum_value_map[enum_name]:
                                        del self.enum_value_map[enum_name]['feature_node']
                            else:
                                assert enum_name not in self.enum_value_map
                                assert enum_name not in self.value_enum_map
                                self.value_map[enum_name] = value
                                self.enum_value_map[enum_name] = {
                                    'value_node': enum_node,
                                    'ext_node': ext_node
                                }
                                if extend_name is not None:
                                    self.enum_value_map[enum_name]['enum_name'] = extend_name
                                    self.enum_value_map[enum_name]['enum_node'] = self.enum_node_map[extend_name]
                                    self.value_enum_map[enum_name] = extend_name

    def get_feature_enum_value(self, enum_node, feature_node):
        enum_name = self.get_node_name_from_attribute(enum_node)
        feature_name = self.get_node_name_from_attribute(feature_node)
        if enum_node.has_attribute('offset'):
            if enum_node.has_attribute('extnumber'):
                ext_number = enum_node.get_attribute('extnumber')
            else:
                raise Generator.Error('In %s, feature "%s", enum "%s" is defined as @offset, but missing extension number' % (self.make_path(enum_node), feature_name, enum_name))
            offset = self.parse_c_int(enum_node.get_attribute('offset'))
            ext_offset = (self.parse_c_int(ext_number) - 1) * 1000
            base = 1000000000
            value = base + ext_offset + offset
        elif enum_node.has_attribute('value') or enum_node.has_attribute('bitpos'):
            value = self.get_enum_value(enum_node)
        else:
            return None
        if enum_node.get_attribute('dir') == '-':
            value = -value
        return value

    def get_ext_enum_value(self, enum_node, ext_node):
        enum_name = self.get_node_name_from_attribute(enum_node)
        ext_name = self.get_node_name_from_attribute(ext_node)
        if enum_node.has_attribute('offset'):
            if enum_node.has_attribute('extnumber'):
                ext_number = enum_node.get_attribute('extnumber')
            elif ext_node.has_attribute('number'):
                ext_number = ext_node.get_attribute('number')
            else:
                raise Generator.Error('In %s, extension "%s", enum "%s" is defined as @offset, but missing extension number' % (self.make_path(enum_node), ext_name, enum_name))
            offset = self.parse_c_int(enum_node.get_attribute('offset'))
            ext_offset = (self.parse_c_int(ext_number) - 1) * 1000
            base = 1000000000
            value = base + ext_offset + offset
        elif enum_node.has_attribute('value') or enum_node.has_attribute('bitpos'):
            value = self.get_enum_value(enum_node)
        else:
            return None
        if enum_node.get_attribute('dir') == '-':
            value = -value
        return value
    
    def get_enum_value(self, node):
        if node.has_attribute('bitpos'):
            bitpos = self.parse_c_int(node.get_attribute('bitpos'))
            return 1 << bitpos
        if node.has_attribute('value'):
            value = self.get_c_constant_value('int', node.get_attribute('value'))
            return value
        raise Generator.Error('Missing enum value: Neither @value, nor @bitpos pressent')

    def preprocess_c_ast(self, node):
        has_substitution = False
        for name, child_node in node.children():
            if type(child_node) is pycparser.c_ast.ID and child_node.name in self.object_macro_map:
                setattr(node, name, Generator.Code(self.object_macro_map[child_node.name]))
                has_substitution = True
                continue
            if type(child_node) is pycparser.c_ast.FuncCall and child_node.name.name in self.func_macro_map:
                args = [self.cgenerator.visit(x) for x in child_node.args]
                macro = self.func_macro_map[child_node.name.name]
                if len(macro['arguments']) != len(args):
                    raise Generator.Error('Macro "%s" accept "%d" arguments, but called with "%d" arguments' % (child_node.name.name, len(macro['arguments'], len(args))))
                code = []
                for part in macro['template']:
                    if isinstance(part, str):
                        code.append(part)
                    else:
                        assert isinstance(part, dict)
                        code.append(args[part['index']])
                code = ''.join(code)
                setattr(node, name, Generator.Code(code))
                has_substitution = True
                continue
            has_descendant_substitution = self.preprocess_c_ast(child_node)
            has_substitution = has_substitution or has_descendant_substitution
        return has_substitution

    def preprocess_c_code(self, code):
        ast = self.cparser.parse(code)
        while self.preprocess_c_ast(ast):
            code = self.cgenerator.visit(ast)
            ast = self.cparser.parse(code)
        return code

    def get_c_constant_value(self, ctype, value):
        assert ctype in self.ctypes_map
        code = '%s value = %s;' % (ctype, value)
        code = self.preprocess_c_code(code)
        ast = self.cparser.parse(code)
        return self.get_c_ast_const_value(ast.ext[0].init)

    def get_c_ast_const_value(self, node):
        node_type = type(node)
        c_ast = pycparser.c_ast
        if node_type is c_ast.Constant:
            if 'int' in node.type:
                return self.parse_c_int(node.value)
            if node.type in ['float', 'double']:
                return self.parse_c_float(node.value)
            if node.type == 'string':
                return self.parse_c_string(node.value)
        elif node_type is c_ast.UnaryOp:
            if node.op == '~':
                return ~self.get_c_ast_const_value(node.expr)
            if node.op == '+':
                return +self.get_c_ast_const_value(node.expr)
            if node.op == '-':
                return -self.get_c_ast_const_value(node.expr)
        elif node_type is c_ast.BinaryOp:
            if node.op == '|':
                return self.get_c_ast_const_value(node.left) | self.get_c_ast_const_value(node.right)
            if node.op == '<<':
                return self.get_c_ast_const_value(node.left) << self.get_c_ast_const_value(node.right)
        elif node_type is c_ast.Cast:
            target_type = self.cgenerator.visit(node.to_type)
            assert target_type in self.ctypes_map
            value = self.get_c_ast_const_value(node.expr)
            return self.ctypes_map[target_type].make_python_value(value)

    @staticmethod
    def parse_c_int(value):
        match = re.match(r'0x([0-9A-Fa-f]+)', value)
        if match:
            return int(match.group(0), 16)
        match = re.match(r'-?[0-9]+', value)
        if match:
            return int(match.group(0), 10)
        raise ValueError('Invalid integer value: %r' % value)

    @staticmethod
    def parse_c_float(value):
        match = re.match(r'-?[0-9]+(?:\.[0-9]+)?', value)
        if match:
            return float(match.group(0))
        raise ValueError('Invalid float value: %r' % value)

    @staticmethod
    def parse_c_string(value):
        if len(value) < 2 or value[0] != '"' or value[-1] != '"':
            raise ValueError('Invalid string value (missing open or close quotes): %s' % value)
        value = value[1:-1]

        value = re.sub(r'\\U([0-9A-Fa-f]{8})', subst_unicode_hex, value)
        value = re.sub(r'\\u([0-9A-Fa-f]{4})', subst_unicode_hex, value)
        value = re.sub(r'\\x([0-9A-Fa-f]{2})', subst_unicode_hex, value)
        value = re.sub(r'\\([0-7]{3})', subst_unicode_oct, value)
        value = re.sub(r'\\(.)', subst_slash_escape, value)
        return value.encode('utf-8')


def subst_unicode_hex(match):
    return chr(int(match.group(1), 16))


def subst_unicode_oct(match):
    return chr(int(match.group(1), 8))


subst_table = {
    'a': 0x07,
    'b': 0x08,
    'e': 0x1B,
    'f': 0x0C,
    'n': 0x0A,
    'r': 0x0D,
    't': 0x09,
    'v': 0x0B,
    '\\': 0x5C,
    "'": 0x27,
    '"': 0x22,
    '?': 0x3F,
}


def subst_slash_escape(match):
    seq = match.group(1)
    if seq in subst_table:
        return chr(subst_table[seq])
    return match.group(0)
