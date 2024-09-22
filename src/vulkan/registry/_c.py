from collections.abc import Mapping, Container
import ast
from typing import Callable

import re
import pycparser.c_ast
import pycparser.c_generator

from .platform import native_types, platform_types

REGEXP_MULTILINE_COMMENT = re.compile(r'\/\*.*\*\/')
REGEXP_SINGLELINE_COMMENT = re.compile(r'\/\/.*')
REGEXP_FUNC_MACRO = re.compile(r'\s*#\s*define\s+(\w+)\(([^)]+)\)(.*)')
REGEXP_VALUE_MACRO = re.compile(r'\s*#\s*define\s+(\w+)\s+(.*)')

def _return_false(*args, **kwargs):
    return False

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
    """
    Same as pycparser.CParser, but allow types to be specified in a python Container (usually Set)
    """
    def __init__(self, types: Container, **kwargs):
        super().__init__(**kwargs)
        self.c_types = types

    def _lex_type_lookup_func(self, name):
        if super()._lex_type_lookup_func(name):
            return True
        return name in self.c_types
    
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
    
    class ParseError(RuntimeError):
        pass

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

class CContext:
    class DefinitionError(RuntimeError):
        pass

    class DuplicateDefinitionError(DefinitionError):
        pass
    
    def __init__(self):
        # Known ctypes
        self.c_type_map = {}
        # Known types in C, may contain private types that do not map to ctypes, used during parsing.
        self.c_type_set = set()
        self.c_parser = CParser(self.c_type_set)
        self.c_generator = CGenerator()
        self.py_value = {}
        self.pp_value_code = {}
        self.pp_func_code = {}

    def define(self, code):
        code = self.get_preprocessor_lines(code)
        if len(code) != 1:
            raise self.DefinitionError('Unable to define macro with more than one preprocessor line.')
        code = code[0]
        is_func_macro = REGEXP_FUNC_MACRO.fullmatch(code)
        if is_func_macro is not None:
            return self._define_func_macro(is_func_macro)
        is_value_macro = REGEXP_VALUE_MACRO.fullmatch(code)
        if is_value_macro is not None:
            return self._define_value_macro(is_value_macro)

    @staticmethod
    def get_preprocessor_lines(code):
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
    
    def _define_func_macro(self, data: re.Match):
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

    def _define_value_macro(self, data: re.Match):
        name = data.group(1)
        code = data.group(2)
        if name in self.pp_func_code or name in self.pp_value_code:
            raise self.DuplicateDefinitionError(f'Macro "{name}" already defined.')
        self.pp_value_code[name] = code

    def preprocess_code(self, code: str):
        ast = self.c_parser.parse(code)
        while self.preprocess_ast(ast):
            code = self.c_generator.visit(ast)
            ast = self.c_parser.parse(code)
        return code

    def preprocess_ast(self, node: pycparser.c_ast.Node):
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
            has_descendant_substitution = self.preprocess_ast(child_node)
            has_substitution = has_substitution or has_descendant_substitution
        return has_substitution
    
    def parse(self, code):
        code = self.preprocess_code(code)
        return self.c_parser.parse(code)

    def get_python_code_for_func_macro(self, name):
        if name not in self.pp_func_code:
            raise KeyError('No function macro named "%s" exists.' % name)
        descriptor = self.pp_func_code[name]
        from pycparser.c_parser import ParseError
        try:
            code = self.preprocess_code('int value = %s(%s);' % (name, ', '.join(descriptor['arguments'])))
        except ParseError:
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
                raise self.c_parser.ParseError('Missing ID: %s' % node.name)
            return ast.Name(id=node.name, ctx=ast.Load())
        elif node_type is c_ast.Cast:
            native_type = self.c_generator.visit(node.to_type.type)
            if native_type in native_types:
                value_node = self._generate_python_ast_from_c_ast(node.expr, args, opts)
                expr_node = ast.Attribute(
                    value=ast.Call(
                        func=ast.Attribute(
                            value=ast.Name(id='ctypes', ctx=ast.Load()),
                            attr=native_types[native_type].__name__,
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
    
    def get_constant_value(self, value):
        code = 'int value = %s;' % (value)
        code = self.preprocess_code(code)
        ast = self.c_parser.parse(code)
        return self.get_const_value_ast(ast.ext[0].init)
    
    def get_const_value_ast(self, node: pycparser.c_ast.Node):
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
                    return ~self.get_const_value_ast(node.expr)
                case '+':
                    return +self.get_const_value_ast(node.expr)
                case '-':
                    return -self.get_const_value_ast(node.expr)
        elif node_type is c_ast.BinaryOp:
            match node.op:
                case '|':
                    return self.get_const_value_ast(node.left) | self.get_const_value_ast(node.right)
                case '&':
                    return self.get_const_value_ast(node.left) & self.get_const_value_ast(node.right)
                case '^':
                    return self.get_const_value_ast(node.left) ^ self.get_const_value_ast(node.right)
                case '+':
                    return self.get_const_value_ast(node.left) + self.get_const_value_ast(node.right)
                case '-':
                    return self.get_const_value_ast(node.left) - self.get_const_value_ast(node.right)
                case '*':
                    return self.get_const_value_ast(node.left) * self.get_const_value_ast(node.right)
                case '/':
                    return self.get_const_value_ast(node.left) / self.get_const_value_ast(node.right)
                case '%':
                    return self.get_const_value_ast(node.left) % self.get_const_value_ast(node.right)
                case '<<':
                    return self.get_const_value_ast(node.left) << self.get_const_value_ast(node.right)
                case '>>':
                    return self.get_const_value_ast(node.left) >> self.get_const_value_ast(node.right)
        elif node_type is c_ast.ID:
            if node.name not in self.value_map:
                raise self.c_parser.ParseError('Missing ID: %s' % node.name)
            return self.value_map[node.name]['value']
        elif node_type is c_ast.Cast:
            native_type = self.c_generator.visit(node.to_type.type)
            if native_type in native_types:
                return native_types[native_type](self.get_const_value_ast(node.expr)).value
            raise NotImplementedError('Casting to type: %s' % node.to_type.type)
        raise NotImplementedError('Unsupported node type "%s"' % node_type.__name__)
    
