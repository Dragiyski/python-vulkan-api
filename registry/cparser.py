from __future__ import annotations

import pycparser
import re

import pycparser.c_ast
from .platform import CArrayType

class ParseError(RuntimeError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.__dict__.update(kwargs)
        
class CLexer(pycparser.c_lexer.CLexer):
    def t_PPHASH(self, t):
        t.type = 'PPHASH'
        return t

def preprocessor(code):
    brace_count = 0
    
    class Token:
        def __init__(self, type, value, position, line_index, column_index):
            self.type = type
            self.value = value
            self.position = position
            self.line_index = line_index
            self.column_index = column_index
    
    def on_error(message, line_number, column_number):
        raise ParseError('%d:%d:%s' % (line_number, column_number, message))
    
    def on_lbrace():
        nonlocal brace_count
        brace_count += 1
    
    def on_rbrace():
        nonlocal brace_count
        brace_count -= 1
    
    def on_type(name):
        return False
    
    lex = CLexer(on_error, on_lbrace, on_rbrace, on_type)
    from pycparser import lextab
    lex.build(optimize=True, lextab=lextab)
    lex.lexer.lexliterals += '\\'
    lex.lexer.lineno = 0
    
    current_position = 0
    current_line = 0
    current_column = 0
    
    lex.input(code)
    token_list = []
    
    while True:
        token = lex.token()
        if token.lexpos > current_position:
            token_list.append(Token('IGNORE', code[current_position:token.lexpos], current_position, current_line, current_column))
            current_position = token.lexpos
            last_token_lines = token_list[-1].value.splitlines()
            current_line += len(last_token_lines) - 1
            current_column = len(last_token_lines[-1])
        if token is None:
            return
        print(token)

class CParser(pycparser.CParser):
    def __init__(self, lookup: callable):
        super().__init__()
        self.__lookup = lookup

    def _lex_type_lookup_func(self, name):
        if super()._lex_type_lookup_func(name):
            return True
        return self.__lookup(name)
    
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
    
    # def get_type_from_decl(self, node: pycparser.c_ast.Node):
    #     if type(node) is pycparser.c_ast.PtrDecl:
    #         return self.get_type_from_decl(node.type).pointer()
    #     if type(node) is pycparser.c_ast.ArrayDecl:
    #         length = self.context.get_c_ast_const_value(node.dim)
    #         return CArrayType(self.get_type_from_decl(node.type), length)
    #     if type(node) is pycparser.c_ast.TypeDecl:
    #         if type(node.type) is pycparser.c_ast.IdentifierType:
    #             type_name = ' '.join(node.type.names)
    #         elif type(node.type) in [pycparser.c_ast.Struct, pycparser.c_ast.Union]:
    #             type_name = node.type.name
    #         else:
    #             raise NotImplementedError('TODO: C: TypeDecl => %s' % type(node.type).__name__)
    #         while type_name in self.context.alias_map:
    #             type_name = self.context.alias_map[type_name]
    #         if type_name not in self.context.ctypes_map:
    #             raise ParseError('Reference to undefined type "%s"' % (type_name))
    #         return self.ctypes_map[type_name]
    #     raise NotImplementedError('TODO: C: %s' % type(node).__name__)
    
class CGenerator(pycparser.c_generator.CGenerator):
    def visit_Code(self, node):
        return node.code
    
    class Code(pycparser.c_ast.Node):
        __slots__ = ('code', 'coord', '__weakref__')

        def __init__(self, code):
            self.code = code