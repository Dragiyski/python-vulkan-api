import pycparser

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
            self.value = values
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
    
    is_new_line = True
    
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
