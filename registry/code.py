import pycparser
import re

REGEXP_MULTILINE_COMMENT = re.compile(r'\/\*.*\*\/')
REGEXP_SINGLELINE_COMMENT = re.compile(r'\/\/.*')

# TODO: Override CParser class with method p_pp_directive handling (see p_pppragma_directive for how preprocessor is handled in the AST)
# TODO: This might require additional pp_condition_stack which store the nodes for each "#if/#ifdef/#ifndef" directives, so that
# TODO: #elif and #else can be attached to any #if node on top of the stack. The #if must contain conditions:list (will have at least one element) and alternative: a block of expressions
# TODO: A condition will have the condition line (unparsed) and a list of expression similar to Compound statement

# TODO: Preprocessor is meant to be run once before actual code parsing.


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
