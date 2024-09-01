from .xml_parser import Node
import pycparser.c_ast

class CompilerError(RuntimeError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.__dict__.update(**kwargs)
    
class CompileNodeError(CompilerError):
    def __init__(self, *args, node: Node, **kwargs):
        super().__init__(f'{node.file_path}:', *args if len(args) > 0 else 'Error while processing node <%s>' % node.node_name, node=node, **kwargs)
    
class DuplicateNodeNameError(CompileNodeError):
    def __init__(self, *args, node: Node, name: str, prev_node: Node, **kwargs):
        super().__init__('Duplicate named node <%s name="%s">, name defined by previous node at %s' % (node.node_name, name, prev_node.root.file_path), *args, node=node, name=name, prev_node=prev_node, **kwargs)

class MultipleChildrenNodeError(CompileNodeError):
    def __init__(self, *args, node: Node, name: str, count: int, **kwargs):
        super().__init__('Expected node <%s> expected a single child node <%s>, but found %d children.' % (node.node_name, name, count))

class NameMap(dict):
    class DuplicateKeyError(Exception):
        def __init__(self, *args, **kwargs):
            super().__init__(*args)
            self.__dict__.update(**kwargs)

    def set(self, name, value):
        if name in self:
            raise self.DuplicateKeyError('Name "%s" already exists' % name, name=name, old_value=self[name], new_value=value)
        self[name] = value

basic_ctypes = {
    'void': { 'class': 'type', 'type': 'unknown', 'name': 'void' },
    'char': { 'class': 'type', 'type': 'ctypes', 'name': 'c_char' },
    'float': { 'class': 'type', 'type': 'ctypes', 'name': 'c_float' },
    'double': { 'class': 'type', 'type': 'ctypes', 'name': 'c_double' },
    'int8_t': { 'class': 'type', 'type': 'ctypes', 'name': 'c_int8' },
    'uint8_t': { 'class': 'type', 'type': 'ctypes', 'name': 'c_uint8' },
    'int16_t': { 'class': 'type', 'type': 'ctypes', 'name': 'c_int16' },
    'uint16_t': { 'class': 'type', 'type': 'ctypes', 'name': 'c_uint16' },
    'uint32_t': { 'class': 'type', 'type': 'ctypes', 'name': 'c_uint32' },
    'uint64_t': { 'class': 'type', 'type': 'ctypes', 'name': 'c_uint64' },
    'int32_t': { 'class': 'type', 'type': 'ctypes', 'name': 'c_int32' },
    'int64_t': { 'class': 'type', 'type': 'ctypes', 'name': 'c_int64' },
    'size_t': { 'class': 'type', 'type': 'ctypes', 'name': 'c_size_t' },
    'int': { 'class': 'type', 'type': 'ctypes', 'name': 'c_int' },
    'bool': { 'class': 'type', 'type': 'ctypes', 'name': 'c_bool' },
    'unsigned int': { 'class': 'type', 'type': 'ctypes', 'name': 'c_uint' },
    'unsigned long': { 'class': 'type', 'type': 'ctypes', 'name': 'c_ulong' },
    'unsigned long int': { 'class': 'type', 'type': 'ctypes', 'name': 'c_ulong' },
    'unsigned short': { 'class': 'type', 'type': 'ctypes', 'name': 'c_ushort' },
    'unsigned short int': { 'class': 'type', 'type': 'ctypes', 'name': 'c_ushort' },
    'unsigned char': { 'class': 'type', 'type': 'ctypes', 'name': 'c_ubyte' },
    'unsigned long long': { 'class': 'type', 'type': 'ctypes', 'name': 'c_ulonglong' },
    'unsigned long long int': { 'class': 'type', 'type': 'ctypes', 'name': 'c_ulonglong' },
    'int': { 'class': 'type', 'type': 'ctypes', 'name': 'c_int' },
    'long': { 'class': 'type', 'type': 'ctypes', 'name': 'c_long' },
    'long int': { 'class': 'type', 'type': 'ctypes', 'name': 'c_long' },
    'short': { 'class': 'type', 'type': 'ctypes', 'name': 'c_short' },
    'short int': { 'class': 'type', 'type': 'ctypes', 'name': 'c_short' },
    'long long': { 'class': 'type', 'type': 'ctypes', 'name': 'c_longlong' },
    'long long int': { 'class': 'type', 'type': 'ctypes', 'name': 'c_longlong' }
}

# Directly used types that are not opaque pointers.
platform_ctypes = {
    'VisualID': { 'class': 'type', 'type': 'ctypes', 'name': 'c_uint32' },  # X11/Xlib.h: CARD32
    'Window': { 'class': 'type', 'type': 'ctypes', 'name': 'c_uint32' },  # X11/Xlib.h: CARD32 => XID
    'RROutput': { 'class': 'type', 'type': 'ctypes', 'name': 'c_uint32' },  # X11/extensions/Xrandr.h
    'xcb_window_t': { 'class': 'type', 'type': 'ctypes', 'name': 'c_uint32' },  # xcb/xcb.h
    'xcb_visualid_t': { 'class': 'type', 'type': 'ctypes', 'name': 'c_uint32' }, # xcb/xcb.h
    'HINSTANCE': { 'class': 'type', 'type': 'ctypes', 'name': 'c_void_p' },  # windows.h
    'HWND': { 'class': 'type', 'type': 'ctypes', 'name': 'c_void_p' },  # windows.h
    'HMONITOR': { 'class': 'type', 'type': 'ctypes', 'name': 'c_void_p' },  # windows.h
    'HANDLE': { 'class': 'type', 'type': 'ctypes', 'name': 'c_void_p' },  # windows.h
    'DWORD': { 'class': 'type', 'type': 'ctypes', 'name': 'c_uint32' },  # windows.h
    'LPCSTR': { 'class': 'type', 'type': 'ctypes', 'name': 'c_char_p' },  # windows.h
    'LPCTSTR': { 'class': 'type', 'type': 'ctypes', 'name': 'c_char_p' },  # windows.h
    'LPCWSTR': { 'class': 'type', 'type': 'ctypes', 'name': 'c_wchar_p' },  # windows.h
    'zx_handle_t': { 'class': 'type', 'type': 'ctypes', 'name': 'c_uint32' },  # zircon/types.h (Fuschia?)
    'GgpStreamDescriptor': { 'class': 'type', 'type': 'ctypes', 'name': 'c_uint32' },  # Google games platform?
    'GgpFrameToken': { 'class': 'type', 'type': 'ctypes', 'name': 'c_uint32' },  # Google games platform?
    'NvSciSyncAttrList': { 'class': 'type', 'type': 'ctypes', 'name': 'c_void_p' }, # NV Sci Platform
    'NvSciSyncObj': { 'class': 'type', 'type': 'ctypes', 'name': 'c_void_p' }, # NV Sci Platform
    'NvSciSyncFence': {
        'class': 'type',
        'type': 'array',
        'length': 6,
        'element_type': {
            'class': 'type',
            'type': 'ctypes',
            'name': 'c_uint64'
        }
    }, # NV Sci Platform
    'NvSciBufAttrList': { 'class': 'type', 'type': 'ctypes', 'name': 'c_void_p' }, # NV Sci Platform
    'NvSciBufObj': { 'class': 'type', 'type': 'ctypes', 'name': 'c_void_p' }, # NV Sci Platform
}

class Compiler:
    def __init__(self, api='vulkan'):
        self.vendor_tag = set()
        self.node_by_type = {}
        self.api = api
        self.vulkan_nodes = {
            'define': NameMap(),
            'basetype': NameMap(),
            'unknown': NameMap(),
            'bitmask': NameMap(),
            'handle': NameMap(),
            'enum': NameMap(),
            'enums': NameMap(),
            'set': NameMap(),
            'struct': NameMap(),
            'union': NameMap(),
            'complex': NameMap(),
            'command': NameMap(),
            'funcpointer': NameMap(),
            'value': NameMap(),
            'type': NameMap(),
            'all': NameMap(),
        }
        self.vulkan_decl = NameMap()
        self.vulkan_decl.update(basic_ctypes)
        self.vulkan_decl.update(platform_ctypes)
        self.vulkan_info = {
            'vendor_tags': set()
        }

    def is_target_api(self, node: Node):
        if not node.has_attribute('api'):
            return True
        api = node.get_attribute('api')
        return self.is_target_api_value(api)

    def is_target_api_value(self, value: str):
        api = [str.strip(x).lower() for x in value.split(',')]
        return self.api in api

    def add_xml(self, root: Node):
        self._enumerate_tags(root)
        self._enumerate_type_nodes(root)
        self._enumerate_enum_nodes(root)
        self._enumerate_command_nodes(root)
        pass
    
    @staticmethod
    def get_node_name_from_children(node: Node):
        if 'name' not in node.children:
            raise CompileNodeError('Missing node name: expected child element <name>', node=node)
        if len(node.children['name']) > 1:
            raise MultipleChildrenNodeError(node=node, name='name', count=len(node.children['name']))
        return node.get('name').get_text()

    @staticmethod
    def get_node_name_from_attribute(node: Node):
        if not node.has_attribute('name'):
            raise CompileNodeError('Missing node name: expected attribute @name', node=node)
        return node.get_attribute('name')

    @staticmethod
    def get_node_name(node):
        if node.has_attribute('name'):
            return node.get_attribute('name')
        if 'name' in node.children:
            if len(node.children['name']) > 1:
                raise MultipleChildrenNodeError(node=node, name='name', count=len(node.children['name']))
            return node.get('name').get_text()
        raise CompileNodeError('Missing node name: expected either attribute @name or child element <name>', node=node)

    def _enumerate_tags(self, node: Node):
        for tags_node in node.get_all('tags'):
            for tag_node in tags_node.get_all('tag'):
                if not tag_node.has_attribute('name'):
                    raise CompileNodeError('Expected <tag> node to have a @name attribute.', node=tag_node)
                name = tag_node.get_attribute('name')
                self.vulkan_info['vendor_tags'].add(name)

    def _enumerate_command_nodes(self, root_node: Node):
        for commands_node in root_node.get_all('commands'):
            for command_node in commands_node.get_all('command'):
                if not self.is_target_api(command_node):
                    continue
                if command_node.has_attribute('alias'):
                    self._enumerate_alias_node(command_node)
                    continue
                if 'proto' not in command_node.children:
                    raise CompileNodeError('Missing child <proto> for <command> node', node=command_node)
                if len(command_node.children['proto']) > 1:
                    raise MultipleChildrenNodeError(node=command_node, name='proto', count=len(command_node.children['proto']))
                proto_node = command_node.get('proto')
                name = self.get_node_name_from_children(proto_node)
                for name_target in ['command', 'all']:
                    try:
                        self.vulkan_nodes[name_target].set(name, command_node)
                    except NameMap.DuplicateKeyError as ex:
                        raise DuplicateNodeNameError(node=command_node, name=name, prev_node=context.command_node_map[name]) from ex
    
    def _enumerate_type_nodes(self, root_node: Node):
        for types_node in root_node.get_all('types'):
            for type_node in types_node.get_all('type'):
                if not self.is_target_api(type_node):
                    continue
                if type_node.has_attribute('alias'):
                    self._enumerate_alias_node(type_node)
                else:
                    category = type_node.get_attribute('category')
                    if category == 'define':
                        # defines are not actually a "type", they are just values or formulas.
                        self._enumerate_type_node([category], self.get_node_name, type_node)
                    elif category == 'basetype':
                        self._enumerate_type_node([category, 'all'], self.get_node_name, type_node)
                    elif category is None:
                        self._enumerate_unknown_type(type_node)
                    elif category == 'bitmask':
                        self._enumerate_type_node([category, 'set', 'all'], self.get_node_name_from_children, type_node)
                    elif category == 'handle':
                        self._enumerate_type_node(['handle', 'all'], self.get_node_name_from_children, type_node)
                    elif category == 'enum':
                        self._enumerate_type_node([category, 'set', 'all'], self.get_node_name_from_attribute, type_node)
                    elif category == 'struct' or category == 'union':
                        self._enumerate_type_node([category, 'complex', 'all'], self.get_node_name_from_attribute, type_node)
                    elif category == 'funcpointer':
                        self._enumerate_type_node([category, 'all'], self.get_node_name_from_children, type_node)

    def _enumerate_type_node(self, target_list: list, get_name: callable, node: Node):
        name = get_name(node)
        for target in target_list:
            name_map = self.vulkan_nodes[target]
            try:
                name_map.set(name, node)
            except NameMap.DuplicateKeyError as ex:
                raise DuplicateNodeNameError(node=node, name=name, prev_node=name_map[name]) from ex

    def _enumerate_alias_node(self, alias_node: Node):
        name = self.get_node_name_from_attribute(alias_node)
        assert isinstance(name, str) and len(name) > 0
        target = alias_node.get_attribute('alias')
        assert isinstance(target, str) and len(target) > 0
        if name in self.vulkan_decl:
            if self.vulkan_decl[name]['class'] != 'alias':
                raise CompileNodeError('Duplicate declaration of name "%s": alias redeclares non-alias name.' % name, node=alias_node)
            if self.vulkan_decl[name]['target'] != target:
                raise CompileNodeError('Duplicate declaration of name "%s": alias redeclare to target "%s" which is different from the original target name "%s".' % (name, target, self.vulkan_decl[name]['target']))
            self.vulkan_decl[name]['nodes'].add(alias_node)
        else:
            self.vulkan_decl[name] = {
                'class': 'alias',
                'target': target,
                'nodes': { alias_node }
            }

    def _enumerate_unknown_type(self, node: Node):
        name = self.get_node_name(node)
        if name in self.vulkan_decl:
            if self.vulkan_decl[name]['class'] != 'type':
                raise CompileNodeError('The name "%s" is already declared, but it is not a "type".' % name, node=node)
            return
        self.vulkan_decl[name] = {
            'class': 'type',
            'type': 'unknown',
            'name': name
        }

    def _enumerate_enum_nodes(self, root_node: Node):
        for enums_node in root_node.get_all('enums'):
            if not self.is_target_api(enums_node):
                continue
            enums_name = self.get_node_name_from_attribute(enums_node)
            enums_class = enums_node.get_attribute('type')
            if enums_class is not None and enums_class not in ['enum', 'bitmask']:
                enums_class = None
            if enums_class is not None:
                for name_target in ['enums']:
                    try:
                        self.vulkan_nodes[name_target].set(enums_name, enums_node)
                    except NameMap.DuplicateKeyError as ex:
                        raise DuplicateNodeNameError(node=enums_node, name=enums_name, prev_node=self.vulkan_nodes[name_target][enums_name])
            for enum_node in enums_node.get_all('enum'):
                if not self.is_target_api(enum_node):
                    continue
                enum_name = self.get_node_name_from_attribute(enum_node)
                if enum_node.has_attribute('alias'):
                    self._enumerate_alias_node(enum_node)
                    continue
                enum_object = { 'enum_node': enum_node, 'enums_node': enums_node }
                if enums_class is not None:
                    enum_object['enum_class'] = enums_class
                    enum_object['enum_name'] = enums_name
                if enum_node.has_attribute('type'):
                    enum_object['type'] = enum_node.get_attribute('type')
                for name_target in ['value', 'all']:
                    try:
                        self.vulkan_nodes[name_target].set(enum_name, enum_object)
                    except NameMap.DuplicateKeyError as ex:
                        raise DuplicateNodeNameError(node=enum_node, name=enum_name, prev_node=self.vulkan_nodes[name_target][enum_name])
