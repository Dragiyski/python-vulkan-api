import re
import os
import pycparser
import pycparser.c_ast
import pycparser.c_generator
from .xml_parser import Node, parse_xml
from .code import get_preprocessor_lines
from .platform import basic_ctypes, platform_ctypes, object_macro_map, func_macro_map, ctypes_map, handle_type_map, CType, CPointerType, CComplexType, CArrayType, CFunctionType


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
                while name in self.alias_map:
                    name = self.alias_map[name]
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
        self.uncategorized_types = set()
        self.complex_type_node_map = {}
        self.callback_node_map = {}
        self.command_node_map = {}
        self.enum_value_map = {}
        self.const_map = {}
        self.bit_map = {}
        self.resolving_complex_type = set()
        self.delayed_complex_type = set()
        self.cparser = CParser()
        self.cgenerator = Generator.CGenerator()

    def make_path(self, node):
        names = []
        while node is not None:
            exposed_attr = []
            if node.has_attribute('category'):
                exposed_attr.append('category="%s"' % node.get_attribute('category'))
            if node.has_attribute('name'):
                exposed_attr.append('name="%s"' % node.get_attribute('name'))
            if node.has_attribute('alias'):
                exposed_attr.append('alias="%s"' % node.get_attribute('alias'))
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
                elif category is None:
                    if type_node.has_attribute('alias'):
                        self.process_alias_node(type_node)
                    else:
                        name = self.get_node_name_from_attribute(type_node)
                        self.uncategorized_types.add(name)

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
                        self.save_node_in_map(self.complex_type_node_map, name, type_node)

                elif category == 'union':
                    if type_node.has_attribute('alias'):
                        self.process_alias_node(type_node)
                    else:
                        name = self.get_node_name_from_attribute(type_node)
                        self.save_node_in_map(self.complex_type_node_map, name, type_node)

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
        self.compile_ext_enum_values()
        self.compile_callback_node_map()
        self.compile_uncategorized_types()
        self.compile_complex_type_node_map()
        self.resolve_callback_type_map()
        self.compile_commands()
        self.resolve_enums()

    def resolve_enums(self):
        self.value_type_map = {}
        for name, value in self.value_enum_map.items():
            if value not in self.value_type_map:
                self.value_type_map[value] = {}
            value_type_map = self.value_type_map[value]
            assert name not in value_type_map
            value_type_map[name] = self.value_map[name]
        self.enum_type_map = {}
        self.bitmask_type_map = {}
        for enums_name, enums_node in self.enums_node_map.items():
            if enums_node.has_attribute('type'):
                enum_type = enums_node.get_attribute('type')
            else:
                enum_type = None
            if enum_type == 'enum':
                if enums_name in self.value_type_map:
                    value_map = self.enum_type_map[enums_name] = self.value_type_map[enums_name]
            elif enum_type == 'bitmask':
                if enums_name in self.value_type_map:
                    value_map = self.bitmask_type_map[enums_name] = self.value_type_map[enums_name]
            else:
                for enum_node in enums_node.get_all('enum'):
                    enum_name = enum_node.get_attribute('name')
                    if enum_node.has_attribute('alias'):
                        self.const_map[enum_name] = enum_node.get_attribute('alias')
                    else:
                        assert enum_node.has_attribute('type')
                        ctype = self.ctypes_map[enum_node.get_attribute('type')]
                        self.const_map[enum_name] = {
                            'value': self.value_map[enum_name],
                            'ctype': ctype
                        }
                continue
            for enum_node in enums_node.get_all('enum'):
                if enum_node.has_attribute('alias'):
                    enum_name = enum_node.get_attribute('name')
                    enum_alias = enum_node.get_attribute('alias')
                    value_map[enum_name] = enum_alias
        j = 0

    def compile_uncategorized_types(self):
        for name in self.uncategorized_types:
            if name not in self.ctypes_map and name not in self.complex_type_node_map:
                self.ctypes_map[name] = CType()

    def compile_callback_node_map(self):
        for name, node in self.callback_node_map.items():
            assert name.startswith('PFN_')
            fn_type = self.ctypes_map[name[4:]] = CFunctionType(name[4:])
            self.ctypes_map[name] = fn_type.pointer()
            # Arguments and return type are to be resolved after compile_complex_type
            # Some complex types member might be a function pointer type
            # Some function pointer arguments might be a complex type
            # Circular references are allowed (pointer to incomplete type is valid pointer)
            # To resolve this, all function pointer types are eagerly generated, while complex types
            # with function pointer type circular can their member delayed:
            # class SomeComplexType(ctypes.Structure):
            #   pass
            # PFN_something = ctypes.POINTER(CFUNCTYPE(SomeComplexType), ...)
            # SomeComplexType._fields_ = [('circular', PFN_something)]

    def resolve_callback_type_map(self):
        for name, node in self.callback_node_map.items():
            code = self.get_member_code(node)
            code = re.sub(r'\bVKAPI_PTR\b', '', code)
            code = self.preprocess_c_code(code)
            ast = self.cparser.parse(code)
            assert type(ast.ext[0]) == pycparser.c_ast.Typedef
            assert ast.ext[0].name == name
            assert type(ast.ext[0].type == pycparser.c_ast.PtrDecl)
            assert type(ast.ext[0].type.type == pycparser.c_ast.FuncDecl)
            assert name.startswith('PFN_')
            assert name in self.ctypes_map
            assert name[4:] in self.ctypes_map
            fn_decl = ast.ext[0].type.type
            ctype = self.ctypes_map[name[4:]]
            assert isinstance(ctype, CFunctionType)
            ctype.constructor = 'VKAPI_PTR'
            for param in fn_decl.args.params:
                param_ctype = self.get_type_from_decl(param.type)
                ctype.argument_types.append(param_ctype)
                if param.name == 'pUserData':
                    ctype['user_data'] = len(ctype.argument_types) - 1
            return_ctype = self.get_type_from_decl(fn_decl.type)
            ctype.return_type = return_ctype

    def compile_commands(self):
        for name, node in self.command_node_map.items():
            code = '%s(%s);' % (self.get_member_code(node.get('proto')), ', '. join([self.get_member_code(x) for x in node.get_all('param')]))
            code = self.preprocess_c_code(code)
            ast = self.cparser.parse(code)
            assert type(ast.ext[0]) == pycparser.c_ast.Decl
            assert type(ast.ext[0].type == pycparser.c_ast.FuncDecl)
            decl = ast.ext[0].type
            ctype = CFunctionType(name)
            ctype.constructor = 'VKAPI_CALL'
            ctype.return_type = self.get_type_from_decl(decl.type)
            arg_ctype_list = []
            for param in decl.args.params:
                param_ctype = self.get_type_from_decl(param.type)
                ctype.argument_types.append(param_ctype)
            assert name not in self.ctypes_map
            self.ctypes_map[name] = ctype

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

    def compile_complex_type_node_map(self):
        for name, node in self.complex_type_node_map.items():
            self.compile_complex_type(name, node)

    def get_member_code(self, node):
        code = []
        for child in node.child_nodes:
            if child.node_name == 'comment':
                continue
            if child.node_name == 'enum':
                enum_name = child.get_text()
                if enum_name not in self.value_map:
                    raise Generator.Error('In %s: Reference to unknown enum "%s"' % (self.make_path(node)))
                enum_value = self.value_map[enum_name]
                if isinstance(enum_value, str):
                    enum_value = self.generate_c_string(enum_value)
                else:
                    assert isinstance(enum_value, int) or isinstance(enum_value, float)
                    enum_value = str(enum_value)
                code.append(enum_value)
                continue
            code.append(child.get_text())
        return ''.join(code)

    def get_type_from_decl(self, node):
        if type(node) is pycparser.c_ast.PtrDecl:
            return self.get_type_from_decl(node.type).pointer()
        if type(node) is pycparser.c_ast.ArrayDecl:
            if type(node.dim) != pycparser.c_ast.Constant:
                raise Generator.Error('Unsupported non-const-expr array')
            length = self.get_c_ast_const_value(node.dim)
            return CArrayType(self.get_type_from_decl(node.type), length)
        if type(node) is pycparser.c_ast.TypeDecl:
            if type(node.type) is pycparser.c_ast.IdentifierType:
                type_name = ' '.join(node.type.names)
            elif type(node.type) in [pycparser.c_ast.Struct, pycparser.c_ast.Union]:
                type_name = node.type.name
            else:
                raise NotImplementedError('TODO: C: TypeDecl => %s' % type(node.type).__name__)
            while type_name in self.alias_map:
                type_name = self.alias_map[type_name]
            if type_name not in self.ctypes_map:
                raise Generator.Error('Reference to undefined type "%s"' % (type_name))
            return self.ctypes_map[type_name]
        raise NotImplementedError('TODO: C: %s' % type(node).__name__)

    def resolve_complex_type(self, name, node):
        assert name in self.ctypes_map
        ctype = self.ctypes_map[name]
        assert isinstance(ctype, CComplexType)
        keyword = 'union' if node.get_attribute('category') == 'union' else 'struct'
        code = [
            '%s %s {' % (keyword, name)
        ]
        for member_node in node.get_all('member'):
            code.append('    %s;' % self.get_member_code(member_node))
        code.append('};')
        code = '\n'.join(code)
        code = self.preprocess_c_code(code)
        ast = self.cparser.parse(code)
        assert len(ast.ext) == 1
        assert type(ast.ext[0]) is pycparser.c_ast.Decl
        assert type(ast.ext[0].type) in [pycparser.c_ast.Struct, pycparser.c_ast.Union]
        assert ast.ext[0].type.name == name
        for decl in ast.ext[0].type.decls:
            ptr_count = 0
            array_length = []
            type_decl = decl.type
            member_type = self.get_type_from_decl(type_decl)
            assert decl.name in ctype.member_map
            ctype.member_map[decl.name]['ctype'] = member_type
            if decl.bitsize is not None:
                if type(decl.bitsize) is not pycparser.c_ast.Constant:
                    raise Generator.Error('In struct %s, member %s: bitsize is not specified as constant' % (name, decl.name))
                bitsize = self.get_c_ast_const_value(decl.bitsize)
                if not isinstance(bitsize, int):
                    raise Generator.Error('In struct %s, member %s: bitsize is not an integer constant' % (name, decl.name))
                ctype.member_map[decl.name]['bitsize'] = bitsize

    def compile_complex_type(self, name, node):
        if name in self.ctypes_map:
            assert isinstance(self.ctypes_map[name], CComplexType)
            return
        if name in self.resolving_complex_type:
            return
        self.resolving_complex_type.add(name)
        try:
            # Step1: Assign Complex Type immediately, as all we need to know is a name and the extending class.
            # The _fields_ can be added later.
            constructor = 'Union' if node.get_attribute('category') == 'union' else 'Structure'
            ctype = self.ctypes_map[name] = CComplexType(name, constructor)
            # Now that the type is added to the ctype map, ensure all members are also types.
            # In case of circular type reference, this type is already added to self.ctype_map,
            # which means the parser will properly return TYPEID for this type.
            # So delay in resolving is not required, but we can aggregate information about
            # if separate _fields_ is required and whose type must appear first.
            # (This might not be necessary, depending on how the code generation is done)
            ctype['delay_fields'] = False
            ctype['dependencies'] = []
            for member_node in node.get_all('member'):
                member_name = self.get_node_name_from_children(member_node)
                ctype.member_map[member_name] = {}
                ctype.member_list.append(member_name)
                if 'type' not in member_node.children:
                    raise Generator.Error('In %s, name="%s.%s": Missing attribute @type' % (self.make_path(node), name, member_name), node=member_node)
                if len(member_node.children['type']) > 1:
                    raise self.multiple_children_error(member_node, 'type')
                member_type = member_node.get('type').get_text()
                while member_type in self.alias_map:
                    member_type = self.alias_map[member_type]
                if member_type in self.resolving_complex_type:
                    assert member_type in self.ctypes_map
                    assert member_type in self.complex_type_node_map
                    assert isinstance(self.ctypes_map[member_type], CComplexType)
                    ctype['delay_fields'] = True
                    ctype['dependencies'].append(member_type)
                elif member_type not in self.ctypes_map:
                    if member_type in self.complex_type_node_map:
                        self.compile_complex_type(member_type, self.complex_type_node_map[member_type])
                        assert member_type in self.ctypes_map
                    else:
                        # Foreign types must have been resolved at this time (see category="basetype")
                        raise Generator.Error('In %s, name="%s.%s": Reference to unknow type "%s"' % (self.make_path(node), name, member_name, member_type))
            self.resolve_complex_type(name, node)
        finally:
            self.resolving_complex_type.remove(name)

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

    @staticmethod
    def generate_c_string(value: str):
        value = REGEXP_SUBST_TABLE.sub(subst_string_c_table, value)
        value = re.sub(r'[^\u0000-\u007F]', subst_string_unicode_char, value)
        return '"%s"' % value

    def get_key_name(self, enums_name: str, enum_name: str):
        lenums_name = enums_name.upper()
        lenum_parts = enum_name.upper().split('_')
        while True:
            part = lenum_parts[0]
            if lenums_name.startswith(part):
                part_len = len(part)
                lenums_name = lenums_name[part_len:]
                lenum_parts.pop(0)
            else:
                break
        return '_'.join(lenum_parts)

    def generate_enum_source(self):
        source = [
            'import ctypes',
            'from .base_enum import VulkanEnum',
            ''
        ]
        for enum_name, value_map in self.enum_type_map.items():
            ctype = self.ctypes_map[enum_name].to_source()
            source.append('class %s(VulkanEnum[%s]):' % (enum_name, ctype))
            for name, value in value_map.items():
                if isinstance(value, int):
                    source.append('    %s = %d' % (name, value))
            for name, value in value_map.items():
                if isinstance(value, str):
                    source.append('    %s = %s' % (name, value))
            source.append('')
        source.append('__all__ = %r' % list(self.enum_type_map.keys()))
        return os.linesep.join(source)

    def generate_bitmask_source(self):
        source = [
            'import ctypes',
            'from .base_enum import VulkanFlag',
            ''
        ]
        for bitmask_name, value_map in self.bitmask_type_map.items():
            ctype = self.ctypes_map[bitmask_name].to_source()
            source.append('class %s(VulkanFlag[%s]):' % (bitmask_name, ctype))
            for name, value in value_map.items():
                if isinstance(value, int):
                    source.append('    %s = %d' % (name, value))
            for name, value in value_map.items():
                if isinstance(value, str):
                    source.append('    %s = %s' % (name, value))
            source.append('')
        source.append('__all__ = %r' % list(self.bitmask_type_map.keys()))
        return os.linesep.join(source)

    def generate_const_source(self):
        source = [
            'import ctypes',
            'from .base_enum import VulkanConst',
            ''
        ]
        for const_name, const_info in self.const_map.items():
            if isinstance(const_info, dict):
                ctype = const_info['ctype'].to_source()
                value = const_info['value']
                source.append('%s = VulkanConst[%s](%d)' % (const_name, ctype, value))

        for const_name, const_info in self.const_map.items():
            if isinstance(const_info, str):
                source.append('%s = %s' % (const_name, const_info))

        source.append('__all__ = %r' % list(self.const_map.keys()))

        return os.linesep.join(source)

    def generate_value_source(self):
        source = [
            'from .ctype_const import *',
            'from .ctype_enum import *',
            'from .ctype_bitmask import *',
            ''
        ]

        names = list(self.const_map.keys())
        for type_map in [self.enum_type_map, self.bitmask_type_map]:
            for enum_name, value_map in type_map.items():
                for name in value_map.keys():
                    names.append(name)
                    source.append('%s = %s.%s' % (name, enum_name, name))
        
        source.append('')
        source.append('__all__ = %r' % names)
        
        return os.linesep.join(source)


    def generate_combined_source(self):
        source = ['import ctypes', '']
        exported_names = []
        current_indent = 0

        def indent(count=current_indent):
            return ' ' * 4 * count

        # TODO: There should be if/else condition for VKAPI_PTR and VKAPI_CALL
        # This should be ctypes.WINFUNCTION is it is defined, otherwise ctypes.CFUNCTION

        for name, value in self.value_map.items():
            from keyword import iskeyword
            assert name.isidentifier()
            assert not iskeyword(name)
            source.append('%s = %r' % (name, value))

        complex_type_has_class = set()
        complex_type_has_fields = set()
        func_type_declared = set()
        func_type_resolving = set()

        def generate_function_type(function_type_name):
            nonlocal self, source, func_type_declared, func_type_resolving
            if function_type_name in func_type_declared:
                return
            assert function_type_name in self.ctypes_map
            assert isinstance(self.ctypes_map[function_type_name], CFunctionType)
            if function_type_name in func_type_resolving:
                raise Generator.Error('Circular reference in function pointer for function "%s": Incomplete function types not supported, yet' % function_type_name)
            func_type_resolving.add(function_type_name)
            try:
                func_type = self.ctypes_map[function_type_name]
                args = []
                if func_type.return_type is self.ctypes_map['void']:
                    # Special case only for return type of functions
                    args.append('None')
                else:
                    ctype = target_ctype = func_type.return_type
                    while isinstance(ctype, CPointerType) or isinstance(ctype, CArrayType):
                        ctype = ctype._ctype
                    if isinstance(ctype, CComplexType):
                        generate_complex_type(ctype._name)
                    elif isinstance(ctype, CFunctionType):
                        generate_function_type(ctype._name)
                    args.append(target_ctype.to_source())
                if len(func_type.argument_types) and func_type.argument_types[0] is self.ctypes_map['void']:
                    # Single void (unnamed) argument is allowed: void fn(void)
                    pass
                else:
                    for target_ctype in func_type.argument_types:
                        ctype = target_ctype
                        while isinstance(ctype, CPointerType) or isinstance(ctype, CArrayType):
                            ctype = ctype._ctype
                        if isinstance(ctype, CComplexType):
                            generate_complex_type(ctype._name)
                        elif isinstance(ctype, CFunctionType):
                            generate_function_type(ctype._name)
                        args.append(target_ctype.to_source())
                if len(args) <= 1:
                    source.append('%s = %s(%s)' % (
                        function_type_name,
                        func_type.constructor,
                        args[0] if len(args) >= 1 else ''
                    ))
                else:
                    source.append('%s = %s(' % (function_type_name, func_type.constructor))
                    for arg in args[:-1]:
                        source.append('%s%s,' % (indent(1), arg))
                    source.append('%s%s' % (indent(1), args[-1]))
                    source.append(')')
                source.append('')
                func_type_declared.add(function_type_name)
            finally:
                func_type_resolving.remove(function_type_name)

        def generate_complex_type(complex_type_name):
            nonlocal complex_type_has_class, complex_type_has_fields, self, source, func_type_declared
            if complex_type_name in complex_type_has_class:
                return
            should_delay = False
            assert complex_type_name in self.ctypes_map
            assert isinstance(self.ctypes_map[complex_type_name], CComplexType)
            complex_type = self.ctypes_map[complex_type_name]
            for definition in complex_type.member_map.values():
                ctype = definition['ctype']
                while isinstance(ctype, CPointerType) or isinstance(ctype, CArrayType):
                    ctype = ctype._ctype
                if isinstance(ctype, CComplexType) and ctype._name not in complex_type_has_class:
                    should_delay = True
                    break
                if isinstance(ctype, CFunctionType) and ctype._name not in func_type_declared:
                    should_delay = True
                    break
            source.append('class %s(ctypes.%s):' % (complex_type_name, complex_type._constructor))
            if should_delay:
                source.append('%spass' % indent(1))
                source.append('')
                source.append('')
                complex_type_has_class.add(complex_type_name)
                for definition in complex_type.member_map.values():
                    ctype = definition['ctype']
                    while isinstance(ctype, CPointerType) or isinstance(ctype, CArrayType):
                        ctype = ctype._ctype
                    if isinstance(ctype, CComplexType) and ctype._name not in complex_type_has_class:
                        generate_complex_type(ctype._name)
                    if isinstance(ctype, CFunctionType):
                        generate_function_type(ctype._name)
                source.append('%s._fields_ = [' % (complex_type_name))
                for name in complex_type.member_list:
                    definition = complex_type.member_map[name]
                    if 'bitsize' in definition:
                        source.append('%s(%r, %s, %d),' % (indent(1), name, definition['ctype'].to_source(), definition['bitsize']))
                    else:
                        source.append('%s(%r, %s),' % (indent(1), name, definition['ctype'].to_source()))
                source.append(']')
                source.append('')
            else:
                source.append('%s_fields_ = [' % (indent(1)))
                for name in complex_type.member_list:
                    definition = complex_type.member_map[name]
                    if 'bitsize' in definition:
                        source.append('%s(%r, %s, %d),' % (indent(2), name, definition['ctype'].to_source(), definition['bitsize']))
                    else:
                        source.append('%s(%r, %s),' % (indent(2), name, definition['ctype'].to_source()))
                source.append('%s]' % (indent(1)))
                source.append('')
                source.append('')
                complex_type_has_class.add(complex_type_name)
            complex_type_has_fields.add(complex_type_name)

        source.append('if hasattr(ctypes, \'WINFUNCTYPE\'):')
        source.append(f'{indent(1)}VKAPI_CALL = ctypes.WINFUNCTYPE')
        source.append(f'{indent(1)}VKAPI_PTR = ctypes.WINFUNCTYPE')
        source.append(f'else:')
        source.append(f'{indent(1)}VKAPI_CALL = ctypes.CFUNCTYPE')
        source.append(f'{indent(1)}VKAPI_PTR = ctypes.CFUNCTYPE')
        source.append(f'')

        for name in self.complex_type_node_map.keys():
            generate_complex_type(name)
            exported_names.append(name)

        for name in self.command_node_map.keys():
            generate_function_type(name)

        source.append('complex_types = %r' % exported_names)

        return os.linesep.join(source)


def subst_unicode_hex(match):
    return chr(int(match.group(1), 16))


def subst_unicode_oct(match):
    return chr(int(match.group(1), 8))


def subst_string_unicode_char(match):
    char = match.group(0)
    code = ord(char)
    if code < 65535:
        return r'\u%04X' % code
    else:
        return r'\U%08X' % code


def subst_string_c_table(match):
    char = match.group(0)
    code = ord(char)
    return '\\%s' % subst_string_table[code]


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

subst_string_table = {v: k for k, v in subst_table.items()}

REGEXP_SUBST_TABLE = re.compile('[%s]' % ''.join(r'\x%02X' % x for x in subst_table.values()))


def subst_slash_escape(match):
    seq = match.group(1)
    if seq in subst_table:
        return chr(subst_table[seq])
    return match.group(0)
