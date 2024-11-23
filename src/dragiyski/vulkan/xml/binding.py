import sys, re, ast, ctypes, pycparser.c_generator, pycparser.c_parser, pycparser.c_ast
from collections.abc import Mapping, Collection
from types import MappingProxyType
from logging import getLogger
from .taxonomy import Taxonomy
from .node import Node

logger = getLogger('dragiyski.vulkan.binding')

REGEXP_MULTILINE_COMMENT = re.compile(r'\/\*.*\*\/')
REGEXP_SINGLELINE_COMMENT = re.compile(r'\/\/.*')
REGEXP_FUNC_MACRO = re.compile(r'\s*#\s*define\s+(\w+)\(([^)]+)\)(.*)')
REGEXP_VALUE_MACRO = re.compile(r'\s*#\s*define\s+(\w+)\s+(.*)')

c_native_types = {
    'char': ctypes.c_char,
    'float': ctypes.c_float,
    'double': ctypes.c_double,
    'int8_t': ctypes.c_int8,
    'uint8_t': ctypes.c_uint8,
    'int16_t': ctypes.c_int16,
    'uint16_t': ctypes.c_uint16,
    'uint32_t': ctypes.c_uint32,
    'uint64_t': ctypes.c_uint64,
    'int32_t': ctypes.c_int32,
    'int64_t': ctypes.c_int64,
    'size_t': ctypes.c_size_t,
    'int': ctypes.c_int,
    'bool': ctypes.c_bool,
    'unsigned int': ctypes.c_uint,
    'unsigned long': ctypes.c_ulong,
    'unsigned long int': ctypes.c_ulong,
    'unsigned short': ctypes.c_ushort,
    'unsigned short int': ctypes.c_ushort,
    'unsigned char': ctypes.c_ubyte,
    'unsigned long long': ctypes.c_ulonglong,
    'unsigned long long int': ctypes.c_ulonglong,
    'int': ctypes.c_int,
    'long': ctypes.c_long,
    'long int': ctypes.c_long,
    'short': ctypes.c_short,
    'short int': ctypes.c_short,
    'long long': ctypes.c_longlong,
    'long long int': ctypes.c_longlong
}

c_external_types = {
    'VisualID': ctypes.c_uint32,  # X11/Xlib.h: CARD32
    'Window': ctypes.c_uint32,  # X11/Xlib.h: CARD32 => XID
    'RROutput': ctypes.c_uint32,  # X11/extensions/Xrandr.h
    'xcb_window_t': ctypes.c_uint32,  # xcb/xcb.h
    'xcb_visualid_t': ctypes.c_uint32, # xcb/xcb.h
    'HINSTANCE': ctypes.c_void_p,  # windows.h
    'HWND': ctypes.c_void_p,  # windows.h
    'HMONITOR': ctypes.c_void_p,  # windows.h
    'HANDLE': ctypes.c_void_p,  # windows.h
    'DWORD': ctypes.c_uint32,  # windows.h
    'LPCSTR': ctypes.c_char_p,  # windows.h
    'LPCTSTR': ctypes.c_char_p,  # windows.h
    'LPCWSTR': ctypes.c_wchar_p,  # windows.h
    'zx_handle_t': ctypes.c_uint32,  # zircon/types.h (Fuschia?)
    'GgpStreamDescriptor': ctypes.c_uint32,  # Google games platform?
    'GgpFrameToken': ctypes.c_uint32,  # Google games platform?
    'NvSciSyncAttrList': ctypes.c_void_p, # NV Sci Platform
    'NvSciSyncObj': ctypes.c_void_p, # NV Sci Platform
    'NvSciSyncFence': ctypes.c_uint64 * 6, # NV Sci Platform
    'NvSciBufAttrList': ctypes.c_void_p, # NV Sci Platform
    'NvSciBufObj': ctypes.c_void_p, # NV Sci Platform
}

class CGenerator(pycparser.c_generator.CGenerator):
    """
    Same as pycparser.c_generator.CGenerator, but accept a special node CGenerator.Code that can substitute C code in the AST.
    """
    def visit_Code(self, node):
        return node.code
    
    class Code(pycparser.c_ast.Node):
        __slots__ = ('code', 'coord', '__weakref__')

        def __init__(self, code):
            self.code = code

class CParser(pycparser.CParser):
    def __init__(self, types: Mapping = {}, **kwargs):
        super().__init__(**kwargs)
        self._types = types
    
    def _lex_type_lookup_func(self, name):
        if super()._lex_type_lookup_func(name):
            return True
        return name in self._types
    
    @staticmethod
    def parse_c_int(value):
        match = re.match(r'(-?)0x([0-9A-Fa-f]+)', value)
        if match:
            return (-1 if len(match.group(1)) else 1) * int(match.group(2), 16)
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
    
    @classmethod
    def parse_c_string(cls, value):
        if len(value) < 2 or value[0] != '"' or value[-1] != '"':
            raise ValueError('Invalid string value (missing open or close quotes): %s' % value)
        value = value[1:-1]

        value = re.sub(r'\\U([0-9A-Fa-f]{8})', cls.subst_unicode_hex, value)
        value = re.sub(r'\\u([0-9A-Fa-f]{4})', cls.subst_unicode_hex, value)
        value = re.sub(r'\\x([0-9A-Fa-f]{2})', cls.subst_unicode_hex, value)
        value = re.sub(r'\\([0-7]{3})', cls.subst_unicode_oct, value)
        value = re.sub(r'\\(.)', cls.subst_slash_escape, value)
        return value.encode('utf-8')
    
    @staticmethod
    def subst_unicode_hex(match):
        return chr(int(match.group(1), 16))


    @staticmethod
    def subst_unicode_oct(match):
        return chr(int(match.group(1), 8))


    @staticmethod
    def subst_string_unicode_char(match):
        char = match.group(0)
        code = ord(char)
        if code < 65535:
            return r'\u%04X' % code
        else:
            return r'\U%08X' % code

    @classmethod
    def subst_string_c_table(cls, match):
        char = match.group(0)
        code = ord(char)
        return '\\%s' % cls.subst_string_table[code]
    
    @classmethod
    def subst_slash_escape(cls, match):
        seq = match.group(1)
        if seq in cls.subst_table:
            return chr(cls.subst_table[seq])
        return match.group(0)

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

    @classmethod
    def generate_c_string(cls, value: str):
        value = cls.REGEXP_SUBST_TABLE.sub(cls.subst_string_c_table, value)
        value = re.sub(r'[^\u0000-\u007F]', cls.subst_string_unicode_char, value)
        return '"%s"' % value

class Binding:
    class DefinitionError(RuntimeError):
        pass

    class DuplicateDefinitionError(DefinitionError):
        pass

# Binding will directly bind vulkan names to ctypes.
# TODO: Create Api classes that accept binding and taxonomy
# TODO: Api classes can use both to generate more pythonic version of vulkan commands.
class LazyBinding(Binding):
    def __init__(self, taxonomy: Taxonomy, *, skip_names: Collection = set()):
        self.taxonomy = taxonomy

        # All names registered by Vulkan
        self._names = {}
        # All types by both Vulkan and external
        self._types = {
            **c_native_types,
            **c_external_types
        }
        # All known values (both vulkan and external)
        self._values = {
            'VK_NULL_HANDLE': None,
            'VK_USE_64_BIT_PTR_DEFINES': ctypes.sizeof(ctypes.c_void_p) == 8
        }
        self._skip_names = set(skip_names) | {
            'VK_DEFINE_HANDLE',
            'VK_DEFINE_NON_DISPATCHABLE_HANDLE'
        }
        self.c_parser = CParser(names=MappingProxyType(self._types))
        self.c_generator = CGenerator()
        # Preprocessor definitions
        self.pp_value_code = {}
        self.pp_func_code = {}

        # Note: Preprocessor macros are converted to functions which may call other preprocessor macro functions.
        # All functions are aggregated into a single module and compiled together, thus must be handled together,
        # and cannot be handled lazily.

        for name in self.taxonomy.category['define']:
            if name in self._skip_names:
                continue
            for node in self.taxonomy.nodes[name]:
                node: Node
                if node.path[-2:] != ['types', 'type']:
                    continue
                try:
                    self.c_preprocessor_define(node.get_text())
                except self.DefinitionError:
                    pass
        for name in self.pp_value_code:
            try:
                self._names[name] = self.__dict__[name] = self.c_get_constant_value(name)
            except NotImplementedError:
                pass
        macro_ast_def = {}
        for name in self.pp_func_code:
            try:
                macro_ast_def[name] = self.get_python_code_for_func_macro(name)
            except NotImplementedError:
                pass
        macro_ast_module = ast.Module(list(macro_ast_def.values()))
        ast.fix_missing_locations(macro_ast_module)
        vulkan_macros = {}
        exec(compile(macro_ast_module, '<vulkan.registry.#define>', 'exec'), vulkan_macros)
        for name in macro_ast_def.keys():
            self._names[name] = self.__dict__[name] = vulkan_macros[name]

    def __dir__(self):
        return object.__dir__(self) + list(self._names)
    
    def __getattr__(self, name: str):
        try:
            return self.__getitem__(name)
        except KeyError:
            raise AttributeError(name)
    def __getitem__(self, name: str):
        if name in self._names:
            if name in self.__dict__:
                return self.__dict__[name]
            try:
                value = self._get_binding(name)
            except NotImplementedError:
                logger.warning(sys.exc_info(), exc_info=True)
                raise KeyError(name)
            self.__dict__[name] = value
            return value
        raise KeyError(name)
    
    def _get_binding(self, name):
        if name not in self._names or name in self._skip_names:
            raise KeyError(name)
        name = self._resolve_alias(name)
        raise NotImplementedError('No vulkan binding for "%s"' % name)

    def _resolve_alias(self, name: str):
        while name in self.taxonomy.category['alias']:
            for node in self.taxonomy.nodes[name]:
                node: Node
                if node.has_attribute('alias'):
                    name = node.get_attribute('alias')
        return name

    @staticmethod
    def c_get_preprocessor_lines(code):
        lines = []
        code = REGEXP_MULTILINE_COMMENT.sub('', code)
        code = code.splitlines()
        is_continuation_line = False
        for line in code:
            line = REGEXP_SINGLELINE_COMMENT.sub('', line)
            if len(line.strip()) <= 0:
                is_continuation_line = False
                continue
            if is_continuation_line:
                lines[-1] += ' ' + line
                if lines[-1].endswith('\\'):
                    lines[-1] = lines[-1][:-1]
                    is_continuation_line = True
                else:
                    is_continuation_line = False
            else:
                if line.endswith('\\'):
                    is_continuation_line = True
                    line = line[:-1]
                else:
                    is_continuation_line = False
                lines.append(line)
        return lines
    
    def c_preprocessor_define(self, code):
        code = self.c_get_preprocessor_lines(code)
        if len(code) != 1:
            raise self.DefinitionError('Unable to define macro with more than one preprocessor line.')
        code = code[0]
        is_func_macro = REGEXP_FUNC_MACRO.fullmatch(code)
        if is_func_macro is not None:
            return self._c_preprocessor_define_func_macro(is_func_macro)
        is_value_macro = REGEXP_VALUE_MACRO.fullmatch(code)
        if is_value_macro is not None:
            return self._c_preprocessor_define_value_macro(is_value_macro)
    
    def _c_preprocessor_define_func_macro(self, data: re.Match):
        name = data.group(1)
        arguments = [arg.strip() for arg in data.group(2).split(',')]
        code = data.group(3).strip()
        # This might not properly handle if argument name appear in a C string, but it is good enough for now.
        # pycparser.cparser cannot be used, as it does not handle #-prefix and ## operator
        words = [y for x in code.split('##') for y in re.split(r'\b', x)]
        template = []
        for word in words:
            if word in arguments:
                if len(template) > 0 and template[-1] == '#':
                    template[-1] = {
                        'name': word,
                        'index': arguments.index(word),
                        'string': True
                    }
                else:
                    template.append({
                        'name': word,
                        'index': arguments.index(word),
                        'string': False
                    })
            else:
                template.append(word)
        if name in self.pp_func_code or name in self.pp_value_code:
            raise self.DuplicateDefinitionError(f'Macro "{name}" already defined.')
        self.pp_func_code[name] = {
            'arguments': arguments,
            'template': template,
        }
    
    def _c_preprocessor_define_value_macro(self, data: re.Match):
        name = data.group(1)
        code = data.group(2)
        if name in self.pp_func_code or name in self.pp_value_code:
            raise self.DuplicateDefinitionError(f'Macro "{name}" already defined.')
        self.pp_value_code[name] = code

    def c_preprocess_code(self, code: str):
        ast = self.c_parser.parse(code)
        while self.c_preprocess_ast(ast):
            code = self.c_generator.visit(ast)
            ast = self.c_parser.parse(code)
        return code
    
    def c_preprocess_ast(self, node: pycparser.c_ast.Node):
        has_substitution = False
        for name, child_node in node.children():
            if type(child_node) is pycparser.c_ast.ID and child_node.name in self.pp_value_code:
                setattr(node, name, self.c_generator.Code(self.pp_value_code[child_node.name]))
                has_substitution = True
                continue
            if type(child_node) is pycparser.c_ast.FuncCall and child_node.name.name in self.pp_func_code:
                args = [self.c_generator.visit(x) for x in child_node.args]
                macro = self.pp_func_code[child_node.name.name]
                if len(macro['arguments']) != len(args):
                    raise self.c_parser.ParseError('Macro "%s" accept "%d" arguments, but called with "%d" arguments' % (child_node.name.name, len(macro['arguments'], len(args))))
                code = []
                for part in macro['template']:
                    if isinstance(part, str):
                        code.append(part)
                    else:
                        code.append(args[part['index']])
                code = ''.join(code)
                setattr(node, name, self.c_generator.Code(code))
                has_substitution = True
                continue
            has_descendant_substitution = self.c_preprocess_ast(child_node)
            has_substitution = has_substitution or has_descendant_substitution
        return has_substitution

    def c_parse(self, code):
        code = self.c_preprocess_code(code)
        return self.c_parser.parse(code)
    
    def get_python_code_for_func_macro(self, name):
        if name not in self.pp_func_code:
            raise KeyError('No function macro named "%s" exists.' % name)
        descriptor = self.pp_func_code[name]
        try:
            code = self.c_preprocess_code('int value = %s(%s);' % (name, ', '.join(descriptor['arguments'])))
        except pycparser.c_parser.ParseError:
            return None
        code_ast = self.c_parser.parse(code)
        c_ast = pycparser.c_ast
        assert type(code_ast) is c_ast.FileAST
        assert type(code_ast.ext[0]) is c_ast.Decl
        assert isinstance(code_ast.ext[0].init, c_ast.Node)
        opts = {}
        try:
            node = self._generate_python_ast_from_c_ast(code_ast.ext[0].init, descriptor['arguments'], opts)
        except NotImplementedError:
            return None
        return_node = ast.Return(node)
        body = [return_node]
        if 'use_ctypes' in opts:
            body.insert(0, ast.Import([ast.alias('ctypes')]))
        def_node = ast.FunctionDef(
            name=name,
            args=ast.arguments(
                args=[ast.arg(arg_name) for arg_name in descriptor['arguments']],
                posonlyargs=[],
                kwonlyargs=[],
                kw_defaults=[],
                defaults=[]
            ),
            body=body,
            decorator_list=[],
            lineno=0,
            col_offset=0
        )
        return def_node
    
    def _generate_python_ast_from_c_ast(self, node: pycparser.c_ast.Node, args: list, opts: dict):
        node_type = type(node)
        c_ast = pycparser.c_ast
        if node_type is c_ast.Constant:
            if 'int' in node.type:
                return ast.Constant(self.c_parser.parse_c_int(node.value))
            elif node.type in ['float', 'double']:
                return ast.Constant(self.c_parser.parse_c_float(node.value))
            elif node.type == 'string':
                return ast.Constant(self.c_parser.parse_c_string(node.value))
        elif node_type is c_ast.UnaryOp:
            if node.op == '~':
                return ast.UnaryOp(op=ast.Invert(), operand=self._generate_python_ast_from_c_ast(node.expr, args, opts))
            elif node.op == '+':
                return ast.UnaryOp(op=ast.UAdd(), operand=self._generate_python_ast_from_c_ast(node.expr, args, opts))
            elif node.op == '-':
                return ast.UnaryOp(op=ast.USub(), operand=self._generate_python_ast_from_c_ast(node.expr, args, opts))
        elif node_type is c_ast.BinaryOp:
            if node.op == '|':
                return ast.BinOp(op=ast.BitOr(), left=self._generate_python_ast_from_c_ast(node.left, args, opts), right=self._generate_python_ast_from_c_ast(node.right, args, opts))
            elif node.op == '&':
                return ast.BinOp(op=ast.BitAnd(), left=self._generate_python_ast_from_c_ast(node.left, args, opts), right=self._generate_python_ast_from_c_ast(node.right, args, opts))
            elif node.op == '^':
                return ast.BinOp(op=ast.BitXor(), left=self._generate_python_ast_from_c_ast(node.left, args, opts), right=self._generate_python_ast_from_c_ast(node.right, args, opts))
            elif node.op == '+':
                return ast.BinOp(op=ast.Add(), left=self._generate_python_ast_from_c_ast(node.left, args, opts), right=self._generate_python_ast_from_c_ast(node.right, args, opts))
            elif node.op == '-':
                return ast.BinOp(op=ast.Sub(), left=self._generate_python_ast_from_c_ast(node.left, args, opts), right=self._generate_python_ast_from_c_ast(node.right, args, opts))
            elif node.op == '*':
                return ast.BinOp(op=ast.Mult(), left=self._generate_python_ast_from_c_ast(node.left, args, opts), right=self._generate_python_ast_from_c_ast(node.right, args, opts))
            elif node.op == '/':
                return ast.BinOp(op=ast.Div(), left=self._generate_python_ast_from_c_ast(node.left, args, opts), right=self._generate_python_ast_from_c_ast(node.right, args, opts))
            elif node.op == '%':
                return ast.BinOp(op=ast.Mod(), left=self._generate_python_ast_from_c_ast(node.left, args, opts), right=self._generate_python_ast_from_c_ast(node.right, args, opts))
            elif node.op == '<<':
                return ast.BinOp(op=ast.LShift(), left=self._generate_python_ast_from_c_ast(node.left, args, opts), right=self._generate_python_ast_from_c_ast(node.right, args, opts))
            elif node.op == '>>':
                return ast.BinOp(op=ast.RShift(), left=self._generate_python_ast_from_c_ast(node.left, args, opts), right=self._generate_python_ast_from_c_ast(node.right, args, opts))
        elif node_type is c_ast.ID:
            if node.name not in args:
                raise pycparser.c_parser.ParseError('Missing ID: %s' % node.name)
            return ast.Name(id=node.name, ctx=ast.Load())
        elif node_type is c_ast.Cast:
            native_type = self.c_generator.visit(node.to_type.type)
            if native_type in c_native_types:
                value_node = self._generate_python_ast_from_c_ast(node.expr, args, opts)
                expr_node = ast.Attribute(
                    value=ast.Call(
                        func=ast.Attribute(
                            value=ast.Name(id='ctypes', ctx=ast.Load()),
                            attr=c_native_types[native_type].__name__,
                            ctx=ast.Load()
                        ),
                        args=[
                            value_node
                        ],
                        keywords=[]
                    ),
                    attr='value',
                    ctx=ast.Load()
                )
                opts['use_ctypes'] = True
                return expr_node
            raise NotImplementedError('Casting to type: %s' % node.to_type.type)
        raise NotImplementedError('Unsupported node type "%s"' % node_type.__name__)
    
    def c_get_constant_value(self, value):
        code = 'int value = %s;' % (value)
        code = self.c_preprocess_code(code)
        ast = self.c_parser.parse(code)
        return self.c_get_const_value_ast(ast.ext[0].init)
    
    def c_get_const_value_ast(self, node: pycparser.c_ast.Node):
        node_type = type(node)
        c_ast = pycparser.c_ast
        if node_type is c_ast.Constant:
            if 'int' in node.type:
                return self.c_parser.parse_c_int(node.value)
            elif node.type in ['float', 'double']:
                return self.c_parser.parse_c_float(node.value)
            elif node.type == 'string':
                return self.c_parser.parse_c_string(node.value)
        elif node_type is c_ast.UnaryOp:
            match node.op:
                case '~':
                    return ~self.c_get_const_value_ast(node.expr)
                case '+':
                    return +self.c_get_const_value_ast(node.expr)
                case '-':
                    return -self.c_get_const_value_ast(node.expr)
        elif node_type is c_ast.BinaryOp:
            match node.op:
                case '|':
                    return self.c_get_const_value_ast(node.left) | self.c_get_const_value_ast(node.right)
                case '&':
                    return self.c_get_const_value_ast(node.left) & self.c_get_const_value_ast(node.right)
                case '^':
                    return self.c_get_const_value_ast(node.left) ^ self.c_get_const_value_ast(node.right)
                case '+':
                    return self.c_get_const_value_ast(node.left) + self.c_get_const_value_ast(node.right)
                case '-':
                    return self.c_get_const_value_ast(node.left) - self.c_get_const_value_ast(node.right)
                case '*':
                    return self.c_get_const_value_ast(node.left) * self.c_get_const_value_ast(node.right)
                case '/':
                    return self.c_get_const_value_ast(node.left) / self.c_get_const_value_ast(node.right)
                case '%':
                    return self.c_get_const_value_ast(node.left) % self.c_get_const_value_ast(node.right)
                case '<<':
                    return self.c_get_const_value_ast(node.left) << self.c_get_const_value_ast(node.right)
                case '>>':
                    return self.c_get_const_value_ast(node.left) >> self.c_get_const_value_ast(node.right)
        elif node_type is c_ast.ID:
            if node.name not in self.value_map:
                raise self.c_parser.ParseError('Missing ID: %s' % node.name)
            return self.value_map[node.name]['value']
        elif node_type is c_ast.Cast:
            native_type = self.c_generator.visit(node.to_type.type)
            if native_type in c_native_types:
                return c_native_types[native_type](self.c_get_const_value_ast(node.expr)).value
            raise NotImplementedError('Casting to type: %s' % node.to_type.type)
        raise NotImplementedError('Unsupported node type "%s"' % node_type.__name__)