import pycparser
import functools
import re

REGEXP_MULTILINE_COMMENT = re.compile(r'\/\*.*\*\/')
REGEXP_SINGLELINE_COMMENT = re.compile(r'\/\/.*')

# TODO: Override CParser class with method p_pp_directive handling (see p_pppragma_directive for how preprocessor is handled in the AST)
# TODO: This might require additional pp_condition_stack which store the nodes for each "#if/#ifdef/#ifndef" directives, so that
# TODO: #elif and #else can be attached to any #if node on top of the stack. The #if must contain conditions:list (will have at least one element) and alternative: a block of expressions
# TODO: A condition will have the condition line (unparsed) and a list of expression similar to Compound statement

# TODO: Preprocessor is meant to be run once before actual code parsing.


class CParser(pycparser.CParser):
    def __init__(self, ctypes_map=dict(), **kwargs):
        super().__init__(lexer=self.__make_lexer, **kwargs)
        self.__ctypes_map = ctypes_map

    def __make_lexer(self, error_func, on_lbrace_func, on_rbrace_func, type_lookup_func):
        lexer = pycparser.c_lexer.CLexer(error_func, on_lbrace_func, on_rbrace_func, functools.partial(self.__type_lookup_func, type_lookup_func))
        return lexer

    def __type_lookup_func(self, parent_func, name):
        if parent_func(name):
            return True
        return name in self.__ctypes_map

    def parse(self, code, *args, **kwargs):
        code = remove_comments(code)
        return super().parse(code, *args, **kwargs)


class CPreprocessor:
    class ParseError(RuntimeError):
        pass

    class Directive:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    class Source:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    def __init__(self, type_lookup_func=None, macro_definition_func=None):
        self.__lexer = pycparser.c_lexer.CLexer(
            self._lex_error_func,
            self._lex_on_lbrace_func,
            self._lex_on_rbrace_func,
            self._lex_type_lookup_func
        )

        self.__type_lookup_func = type_lookup_func

        self.__lexer.build(optimize=True)

        if '\\' not in self.__lexer.lexer.lexliterals:
            self.__lexer.lexer.lexliterals += '\\'

    def process(self, code):
        code = remove_comments(code)
        self.__last_error = None
        self.__lexer.input(code)
        lines = code.splitlines()
        tokens = []
        while True:
            token = self.__lexer.token()
            if token is None:
                break
            tokens.append(token)
        directive_start = None
        directive_start_index = None
        directive_end_index = None
        directive_line_end = None
        block_range_list = []
        for index in range(len(tokens)):
            token = tokens[index]
            if directive_start is not None:
                if token.lineno != directive_line_end:
                    directive_end_index = index
                    block_range_list.append((directive_start.lineno - 1, directive_line_end, directive_start_index, directive_end_index))
                    directive_start = None
                    directive_start_index = None
            if token.type == 'PPHASH':
                if index > 0 and tokens[index - 1].lineno == token.lineno:
                    continue
                if directive_start is not None:
                    continue
                directive_start = token
                directive_start_index = index
                directive_line_end = directive_start.lineno
                continue
            if token.type == '\\':
                if index < len(tokens) - 1 and tokens[index + 1].lineno != token.lineno:
                    directive_line_end = token.lineno + 1
                    continue
        block_list = []
        last_source_line = 0
        for block_range in block_range_list:
            if block_range[0] > last_source_line:
                block_list.append(CPreprocessor.Source(code='\n'.join(lines[last_source_line:block_range[0]])))
            block_list.append(CPreprocessor.Directive(code='\n'.join([x.rstrip('\\') for x in lines[block_range[0]:block_range[1]]]), tokens=tokens[block_range[2]:block_range[3]]))
            last_source_line = block_range[1]
        # block_list now contains array of object wrappers:
        # If the wrapper is source it is C source code to be parsed. It won't contain any preprocessor directive lines
        # If the wrapper is directive, it is a C Preprocessor directive. The directive will have code containing the source text,
        # but also contains token lists for that source. This list can be used to parse the directive:
        # The token.value after the PPHASH (whatever the token.type is), is defines the preprocessor directive. Tokens can be used to
        # parse that directive and compile it:
        # The #if/#ifdef/#ifndef ... #elif ... #endif will define conditional
        # The #define can define object or function macros
        # Other directives are ignored and assumed not to form blocks
        j = 0

    def _lex_error_func(self, message, line, column):
        raise CPreprocessor.ParseError('%d:%d:%s' % (line, column, message))

    def _lex_on_lbrace_func(self):
        pass

    def _lex_on_rbrace_func(self):
        pass

    def _lex_type_lookup_func(self, name):
        if callable(self.__type_lookup_func):
            if self.__type_lookup_func(name):
                return True
        return False


def remove_comments(code):
    code = REGEXP_MULTILINE_COMMENT.sub('', code)
    code = [REGEXP_SINGLELINE_COMMENT.sub('', line) for line in code.splitlines()]
    code = '\n'.join(code)
    return code


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
