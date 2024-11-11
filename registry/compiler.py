import logging, pycparser.c_ast, ctypes

from .node import Node
from .c import CParser, CGenerator, CIntType, CFloatType, CBooleanType, CPointerType, CStringPointerType, CArrayType, COpaqueType, ValueNode, UnaryOperatorNode, BinaryOperatorNode

class Compiler:
    def __init__(self):
        self.nodes = {}
        self.labels = {
            'alias': set(),
            'basetype': set(),
            'type': set(),
            'complex': set(),
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
        self.tags = {}

        self.enum_bit_map = {}
        self.bit_enum_map = {}
        self.enum_value_map = {}
        self.value_enum_map = {}
        self.object_macro_map = {}
        self.func_macro_map = {}
        self.value_map = {}

        self.logger = logging.getLogger('vulkan.registry')

        self.ctypes_map = {
            'void': None,
            'char': CIntType('c_char'),
            'float': CFloatType('c_float'),
            'double': CFloatType('c_double'),
            'int8_t': CIntType('c_int8'),
            'uint8_t': CIntType('c_uint8'),
            'int16_t': CIntType('c_int16'),
            'uint16_t': CIntType('c_uint16'),
            'uint32_t': CIntType('c_uint32'),
            'uint64_t': CIntType('c_uint64'),
            'int32_t': CIntType('c_int32'),
            'int64_t': CIntType('c_int64'),
            'size_t': CIntType('c_size_t'),
            'int': CIntType('c_int'),
            'bool': CBooleanType('c_bool'),
            'unsigned int': CIntType('c_uint'),
            'unsigned long': CIntType('c_ulong'),
            'unsigned long int': CIntType('c_ulong'),
            'unsigned short': CIntType('c_ushort'),
            'unsigned short int': CIntType('c_ushort'),
            'unsigned char': CIntType('c_ubyte'),
            'unsigned long long': CIntType('c_ulonglong'),
            'unsigned long long int': CIntType('c_ulonglong'),
            'long': CIntType('c_long'),
            'long int': CIntType('c_long'),
            'short': CIntType('c_short'),
            'short int': CIntType('c_short'),
            'long long': CIntType('c_longlong'),
            'long long int': CIntType('c_longlong'),
            'VisualID': CIntType('c_uint32'),  # X11/Xlib.h: CARD32
            'Window': CIntType('c_uint32'),  # X11/Xlib.h: CARD32 => XID
            'RROutput': CIntType('c_uint32'),  # X11/extensions/Xrandr.h
            'xcb_window_t': CIntType('c_uint32'),  # xcb/xcb.h
            'xcb_visualid_t': CIntType('c_uint32'), # xcb/xcb.h
            'HINSTANCE': CPointerType(type=None, input=True),  # windows.h
            'HWND': CPointerType(type=None, input=True),  # windows.h
            'HMONITOR': CPointerType(type=None, input=True),  # windows.h
            'HANDLE': CPointerType(type=None, input=True),  # windows.h
            'DWORD': CIntType('c_uint32'),  # windows.h
            'LPCSTR': CStringPointerType(char_type=CIntType('c_char'), input=True),  # windows.h
            'LPCTSTR': CStringPointerType(char_type=CIntType('c_char'), input=True),  # windows.h
            'LPCWSTR': CStringPointerType(char_type=CIntType('c_uint16'), encoding='utf-16', input=True),  # windows.h
            'zx_handle_t': CIntType('c_uint32'),  # zircon/types.h (Fuschia?)
            'GgpStreamDescriptor': CIntType('c_uint32'),  # Google games platform?
            'GgpFrameToken': CIntType('c_uint32'),  # Google games platform?
            'NvSciSyncAttrList': CPointerType(type=None, input=True), # NV Sci Platform
            'NvSciSyncObj': CPointerType(type=None, input=True), # NV Sci Platform
            'NvSciSyncFence': CArrayType(element_type=CIntType('c_uint64'), length=6), # NV Sci Platform
            'NvSciBufAttrList': CPointerType(type=None, input=True), # NV Sci Platform
            'NvSciBufObj': CPointerType(type=None, input=True), # NV Sci Platform
        }

        self.cparser = CParser(self.ctypes_map)
        self.cgenerator = CGenerator()

    @staticmethod
    def is_vulkan_api(node):
        if node.has_attribute('api'):
            api_set = { x.strip().lower() for x in node.get_attribute('api').split(',') }
            if 'vulkan' not in api_set:
                return False
        return True
    
    def _append_node(self, name: str, node: Node):
        if name not in self.nodes:
            self.nodes[name] = set()
        self.nodes[name].add(node)

    def add_xml(self, root: Node):
        self._enumerate_tag_nodes(root)
        self._enumerate_type_nodes(root)
        self._enumerate_enum_nodes(root)
        self._enumerate_command_nodes(root)
        self._enumerate_feature_nodes(root)
        self._enumerate_extension_nodes(root)

    def _enumerate_tag_nodes(self, root: Node):
        for tags_node in root.get_all('tags'):
            for tag_node in tags_node.get_all('tag'):
                if not self.is_vulkan_api(tag_node):
                    continue
                if not tag_node.has_attribute('name'):
                    self.logger.warning(f'xml:{tag_node.file_path}: skipping, missing attribute @name')
                    continue
                name = tag_node.get_attribute('name')
                if name not in self.tags:
                    self.tags[name] = set()
                self.tags[name].add(tag_node)

    def _enumerate_type_nodes(self, root):
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
                    self.logger.warning(f'xml:{type_node.file_path}: skipping, missing attribute @name or child <name>')
                    continue
                if type_node.has_attribute('alias'):
                    self.labels['alias'].add(name)
                else:
                    if category == 'bitmask':
                        mask_name = None
                        if type_node.has_attribute('bitvalues'):
                            mask_name = type_node.get_attribute('bitvalues')
                        elif type_node.has_attribute('requires'):
                            mask_name = type_node.get_attribute('requires')
                        if mask_name is not None:
                            if name in self.enum_bit_map and self.enum_bit_map[name] != mask_name:
                                self.logger.warning(f'xml:{type_node.file_path}: bitmask {name!r} refer to bits {mask_name!r}, but reference to different bits already exists: {self.enum_bit_map[name]!r}')
                            else:
                                self.enum_bit_map[name] = mask_name
                            if mask_name in self.bit_enum_map and self.bit_enum_map[mask_name] != name:
                                self.logger.warning(f'xml:{type_node.file_path}: bits {mask_name!r} refer to enum {name!r}, but reference to different enum already exists: {self.bit_enum_map[mask_name]!r}')
                            else:
                                self.bit_enum_map[mask_name] = name
                        self.labels['bitmask'].add(name)
                    elif category == 'funcpointer':
                        self.labels['callback'].add(name)
                    elif category in ['struct', 'union', 'enum', 'handle', 'define', 'basetype']:
                        self.labels[category].add(name)
                    if category in ['struct', 'union']:
                        self.labels['complex'].add(name)
                self._append_node(name, type_node)
    
    def _enumerate_enum_nodes(self, root: Node):
        for enums_node in root.get_all('enums'):
            if not self.is_vulkan_api(enums_node):
                continue
            enum_name = None
            if enums_node.has_attribute('name') and (enums_node.has_attribute('alias') or enums_node.has_attribute('type') and enums_node.get_attribute('type') in ['enum', 'bitmask']):
                enum_name = enums_node.get_attribute('name')
                if enums_node.has_attribute('alias'):
                    self.labels['alias'].add(enum_name)
                else:
                    self.labels['enum'].add(enum_name)
                    self.labels['type'].add(enum_name)
                    if enum_name not in self.enum_value_map:
                        self.enum_value_map[enum_name] = set()
                self._append_node(enum_name, enums_node)
            for enum_node in enums_node.get_all('enum'):
                if not self.is_vulkan_api(enum_node):
                    continue
                if not enum_node.has_attribute('name'):
                    self.logger.warning(f'xml:{enum_node.file_path}: skipping, missing attribute @name')
                    continue
                name = enum_node.get_attribute('name')
                if enum_node.has_attribute('alias'):
                    self.labels['alias'].add(name)
                else:
                    self.labels['value'].add(name)
                if enum_name is not None:
                    self.enum_value_map[enum_name].add(name)
                    self.value_enum_map[name] = enum_name
                self._append_node(name, enum_node)

    def _enumerate_command_nodes(self, root: Node):
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
                    self.logger.warning(f'xml:{command_node.file_path}: skipping, missing attribute @name or child <name>')
                    continue
                if command_node.has_attribute('alias'):
                    self.labels['alias'].add(name)
                else:
                    self.labels['command'].add(name)
                self._append_node(name, command_node)

    def _enumerate_feature_nodes(self, root: Node):
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
                            self.logger.warning(f'xml:{node.file_path}: skipping, missing attribute @name')
                            continue
                        name = node.get_attribute('name')
                        if node.has_attribute('alias') or name in self.labels['alias']:
                            self.labels['alias'].add(name)
                            if node_type == 'enum':
                                alias_name = node.get_attribute('alias')
                                if alias_name in self.value_enum_map:
                                    self.value_enum_map[name] = self.value_enum_map[alias_name]
                                    self.enum_value_map[self.value_enum_map[alias_name]].add(name)
                        elif node_type == 'enum':
                            self.labels['value'].add(name)
                            if node.has_attribute('extends'):
                                enum_name = node.get_attribute('extends')
                                if enum_name not in self.enum_value_map:
                                    self.enum_value_map[enum_name] = set()
                                self.enum_value_map[enum_name].add(name)
                        self._append_node(name, node)
    
    def _enumerate_extension_nodes(self, root: Node):
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
                                self.logger.warning(f'xml:{node.file_path}: skipping, missing attribute @name')
                                continue
                            name = node.get_attribute('name')
                            if node.has_attribute('alias') or name in self.labels['alias']:
                                self.labels['alias'].add(name)
                                if node_type == 'enum':
                                    alias_name = node.get_attribute('alias')
                                    if alias_name in self.value_enum_map:
                                        self.value_enum_map[name] = self.value_enum_map[alias_name]
                                        self.enum_value_map[self.value_enum_map[alias_name]].add(name)
                            elif node_type == 'enum':
                                self.labels['value'].add(name)
                                if node.has_attribute('extends'):
                                    enum_name = node.get_attribute('extends')
                                    if enum_name not in self.enum_value_map:
                                        self.enum_value_map[enum_name] = set()
                                    self.enum_value_map[enum_name].add(name)
                            self._append_node(name, node)

    def get_type_from_decl_ast(self, node: pycparser.c_ast.Node):
        if node.__class__ == pycparser.c_ast.PtrDecl:
            # This can be (const) char* (thus CStringPointerType)
            # Or it can be (const) void* (thus CPointer(None))
            is_input = hasattr(node.type, 'quals') and 'const' in node.type.quals
            if node.type.__class__ == pycparser.c_ast.IdentifierType:
                pointer_type = ' '.join(node.type.names)
                if pointer_type == 'char':
                    return CStringPointerType(char_type=CIntType('c_char'), input=is_input)
            return CPointerType(type=self.get_type_from_decl_ast(node.type), input=is_input)
        elif node.__class__ == pycparser.c_ast.ArrayDecl:
            length = self.get_c_ast_const_value(node.dim)
            return CArrayType(element_type=self.get_type_from_decl_ast(node.type), length=length)
        elif node.__class__ == pycparser.c_ast.TypeDecl:
            if node.type.__class__ == pycparser.c_ast.IdentifierType:
                type_name = ' '.join(node.type.names)
                if type_name in self.ctypes_map:
                    return self.ctypes_map[type_name]
                return COpaqueType(name=type_name)
            elif node.type.__class__ == [pycparser.c_ast.Struct, pycparser.c_ast.Union]:
                return COpaqueType(name=node.type.name)
            raise NotImplementedError(f'No implementation handles `pycparser.c_ast.{node.type.__class__.__name__}`')
        
    def get_c_constant_value_node(self, value):
        code = 'int value = %s;' % value
        code = self.preprocess_c_code(code)
        ast = self.cparser.parse(code)
        return self.get_c_ast_const_value(ast.ext[0].init)
    
    def preprocess_c_code(self, code: str):
        ast = self.cparser.parse(code)
        while self.preprocess_c_ast(ast):
            code = self.cgenerator.visit(ast)
            ast = self.cparser.parse(code)
        return code
    
    def preprocess_c_ast(self, node: pycparser.c_ast.Node):
        has_substitution = False
        for name, child_node in node.children():
            if type(child_node) is pycparser.c_ast.ID and child_node.name in self.object_macro_map:
                setattr(node, name, self.cgenerator.Code(self.object_macro_map[child_node.name]['code']))
                has_substitution = True
                continue
            if type(child_node) is pycparser.c_ast.FuncCall and child_node.name.name in self.func_macro_map:
                args = [self.cgenerator.visit(x) for x in child_node.args]
                macro = self.func_macro_map[child_node.name.name]
                if len(macro['arguments']) != len(args):
                    raise self.cparser.ParseError('Macro "%s" accept "%d" arguments, but called with "%d" arguments' % (child_node.name.name, len(macro['arguments'], len(args))))
                code = []
                for part in macro['template']:
                    if isinstance(part, str):
                        code.append(part)
                    else:
                        code.append(args[part['index']])
                code = ''.join(code)
                setattr(node, name, self.cgenerator.Code(code))
                has_substitution = True
                continue
            has_descendant_substitution = self.preprocess_c_ast(child_node)
            has_substitution = has_substitution or has_descendant_substitution
        return has_substitution
    
    def get_c_ast_const_value_node(self, node: pycparser.c_ast.Node):
        node_type = type(node)
        c_ast = pycparser.c_ast
        if node_type is c_ast.Constant:
            if 'int' in node.type:
                return ValueNode(getattr(ctypes, self.ctypes_map[' '.join(node.type)].name), self.cparser.parse_c_int(node.value))
            if node.type in ['float', 'double']:
                return ValueNode(getattr(ctypes, self.ctypes_map[' '.join(node.type)].name), self.cparser.parse_c_float(node.value))
            if node.type == 'string':
                return ValueNode(ctypes.c_char_p, self.cparser.parse_c_string(node.value))
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
            if node.op == '&':
                return self.get_c_ast_const_value(node.left) & self.get_c_ast_const_value(node.right)
            if node.op == '^':
                return self.get_c_ast_const_value(node.left) ^ self.get_c_ast_const_value(node.right)
            if node.op == '+':
                return self.get_c_ast_const_value(node.left) + self.get_c_ast_const_value(node.right)
            if node.op == '-':
                return self.get_c_ast_const_value(node.left) - self.get_c_ast_const_value(node.right)
            if node.op == '*':
                return self.get_c_ast_const_value(node.left) * self.get_c_ast_const_value(node.right)
            if node.op == '/':
                return self.get_c_ast_const_value(node.left) / self.get_c_ast_const_value(node.right)
            if node.op == '%':
                return self.get_c_ast_const_value(node.left) % self.get_c_ast_const_value(node.right)
            if node.op == '<<':
                return self.get_c_ast_const_value(node.left) << self.get_c_ast_const_value(node.right)
            if node.op == '>>':
                return self.get_c_ast_const_value(node.left) >> self.get_c_ast_const_value(node.right)
        elif node_type is c_ast.ID:
            if node.name not in self.value_map:
                raise self.cparser.ParseError('Missing ID: %s' % node.name)
            return self.value_map[node.name]['value']
        elif node_type is c_ast.Cast:
            target_type = self.get_type_from_decl_ast(node.to_type.type)
            value = self.get_c_ast_const_value(node.expr)
            return target_type.cast(value)
        raise NotImplementedError('Unsupported node type "%s"' % node_type.__name__)
