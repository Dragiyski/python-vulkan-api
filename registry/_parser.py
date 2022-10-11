import re
from ._xml_parser import parse_xml, Node, get_error_prefix
from ._platform import handle_ctypes
from pycparser import CParser, c_generator, c_ast


class CSparseParser(CParser):
    def _lex_type_lookup_func(self, name):
        # Always assume there are a type in scope.
        return True


class RegistryParser:
    def __init__(self, *files):
        from ._platform import basic_ctypes, platform_ctypes
        self.xml = [parse_xml(file, is_file=True) for file in files]
        self.ctypes = {**basic_ctypes, **platform_ctypes}
        self.alias = {}
        self.cparser = CSparseParser()
        self.cgenerator = c_generator.CGenerator(reduce_parentheses=True)
        self.handle_map = {}
        self.bitmask_map = {}
        self.basetype_map = {}
        self.enum_map = {}
        self.value_map = {}
        self.const_map = {}
        # Similar to value_map, but provides the name of the enum which the value belongs to, instead the value itself
        self.enum_value_map = {}
        self.bitmask_value_map = {}
        self._state = {}
        self.parse_basetype_nodes = self._parse_basetypes_nodes
        self.parse_bitmask_type_nodes = self._parse_bitmask_type_nodes
        self.parse_handle_type_nodes = self._parse_handle_type_nodes

    def _parse_basetypes_nodes(self):
        for xml in self.xml:
            for types_node in xml.get_all('types'):
                for type_node in types_node.get_all('type'):
                    if type_node.get_attribute('category') == 'basetype':
                        self._parse_basetype_node(type_node)

        # In case some typedef types are unresolved, resolve them now;
        for name, typedef in self.basetype_map.items():
            if name not in self.ctypes:
                # All base types must be resolved
                assert typedef['ctype'] in self.ctypes, f'Missing basetype typedef type "{typedef["ctype"]}" for type "{name}"'
                self.ctypes[name] = self.ctypes[typedef['ctype']]
        self.parse_basetype_nodes = self._parse_noop
        return self

    def _parse_bitmask_type_nodes(self):
        self.parse_basetype_nodes()
        for xml in self.xml:
            for types_node in xml.get_all('types'):
                for type_node in types_node.get_all('type'):
                    if type_node.get_attribute('category') == 'bitmask':
                        self._parse_bitmask_type_node(type_node)

        self.parse_bitmask_type_nodes = self._parse_noop
        return self

    def _parse_handle_type_nodes(self):
        for xml in self.xml:
            for types_node in xml.get_all('types'):
                for type_node in types_node.get_all('type'):
                    if type_node.get_attribute('category') == 'handle':
                        self._parse_handle_type_node(type_node)

        self.parse_handle_type_nodes = self._parse_noop
        return self

    def _parse_noop(self):
        return self

    def _parse_bitmask_type_node(self, node):
        if node.has_attribute('alias'):
            assert node.has_attribute('name'), f'{get_error_prefix(node)}: alias node missing attribute "name"'
            name = node.get_attribute('name')
            assert name not in self.alias, f'{get_error_prefix(node)}: alias "{name}" already defined'
            self.alias[name] = node.get_attribute('alias')
            return
        name_node = node.get('name')
        assert name_node is not None, f'{get_error_prefix(node)}: "name" child not found'
        name = name_node.get_text()
        definition = {
            'name': name,
            'type_node': node
        }
        for attr_name in ['requires', 'bitvalues']:
            if node.has_attribute(attr_name):
                assert 'bits' not in definition, f'{get_error_prefix(node)}: attributes "requires" and "bitvalues" are both present'
                definition['bits'] = node.get_attribute(attr_name)
        assert 'type' in node.children, f'{get_error_prefix(node)}: "type" child not found'
        definition['ctype'] = node.get('type').get_text()
        assert definition['ctype'] in self.ctypes, f'{get_error_prefix(node)}: ctype({definition["ctype"]}) not found'
        assert name not in self.ctypes, f'ctype({name}) is already defined'
        assert name not in self.bitmask_map, f'bitmask({name}) is already defined'
        self.ctypes[name] = self.ctypes[definition['ctype']]
        self.bitmask_map[name] = definition

    def _parse_basetype_node(self, node):
        name_node = node.get('name')
        assert name_node is not None, f'{get_error_prefix(node)}: "name" child not found'
        name = name_node.get_text()
        code = self.get_text_lines_children_tagged(node)
        code = self.get_line_containing_node(code, name_node)
        code = [x if isinstance(x, str) else x.get_text() for x in code]
        code = ''.join(code)
        if not code.startswith('typedef'):
            return
        assert name not in self.ctypes, f'"{name}" already declared in ctypes'
        assert name not in self.basetype_map, f'"{name}" already declared in basetype_map'
        definition = {
            'name': name,
            'node': node
        }
        ast = self.cparser.parse(code)
        assert len(ast.ext) == 1
        typedef = ast.ext[0]
        assert isinstance(typedef, c_ast.Typedef)
        assert typedef.name == name
        is_pointer = isinstance(typedef.type, c_ast.PtrDecl)
        typedecl = typedef.type
        while not isinstance(typedecl, c_ast.TypeDecl):
            assert hasattr(typedecl, 'type')
            typedecl = typedecl.type
        # Clear any qualifiers: {const char *} becomes {char *}
        typedecl.quals.clear()
        typedecl.align = None
        definition['ctype'] = self.cgenerator.visit(typedecl.type)
        if is_pointer:
            ctype = 'ctypes.c_void_p'
            if isinstance(typedecl.type, c_ast.IdentifierType):
                if 'char' in typedecl.type.names:
                    ctype = 'ctypes.c_char_p'
            self.ctypes[name] = ctype
        else:
            if isinstance(typedecl.type, c_ast.Struct):
                ctype = typedecl.type.name
            else:
                ctype = definition['ctype']
            if ctype in self.ctypes:
                self.ctypes[name] = self.ctypes[ctype]
        self.basetype_map[name] = definition

    def _parse_handle_type_node(self, node):
        if node.has_attribute('alias'):
            assert node.has_attribute('name'), f'{get_error_prefix(node)}: alias node missing attribute "name"'
            name = node.get_attribute('name')
            assert name not in self.alias, f'{get_error_prefix(node)}: alias "{name}" already defined'
            self.alias[name] = node.get_attribute('alias')
            return
        assert 'name' in node.children, f'{get_error_prefix(node)}: "name" child not found'
        assert 'type' in node.children, f'{get_error_prefix(node)}: "type" child not found'
        assert node.has_attribute('objtypeenum'), f'{get_error_prefix(node)}: attribute "objtypeenum" not found'
        name = node.get('name').get_text()
        ctype = node.get('type').get_text()
        assert ctype in handle_ctypes, f'{get_error_prefix(node)}: Unknown handle type "{ctype}"'
        definition = {
            'name': name,
            'ctype': ctype,
            'object_type': node.get_attribute('objtypeenum')
        }
        if node.has_attribute('parent'):
            definition['parent'] = node.get_attribute('parent')
        ctype = handle_ctypes[ctype]
        assert name not in self.ctypes, f'"{name}" already declared in ctypes'
        assert name not in self.handle_map, f'"{name}" already declared in handle_map'
        self.ctypes[name] = ctype
        self.handle_map[name] = definition
        
    def _parse_enums(self):
        self.parse_basetype_nodes()
        self.parse_bitmask_type_nodes()
        # 1. Get all enums from the types/type[category="enum"], and check for alias
        for xml in self.xml:
            for types_node in xml.get_all('types'):
                for type_node in types_node.get_all('type'):
                    if type_node.get_attribute('category') == 'enum':
                        assert type_node.has_attribute('name'), f'{get_error_prefix(type_node)}: enum type node missing attribute "name"'
                        name = node.get_attribute('name')
                        if type_node.has_attribute('alias'):
                            assert name not in self.alias, f'{get_error_prefix(node)}: alias "{name}" already defined'
                            self.alias[name] = type_node.get_attribute('alias')
        # Node <enums>:
        # ! @name
        # ! @type: can be "bitmask" or "enum", missing only for "API Constants"
        # ? @comment
        # ? @bitwidth: can be "64" is specified for type="bitmask", to indicate 64 bit flags:
        # but the exact type can be derived from <type> element.
        
        # Node <enums>/<enum>:
        # ! @name
        # ? @alias: if it is given, descript an alias. Only @name and @alias should be present.
        # ? @value: the value of the enum, in valid C notation, currently it can be:
        # Contant of type: float, int, unsigned int, unsigned long int, unsigned long long int
        # UnaryOp with operator ~, usually around uint64_t(-1), uint64_t(-2), uint32_t(-1), etc.
        # ? @bitpos: an integer for type="bitmask" indicating the bit position of a flag.
        # NOTE: bit position might be indicated with @value, @value can include bit unions, @value can be specified for no-bit-set (i.e. 0)
        # In other words, bitmask types should still process @value
        # NOTE: If @alias is not specified, exactly one of @bitpos and @value must be present (cannot be both present or both missing)
        # ? @type: Only present if <enums> type is missing, i.e. when defining a constant. Otherwise:
        # For bitmask, the type is inherited from the bitmask <type> definition, or bitwidth="64" = uint64_t
        # If enum type is present, it is that enum type,
        # Otherwise it is ctypes.c_int (=32-bit)
        # @type is never present if <enums> @type is present
        for xml in self.xml:
            for enums_node in xml.get_all('enums'):
                assert enums_node.has_attribute('name'), f'{get_error_prefix(type_node)}: enums node missing attribute "name"'
                enums_name = enums_node.get_attribute('name')
                enum_type = enums_node.get_attribute('type')
                if enum_type is not None:
                    assert enum_type == 'enum' or enum_type == 'bitmask'
                    if enum_type == 'enum':
                        self._process_enums_enum_node(enums_node)
                    else:
                        self._process_enums_bitmask_node(enums_node)
                else:
                    self._process_enums_const_node(enums_node)
                    
                
        # <extension>/<require>/<enum> (no <enums> node here), declare an extension to existing <enums> where:
        # @extends: if not present, just define a constant, otherwise it extends existing enum (from <enums>)
        # !!! Some constants are strings: c_ast.Contant(type="string")
        # @alias: can be present alongside with @extends, to define additional alias to enum
        # @value/@bitpos: defines the exact value of the enum. It is only way to convey a value for extension without @number (usually in video.xml)
        # @offset/@extnumber/@dir: defines a value derived from extension number.
        # @extnumber: if not defined, get the @number from parent <extension>
        # @dir: when defined it must be "-" (minus)
        # 
        # The formula for enum constant when defined from extensions is:
        # BASE = 1000000000 (1e9 = 1 billion)
        # EXT_NUMBER = @extnumber - 1
        # SIGN = -1 if @dir (== "-") else 1
        # OFFSET = @offset
        # EXT_VALUE = BASE + EXT_NUMBER * 1000 + OFFSET
        # VALUE = SIGN * EXT_VALUE
        
    def _process_enums_enum_node(enums_node):
        enums_name = enums_node.get_attribute('name')
        for enum_node in enums_node.get_all('enum'):
            assert enum_node.has_attribute('name')
            enum_name = enum_node.get_attribute('name')
            if enum_node.has_attribute('alias'):
                assert enum_name not in self.alias
                self.alias[enum_name] = enum_node.get_attribute('alias')
                
        
    @staticmethod
    def _parse_enum_value(value):
        # Type of value is meaningless here, we only process the initialization part.
        code = f'void *value = {value};'
        ast = self.cparser.parse(code)
        assert len(ast.ext) == 1
        assert type(ast.ext[0]) == c_ast.Decl
        return _get_python_value_for_c_ast(ast.ext[0].init)
    
    @staticmethod
    def _get_python_value_for_c_ast(ast_node):
        if type(ast_node) == c_ast.Constant:
            if 'int' in ast_node.type:
                return _get_python_value_for_c_int(ast_node.value)
            if ast_node.type in ['float', 'double']:
                return _get_python_value_for_c_float(ast_node.value)
            if ast_node.type == 'string':
                return _get_python_value_for_c_string(ast_node.value)
        
    def _get_c_const_value(self, ctype: str, value: str):
        value = value.strip('()')
        if '.' in value:
            assert ctype in ['float', 'double']
            match = re.search(r'[+-]?[0-9.]+', value)
            assert match is not None
            value = float(match.string[match.start():match.end()])
        else:
            assert ctype in self.basic_ctypes
            match = re.search(r'[+-]?[0-9]+', value)
            assert match is not None
            integer = int(match.string[match.start():match.end()])
            if '~' in value:
                value = eval(self.basic_ctypes[ctype])(~integer).value
            else:
                value = eval(self.basic_ctypes[ctype])(integer).value
        return value

    @staticmethod
    def get_text_lines_children_tagged(node):
        tagged_lines = []
        for child in node.child_nodes:
            if child.node_type == 'text':
                lines = child.node_value.splitlines()
                if len(tagged_lines) > 0 and isinstance(tagged_lines[-1][-1], Node):
                    tagged_lines[-1].append(lines.pop(0))
                if lines:
                    tagged_lines.append(lines)
            elif child.node_type == 'element':
                if not tagged_lines:
                    tagged_lines.append([])
                tagged_lines[-1].append(child)
        return tagged_lines

    @staticmethod
    def get_line_containing_node(tagged_lines, node):
        for line in tagged_lines:
            if node in line:
                return line
