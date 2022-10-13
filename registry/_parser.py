import re
import sys
import ctypes
from ._xml_parser import parse_xml, Node, get_error_prefix
from ._platform import handle_ctypes, basic_ctypes
from pycparser import CParser, c_generator, c_ast


class RegistryParseError(RuntimeError):
    @classmethod
    def check(cls, condition):
        if not condition:
            try:
                raise RuntimeError()
            except:
                from inspect import stack as stack_trace
                frames = stack_trace(1)
                traceback = type(sys.exc_info()[2])
            if isinstance(frames, list) and len(frames) > 1 and hasattr(frames[1], 'code_context') and isinstance(frames[1].code_context, list) and len(frames[1].code_context) == 1:
                match = re.match(r'^\s*RegistryParseError.check\((.*)\)$', frames[1][4][0])
                if match is not None:
                    tb = traceback(None, frames[1].frame, frames[1].index, frames[1].lineno)
                    raise cls(match.group(1)).with_traceback(tb)
            raise cls('RegistryParseError.check() failed')

class RegistryParser:
    def __init__(self, *files):
        from ._platform import basic_ctypes, platform_ctypes
        self.xml = [parse_xml(file, is_file=True) for file in files]
        self.ctypes = {**basic_ctypes, **platform_ctypes}
        self.alias = {}

        class CSparseParser(CParser):
            def _lex_type_lookup_func(parser, name):
                return name in self.ctypes
            
        class Code(c_ast.Node):
            __slots__ = ('code', 'coord', '__weakref__')
            def __init__(self, code):
                self.code = code
                
        def visit_Code(node):
            return node.code

        self.AstCode = Code
        self.cparser = CSparseParser()
        self.cgenerator = c_generator.CGenerator(reduce_parentheses=True)
        setattr(self.cgenerator, 'visit_Code', visit_Code)
        self.handle_map = {}
        self.bitmask_map = {}
        self.bitmask_bit_map = {}
        self.basetype_map = {}
        self.enum_map = {}
        self.value_map = {}
        self.const_map = {}
        self.macro_args_map = {}
        self.macro_no_args_map = {}
        # Similar to value_map, but provides the name of the enum which the value belongs to, instead the value itself
        self.enum_value_map = {}
        self.bitmask_value_map = {}
        self.struct_map = {}
        self._state = {}
        self.parse_basetype_nodes = self._parse_basetypes_nodes
        self.parse_bitmask_type_nodes = self._parse_bitmask_type_nodes
        self.parse_handle_type_nodes = self._parse_handle_type_nodes
        self.parse_enums = self._parse_enums
        self.parse_defines = self._parse_defines

    def _parse_defines(self):
        for xml in self.xml:
            for types_node in xml.get_all('types'):
                for type_node in types_node.get_all('type'):
                    if type_node.get_attribute('category') == 'define':
                        self._parse_define_node(type_node)

        self.parse_define = self._parse_noop()

    def _parse_define_node(self, node):
        if 'name' not in node.children:
            return
        name = node.get('name').get_text()
        code = node.get_text()
        code = re.sub(r'\/\/.*', '', code)
        code = '\n'.join([x for x in code.splitlines() if x])
        if not code.startswith('#define '):
            return
        code = code.replace('\\\n', '')
        has_args = True
        match = re.match(r'#define\s*(\w+)\s*\(([^)]+)\)\s*(.*)', code)
        if match is None:
            match = re.match(r'#define\s*(\w+)\s*(.*)', code)
            if match is None:
                return
            has_args = False
        match_name = match.group(1)
        if match_name != name:
            return
        if has_args:
            args = [x.strip() for x in match.group(2).split(',')]
        else:
            args = []
        template = []
        if has_args:
            code = match.group(3)
            code = re.split(r'\b', code)
            for entry in code:
                try:
                    arg_index = args.index(entry)
                except ValueError:
                    template.append(entry)
                    continue
                template.append({
                    'index': arg_index,
                    'name': entry
                })
                
            RegistryParseError.check(name not in self.macro_args_map)
            self.macro_args_map[name] = {
                'name': name,
                'arg_list': args,
                'template': template
            }
        else:
            RegistryParseError.check(name not in self.macro_no_args_map)
            self.macro_no_args_map[name] = match.group(2)
            
    def _generate_define_code(self, name, args):
        RegistryParseError.check(name in self.macro_args_map)
        macro = self.macro_args_map[name]
        RegistryParseError.check(len(args) == len(macro['arg_list']))
        template = macro['template']
        code = []
        for part in template:
            if isinstance(part, str):
                code.append(part)
            else:
                assert isinstance(part, dict)
                code.append(args[part['index']])
        return ''.join(code)
        

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
                RegistryParseError.check(typedef['ctype'] in self.ctypes)
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
            RegistryParseError.check(node.has_attribute('name'))
            name = node.get_attribute('name')
            RegistryParseError.check(name not in self.alias)
            self.alias[name] = node.get_attribute('alias')
            return
        name_node = node.get('name')
        RegistryParseError.check(name_node is not None)
        name = name_node.get_text()
        definition = {
            'name': name,
            'type_node': node
        }
        for attr_name in ['requires', 'bitvalues']:
            if node.has_attribute(attr_name):
                RegistryParseError.check('bits' not in definition)
                definition['bits'] = node.get_attribute(attr_name)
        RegistryParseError.check('type' in node.children)
        definition['ctype'] = node.get('type').get_text()
        RegistryParseError.check(definition['ctype'] in self.ctypes)
        RegistryParseError.check(name not in self.ctypes)
        RegistryParseError.check(name not in self.bitmask_map)
        self.ctypes[name] = self.ctypes[definition['ctype']]
        self.bitmask_map[name] = definition

    def _parse_basetype_node(self, node):
        name_node = node.get('name')
        RegistryParseError.check(name_node is not None)
        name = name_node.get_text()
        code = self.get_text_lines_children_tagged(node)
        code = self.get_line_containing_node(code, name_node)
        code = [x if isinstance(x, str) else x.get_text() for x in code]
        code = ''.join(code)
        if not code.startswith('typedef'):
            return
        RegistryParseError.check(name not in self.ctypes)
        RegistryParseError.check(name not in self.basetype_map)
        definition = {
            'name': name,
            'node': node
        }
        ast = self.cparser.parse(code)
        RegistryParseError.check(len(ast.ext) == 1)
        typedef = ast.ext[0]
        RegistryParseError.check(isinstance(typedef, c_ast.Typedef))
        RegistryParseError.check(typedef.name == name)
        is_pointer = isinstance(typedef.type, c_ast.PtrDecl)
        typedecl = typedef.type
        while not isinstance(typedecl, c_ast.TypeDecl):
            RegistryParseError.check(hasattr(typedecl, 'type'))
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
            RegistryParseError.check(node.has_attribute('name'))
            name = node.get_attribute('name')
            RegistryParseError.check(name not in self.alias)
            self.alias[name] = node.get_attribute('alias')
            return
        RegistryParseError.check('name' in node.children)
        RegistryParseError.check('type' in node.children)
        RegistryParseError.check(node.has_attribute('objtypeenum'))
        name = node.get('name').get_text()
        ctype = node.get('type').get_text()
        RegistryParseError.check(ctype in handle_ctypes)
        definition = {
            'name': name,
            'ctype': ctype,
            'object_type': node.get_attribute('objtypeenum')
        }
        if node.has_attribute('parent'):
            definition['parent'] = node.get_attribute('parent')
        ctype = handle_ctypes[ctype]
        RegistryParseError.check(name not in self.ctypes)
        RegistryParseError.check(name not in self.handle_map)
        self.ctypes[name] = ctype
        self.handle_map[name] = definition

    def _parse_enums(self):
        self.parse_defines()
        self.parse_basetype_nodes()
        self.parse_bitmask_type_nodes()
        # 1. Get all enums from the types/type[category="enum"], and check for alias
        for xml in self.xml:
            for types_node in xml.get_all('types'):
                for type_node in types_node.get_all('type'):
                    if type_node.get_attribute('category') == 'enum':
                        RegistryParseError.check(type_node.has_attribute('name'))
                        name = type_node.get_attribute('name')
                        if type_node.has_attribute('alias'):
                            RegistryParseError.check(name not in self.alias)
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
                RegistryParseError.check(enums_node.has_attribute('name'))
                enums_name = enums_node.get_attribute('name')
                enum_type = enums_node.get_attribute('type')
                if enum_type is not None:
                    RegistryParseError.check(enum_type == 'enum' or enum_type == 'bitmask')
                    if enum_type == 'enum':
                        self._parse_enums_enum_node(enums_node)
                    else:
                        self._parse_enums_bitmask_node(enums_node)
                else:
                    self._parse_enums_const_node(enums_node)

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
        for xml in self.xml:
            for exts_node in xml.get_all('extensions'):
                for ext_node in exts_node.get_all('extension'):
                    for req_node in ext_node.get_all('require'):
                        for enum_node in req_node.get_all('enum'):
                            self._parse_ext_enum_node(ext_node, enum_node)
        self.parse_enums = self._parse_noop

    def _parse_ext_enum_node(self, ext_node, enum_node):
        RegistryParseError.check(enum_node.has_attribute('name'))
        name = enum_node.get_attribute('name')
        if enum_node.has_attribute('alias'):
            self._assign_or_ensure_same_value(self.alias, name, enum_node.get_attribute('alias'))
            return
        definition = None
        if enum_node.has_attribute('extends'):
            extend_name = enum_node.get_attribute('extends')
            if extend_name in self.enum_map:
                definition = self.enum_map[extend_name]
            elif extend_name in self.bitmask_bit_map:
                definition = self.bitmask_bit_map[extend_name]
            else:
                raise RegistryParseError('Unable to extend non-existing enum "%s"' % extend_name)
        value = self._get_ext_enum_value(ext_node, enum_node)
        if value is None:
            RegistryParseError.check(self._resolve_alias(name) in self.value_map)
            return
        if definition is not None:
            self._assign_or_ensure_same_value(definition['values'], name, value)
            definition['values'][name] = value
        self._assign_or_ensure_same_value(self.value_map, name, value)

    @staticmethod
    def _assign_or_ensure_same_value(dictionary, key, value):
        if key not in dictionary:
            dictionary[key] = value
        else:
            RegistryParseError.check(dictionary[key] == value)

    def _resolve_alias(self, name):
        while name in self.alias:
            name = self.alias[name]
        return name

    def _parse_enums_enum_node(self, enums_node):
        enums_name = enums_node.get_attribute('name')
        RegistryParseError.check(enums_name not in self.enum_map)
        RegistryParseError.check(enums_name not in self.ctypes)
        # Currently the XML does not specify type of enums, they all seems to fallback to the default type: int
        # This does not apply to <enums> of type bitmask
        ctype = self.ctypes[enums_name] = 'ctypes.c_int'
        definition = self.enum_map[enums_name] = {
            'name': enums_name,
            'ctype': ctype,
            'values': {}
        }
        for enum_node in enums_node.get_all('enum'):
            RegistryParseError.check(enum_node.has_attribute('name'))
            enum_name = enum_node.get_attribute('name')
            if enum_node.has_attribute('alias'):
                RegistryParseError.check(enum_name not in self.alias)
                self.alias[enum_name] = enum_node.get_attribute('alias')
                return
            value = self._get_enum_value(enum_node)
            RegistryParseError.check(enum_name not in self.value_map)
            RegistryParseError.check(enum_name not in self.enum_value_map)
            RegistryParseError.check(enum_name not in definition['values'])
            definition['values'][enum_name] = value
            self.value_map[enum_name] = value
            self.enum_value_map[enum_name] = enums_name

    def _parse_enums_bitmask_node(self, enums_node):
        enums_name = enums_node.get_attribute('name')
        RegistryParseError.check(enums_name not in self.bitmask_bit_map)
        RegistryParseError.check(enums_name not in self.ctypes)
        # Currently the XML does not specify type of enums, they all seems to fallback to the default type: int
        # This does not apply to <enums> of type bitmask
        ctype = self.ctypes[enums_name] = 'ctypes.c_uint64' if enums_node.get_attribute('bitwidth') == 64 else 'ctypes.c_uint32'
        definition = self.bitmask_bit_map[enums_name] = {
            'name': enums_name,
            'ctype': ctype,
            'values': {}
        }
        for enum_node in enums_node.get_all('enum'):
            RegistryParseError.check(enum_node.has_attribute('name'))
            enum_name = enum_node.get_attribute('name')
            if enum_node.has_attribute('alias'):
                RegistryParseError.check(enum_name not in self.alias)
                self.alias[enum_name] = enum_node.get_attribute('alias')
                return
            value = self._get_enum_value(enum_node)
            RegistryParseError.check(enum_name not in self.value_map)
            RegistryParseError.check(enum_name not in self.bitmask_value_map)
            RegistryParseError.check(enum_name not in definition['values'])
            definition['values'][enum_name] = value
            self.value_map[enum_name] = value
            self.bitmask_value_map[enum_name] = enums_name

    def _parse_enums_const_node(self, enums_node):
        for enum_node in enums_node.get_all('enum'):
            RegistryParseError.check(enum_node.has_attribute('name'))
            name = enum_node.get_attribute('name')
            if enum_node.has_attribute('alias'):
                RegistryParseError.check(name not in self.alias)
                self.alias[name] = enum_node.get_attribute('alias')
                continue
            RegistryParseError.check(enum_node.has_attribute('type'))
            RegistryParseError.check(enum_node.has_attribute('value'))
            RegistryParseError.check(name not in self.value_map)
            ctype = enum_node.get_attribute('type')
            RegistryParseError.check(ctype in self.ctypes)
            value = enum_node.get_attribute('value')
            value = self._parse_enum_value(value)
            value = eval(self.ctypes[ctype])(value).value
            self.value_map[name] = value

    def _get_enum_value(self, node):
        if node.has_attribute('value'):
            value = self._parse_enum_value(node.get_attribute('value'))
            if node.get_attribute('dir') == '-':
                RegistryParseError.check(isinstance(value, int))
                value = -value
            return value
        if node.has_attribute('bitpos'):
            bitpos = int(node.get_attribute('bitpos'))
            return 1 << bitpos
        raise RegistryParseError('Expected node to have either @value or @bitpos attribute')

    def _get_ext_enum_value(self, ext_node, enum_node):
        if enum_node.has_attribute('value'):
            value = self._parse_enum_value(enum_node.get_attribute('value'))
            if enum_node.get_attribute('dir') == '-':
                RegistryParseError.check(isinstance(value, int))
                value = -value
            return value
        if enum_node.has_attribute('bitpos'):
            bitpos = int(enum_node.get_attribute('bitpos'))
            return 1 << bitpos
        if enum_node.has_attribute('offset'):
            value = int(enum_node.get_attribute('offset'), 10)
            RegistryParseError.check(value >= 0)
            if enum_node.has_attribute('extnumber'):
                ext_number = int(enum_node.get_attribute('extnumber')) - 1
            else:
                RegistryParseError.check(ext_node.has_attribute('number'))
                ext_number = int(ext_node.get_attribute('number')) - 1
            RegistryParseError.check(ext_number >= 0)
            value = 1000000000 + ext_number * 1000 + value
            if enum_node.get_attribute('dir') == '-':
                value = -value
            return value
        return None
    
    def _preprocess_children_ast(self, parent_node):
        has_substitution = False
        for name, child_node in parent_node.children():
            if type(child_node) == c_ast.ID and child_node.name in self.macro_no_args_map:
                setattr(parent_node, name, self.AstCode(self.macro_no_args_map[child_node.name]))
                has_substitution = True
                continue
            if type(child_node) == c_ast.FuncCall and child_node.name.name in self.macro_args_map:
                args = [self.cgenerator.visit(x) for x in child_node.args]
                code = self._generate_define_code(child_node.name.name, args)
                setattr(parent_node, name, self.AstCode(code))
                has_substitution = True
                continue
            has_substitution_new = self._preprocess_children_ast(child_node)
            has_substitution = has_substitution or has_substitution_new
        return has_substitution
    
    def _preprocess_c_code(self, code):
        ast = self.cparser.parse(code)
        while self._preprocess_children_ast(ast):
            code = self.cgenerator.visit(ast)
            ast = self.cparser.parse(code)
        return code

    def _parse_enum_value(self, value):
        # Type of value is meaningless here, we only process the initialization part.
        code = f'void *value = {value};'
        code = self._preprocess_c_code(code)
        ast = self.cparser.parse(code)
        RegistryParseError.check(len(ast.ext) == 1)
        RegistryParseError.check(type(ast.ext[0]) == c_ast.Decl)
        return self._get_python_value_for_c_ast(ast.ext[0].init)

    def _get_python_value_for_c_ast(self, ast_node):
        if type(ast_node) == c_ast.Constant:
            if 'int' in ast_node.type:
                return self._get_python_value_for_c_int(ast_node.value)
            if ast_node.type in ['float', 'double']:
                return self._get_python_value_for_c_float(ast_node.value)
            if ast_node.type == 'string':
                return self._get_python_value_for_c_string(ast_node.value)
        elif type(ast_node) == c_ast.UnaryOp:
            if ast_node.op == '~':
                return ~self._get_python_value_for_c_ast(ast_node.expr)
            if ast_node.op == '+':
                return +self._get_python_value_for_c_ast(ast_node.expr)
            if ast_node.op == '-':
                return -self._get_python_value_for_c_ast(ast_node.expr)
            raise NotImplementedError('Handling of UnaryOp(%s) is not implemented' % node.op)
        elif type(ast_node) == c_ast.BinaryOp:
            if ast_node.op == '|':
                return self._get_python_value_for_c_ast(ast_node.left) | self._get_python_value_for_c_ast(ast_node.right)
            if ast_node.op == '<<':
                return self._get_python_value_for_c_ast(ast_node.left) << self._get_python_value_for_c_ast(ast_node.right)
        elif type(ast_node) == c_ast.Cast:
            target_type = self.cgenerator.visit(ast_node.to_type)
            RegistryParseError.check(target_type in basic_ctypes)
            value = self._get_python_value_for_c_ast(ast_node.expr)
            return eval(basic_ctypes[target_type])(value).value
        raise NotImplementedError('Handling of note of type [%s] is not implemented' % type(ast_node).__name__)

    @staticmethod
    def _get_python_value_for_c_int(value):
        match = re.match(r'0x([0-9A-Fa-f]+)', value)
        if match:
            return int(match.group(0), 16)
        match = re.match(r'-?[0-9]+', value)
        if match:
            return int(match.group(0), 10)
        raise ValueError('Invalid integer value: %r' % value)

    @staticmethod
    def _get_python_value_for_c_float(value):
        match = re.match(r'-?[0-9]+(?:\.[0-9]+)?', value)
        if match:
            return float(match.group(0))
        raise ValueError('Invalid float value: %r' % value)

    @staticmethod
    def _get_python_value_for_c_string(value):
        RegistryParseError.check(value[0] == '"' and value[-1] == '"')
        value = value[1:-1]

        value = re.sub(r'\\U([0-9A-Fa-f]{8})', subst_unicode_hex, value)
        value = re.sub(r'\\u([0-9A-Fa-f]{4})', subst_unicode_hex, value)
        value = re.sub(r'\\x([0-9A-Fa-f]{2})', subst_unicode_hex, value)
        value = re.sub(r'\\([0-7]{3})', subst_unicode_oct, value)
        value = re.sub(r'\\(.)', subst_slash_escape, value)
        return value.encode('utf-8')

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


def subst_unicode_hex(match):
    return chr(int(match.group(0), 16))


def subst_unicode_oct(match):
    return chr(int(match.group(0), 8))


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
    seq = match.group(0)
    if seq in subst_table:
        return chr(subst_table[seq])
    return match.string[match.start():match.end()]
