import re
import pycparser
import pycparser.c_ast
import pycparser.c_generator
from .xml_parser import Node, parse_xml
from .code import get_preprocessor_lines
from .platform import basic_ctypes, platform_ctypes, object_macro_map, func_macro_map, ctypes_map, handle_type_map, CType, CComplexType, CFunctionPointerType


class Generator:
    class Error(RuntimeError):
        def __init__(self, *args, **kwargs):
            super().__init__(*args)
            self.__dict__.update(**kwargs)

    class Code(pycparser.c_ast.Node):
        __slots__ = ('code', 'coord', '__weakref__')

        def __init__(self, code):
            self.code = code

    class CGenerator(pycparser.c_generator.CGenerator):
        def visit_Code():
            return node.code

    def __init__(self):
        self.ctypes_map = {**basic_ctypes, **platform_ctypes}

        class CParser(pycparser.CParser):
            def _lex_type_lookup_func(parser, name):
                if super()._lex_type_lookup_func(name):
                    return True
                return name in self.ctypes_map

        self.object_macro_map = dict(object_macro_map)
        self.func_macro_map = dict(func_macro_map)
        self.root_node_list = []
        self.alias_map = {}
        self.enum_node_map = {}
        self.value_node_map = {}
        self.bitmask_node_map = {}
        self.handle_node_map = {}
        self.struct_node_map = {}
        self.union_node_map = {}
        self.callback_node_map = {}
        self.command_node_map = {}
        self.enum_value_node_map = {}
        self.cparser = CParser()
        self.cgenerator = Generator.CGenerator()

    def make_path(self, node):
        names = []
        while node is not None:
            names.append('<%s>' % node.node_name)
            node = node.parent_node
        return '/'.join(names)

    def multiple_children_error(self, node, child_name):
        child_count = len(node.children[child_name])
        return Generator.Error('In %s: Expected a single child <%s>, but found %d children' % (self.make_path(node), child_name, child_count), node=node)

    def get_node_name(self, node):
        if node.has_attribute('name'):
            return node.get_attribute('name')
        if 'name' in node.children:
            if len(node.children['name']) > 1:
                raise self.multiple_children_error(node, 'name')
            return node.get('name').get_text()
        raise Generator.Error('In %s: Missing name' % self.make_path(node), node=node)

    def get_node_name_from_children(self, node):
        if 'name' not in node.children:
            raise Generator.Error('In %s: Missing child <name>' % self.make_path(node), node=node)
        if len(node.children['name']) > 1:
            raise self.multiple_children_error(node, 'name')
        return node.get('name').get_text()
    
    def get_node_name_from_attribute(self, node):
        if not node.has_attribute('name'):
            raise Generator.Error('In %s: Missing attribute @name' % self.make_path(node), node=node)
        return node.get_attribute('name')

    def save_alias(self, name, alias):
        if name in self.alias_map:
            if self.alias_map[name] != alias:
                raise Generator.Error('Duplicate alias "%s": The referred alias "%s" does not match previously defined value "%s"' % (name, alias, self.alias_map[alias]))
        else:
            self.alias_map[name] = alias
    
    def save_node_in_map(self, target_map, name, node):
        if name in target_map:
            map_name = None
            for key in dir(self):
                if getattr(self, key) is target_map:
                    map_name = key
                    break
            else:
                raise Generator.Error('In %s: Duplicate key "%s"' % (self.make_path(node), name), node=node)
            raise Generator.Error('In %s: Duplicate key "%s" in self.%s' % (self.make_path(node), name, map_name), node=node)
        target_map[name] = node
    
    def process_alias_node(self, node):
        assert node.has_attribute('alias')
        name = get_node_name_from_attribute(node)
        alias = node.get_attribute('alias')
        self.save_alias(name, alias)

    def add_xml_file(self, file):
        root_node = parse_xml(file, is_file=True)
        self.root_node_list.append(root_node)

        for types_node in root_node.get_all('types'):
            for type_node in types_node.get_all('type'):
                category = type_node.get_attribute('category')
                if category == 'define':
                    name = self.get_node_name(type_node)
                    code = type_node.get_text()
                    code = get_preprocessor_lines(code)
                    if len(code) > 1:
                        raise Generator.Error('In %s: found %d preprocessor lines in <type category="define">' % (self.make_path(type_node), len(code)))
                    if len(code) < 1:
                        # Note: Some <type category="define"> nodes might be present but commented out.
                        continue
                    func_macro = re.fullmatch('\s*#\s*define\s+(\w+)\(([^)]+)\)(.*)', code)
                    if func_macro is not None:
                        macro_name = func_macro.group(1)
                        if macro_name != name:
                            raise Generator.Error('In %s: Parsing definition "%s" found a macro with different name "%s"' % (self.make_path(type_node), name, macro_name))
                        args = [arg.strip() for arg in func_macro.group(2).split(',')]
                        code = func_macro.group(3)
                        code = [re.split(r'\b', x) for x in code.split('##')]
                        template = []
                        for words in code:
                            for word in words:
                                template.append(word)
                        index = 0
                        while index < len(template):
                            word = template[index]
                            if word in args:
                                if index > 0 and template[index - 1] == '#':
                                    template[index] = {
                                        'name': word,
                                        'index': args.index(word),
                                        'string': True
                                    }
                                    template.pop(index - 1)
                                    continue
                                template[index] = {
                                    'name': word,
                                    'index': args.index(word),
                                    'string': False
                                }
                            index += 1
                        if name in self.func_macro_map or name in self.object_macro_map:
                            raise Generator.Error('In %s: Duplicate preprocessor #define "%s"' % (self.make_path(type_node), name))
                        self.func_macro_map[name] = {
                            'arguments': args,
                            'template': template
                        }
                    else:
                        object_macro = re.fullmatch('\s*#\s*define\s+(\w+)\s+(.*)', code)
                        if object_macro is None:
                            raise Generator.Error('In %s: Unable to parse preprocessor #define' % (self.make_path(type_node)))
                        macro_name = object_macro.group(1)
                        if macro_name != name:
                            raise Generator.Error('In %s: Parsing definition "%s" found a macro with different name "%s"' % (self.make_path(type_node), name, macro_name))
                        code = object_macro.group(2)
                        if name in self.func_macro_map or name in self.object_macro_map:
                            raise Generator.Error('In %s: Duplicate preprocessor #define "%s"' % (self.make_path(type_node), name))
                        self.object_macro_map[name] = code
                    continue

                elif category == 'basetype':
                    if type_node.has_attribute('alias'):
                        self.process_alias_node(type_node)
                    else:
                        name = self.get_node_name(type_node)
                        if name in self.ctypes_map:
                            continue
                        words = [x.strip() for x in re.split(r'\b', ''.join([x.node_value for x in type_node.get_text_nodes_before(type_node.get('name'))]))]
                        words = [x for x in words if x]
                        if 'typedef' not in words:
                            if words[-1] == 'struct':
                                self.ctypes_map[name] = CType()
                                continue
                            raise GeneratorError('In %s: Basetype "%s" not a typedef or struct' % (self.make_path(type_node), name))
                        words = words[len(words) - words[::-1].index('typedef'):]
                        ctype = ' '.join(words).strip()
                        ptr_count = 0
                        while ctype.endswith('*'):
                            ctype = ctype[:-1].strip()
                            ptr_count += 1
                        if 'struct' in words:
                            ctype = CType()
                        elif ctype in self.ctypes_map:
                            ctype = self.ctypes_map[ctype]
                        else:
                            raise GeneratorError('In %s: Basetype "%s" is a typedef to an unknown type "%s"' % (self.make_path(type_node), name, ctype))
                        while ptr_count > 0:
                            ctype = ctype.pointer()
                            ptr_count -= 1
                        self.ctypes_map[name] = ctype
                        continue

                # Note on bitmask: The bitmask define a type and potential aliases, but they do not define any values.
                # The values are defined by enum name referred by <enums type="bitmask"> node.
                # For example: <type category="bitmask" requires="VkQueryControlFlagBits">...<name>VkQueryControlFlags</name></type>
                # "VkQueryControlFlags" is a type, but not enum. An enum "VkQueryControlFlagBits" defines the values:
                # There will be <type name="VkQueryControlFlagBits" category="enum"/>
                # And there will be <enums name="VkQueryControlFlagBits" type="bitmask">
                # Not every mask will have associated enum to it (some bitmask are types with no bits, but reserved for future use)
                # When it has bits they will be defined in @bitvalues or @requires attribute, specifying enum name

                elif category == 'bitmask':
                    if type_node.has_attribute('alias'):
                        self.process_alias_node(type_node)
                    else:
                        name = self.get_node_name_from_children(type_node)
                        self.save_node_in_map(self.bitmask_node_map, name, type_node)
                elif category == 'handle':
                    if type_node.has_attribute('alias'):
                        self.process_alias_node(type_node)
                    else:
                        name = self.get_node_name_from_children(type_node)
                        self.save_node_in_map(self.handle_node_map, name, type_node)

                elif category == 'enum':
                    if type_node.has_attribute('alias'):
                        self.process_alias_node(type_node)
                    else:
                        name = self.get_node_name_from_attribute(type_node)
                        self.save_node_in_map(self.enum_node_map, name, type_node)
                
                elif category == 'struct':
                    if type_node.has_attribute('alias'):
                        self.process_alias_node(type_node)
                    else:
                        name = self.get_node_name_from_attribute(type_node)
                        self.save_node_in_map(self.struct_node_map, name, type_node)

                elif category == 'union':
                    if type_node.has_attribute('alias'):
                        self.process_alias_node(type_node)
                    else:
                        name = self.get_node_name_from_attribute(type_node)
                        self.save_node_in_map(self.union_node_map, name, type_node)

                elif category == 'funcpointer':
                    if type_node.has_attribute('alias'):
                        self.process_alias_node(type_node)
                    else:
                        name = self.get_node_name_from_children(type_node)
                        self.save_node_in_map(self.callback_node_map, name, type_node)

        for enums_node in root_node.get_all('enums'):
            if not enums_node.has_attribute('name'):
                raise GeneratorError('In <registry>/<enums>: Missing attribute @name')
            enums_name = enums_node.get_attribute('name')
            enums_type = enums_node.get_attribute('type')
            target_map = None
            if enums_type == 'enum':
                target_map = self.enum_value_map
            elif enums_type == 'bitmask':
                target_map = self.bitmask_value_map
            elif enums_type is None:
                target_map = self.const_value_map
            else:
                raise GeneratorError('In <registry>/<enums name="%s">: Unknown type "%s"' % (enums_name, enums_type))
            for enum_node in enums_node.get_all('enum'):
                enum_name = enum_node.get_attribute('name')
                if enum_name is None:
                    raise GeneratorError('In <registry>/<enums name="%s">/<enum name="%s">: Missing attribute @name' % (enums_name, enum_name))
                if enum_node.has_attribute('alias'):
                    alias = enum_node.get_attribute('alias')
                    if enum_name in self.alias_map:
                        if self.alias_map[enum_name] != alias:
                            raise GeneratorError('In <registry>/<enums name="%s">/<enum name="%s" alias>: Duplicate alias "%s" of "%s", previously declared of "%s"' % (enums_name, enum_name, enum_name, alias, self.alias_map[enum_name]))
                    else:
                        self.alias_map[enum_name] = alias
                else:
                    if enum_name in target_map:
                        raise GeneratorError('In <registry>/<enums name="%s">/<enum name="%s">: Duplicate const value "%s"' % (enums_name, enum_name, enum_name))
                    target_map[enum_name] = {
                        'name': enum_name,
                        'node': enum_node,
                        'enums_node': enums_node,
                        'enums_name': enums_name
                    }

        for commands_node in root_node.get_all('commands'):
            for command_node in commands_node.get_all('command'):
                if command_node.has_attribute('alias'):
                    name = command_node.get_attribute('name')
                    if name is None:
                        raise GeneratorError('In <registry>/<commands>/<command alias>: Missing attribute @name')
                    if name in self.alias_map:
                        if self.alias_map[name] != alias:
                            raise GeneratorError('In <registry>/<commands>/<command alias>: Duplicate alias "%s" of "%s", previously declared of "%s"' % (name, alias, self.alias_map[name]))
                    else:
                        self.alias_map[name] = alias
                else:
                    name = command_node.get('proto').get('name').get_text()
                    if name in self.command_map:
                        raise GeneratorError('In <registry>/<commands>/<command name="%s">: Duplicate command' % (name))
                    self.command_map[name] = {
                        'name': name,
                        'node': command_node
                    }
    
    def compile(self):
        self.compile_value_map()

    def compile_value_map(self):
        self.compile_const_value_map()
    
    def compile_const_value_map(self):
        for name, record in self.const_value_map.items():
            node = record['node']
            value = self.get_enum_value(node)
            if name in self.value_map:
                raise GeneratorError('Duplicate value "%s"' % name)
            self.value_map[name] = value
    
    def compile_enum_value_map(self):

    
    def get_enum_value(node):
        if node.has_attribute('bitpos'):
            bitpos = self.parse_c_int(node.get_attribute('bitpos'))
            return 1 << bitpos
        if node.has_attribute('value'):
            value = self.get_c_constant_value('int', node.get_attribute('value'))
            return value
        raise GeneratorError('Missing enum value: Neither @value, nor @bitpos pressent')
        
    
    def preprocess_c_ast(self, node):
        has_substitution = False
        for name, child_node in parent_node.children():
            if type(child_node) is pycparser.c_ast.ID and child_node.name in self.object_macro_map:
                setattr(node, name, Generator.Code(self.object_macro_map[child_node.name]))
                has_substitution = True
                continue
            if type(child_node) is pycparser.c_ast.FuncCall and child_node.name.name in self.func_macro_map:
                args = [self.cgenerator.visit(x) for x in child_node.args]
                template = self.func_macro_map[child_node.name.name]
                code = []
                for part in template:
                    if isinstance(part, str):
                        code.append(part)
                    else:
                        assert isinstance(part, dict)
                        code.append(args[part['index']])
                code = ''.join(code)
                setattr(node, name, Generator.Code(code))
                has_substitution = True
                continue
            has_descendant_substitution = self.preprocess_c_ast(child_node)
            has_substitution = has_substitution or has_descendant_substitution
        return has_substitution

    def preprocess_c_code(self, code):
        ast = self.cparser.parse(code)
        while self.preprocess_c_ast(ast):
            code = self.cgenerator.visit(ast)
            ast = self.cparser.parse(code)
        return code

    def get_c_constant_value(self, ctype, value):
        assert ctype in self.ctypes_map
        code = '%s value = %s;' % (ctype, value)
        code = self.preprocess_c_code(self, code)
        ast = self.cparser.parse(code)
        return get_c_ast_const_value(ast.ext[0].init)

    def get_c_ast_const_value(self, node):
        node_type = type(node)
        c_ast = pycparser.c_ast
        if node_type is c_ast.Constant:
            if 'int' in node.type:
                return self.parse_c_int(node.value)
            if node.type in ['float', 'double']:
                return self.parse_c_float(node.value)
            if node.type == 'string':
                return self.parse_c_string(node.value)
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
            if node.op == '<<':
                return self.get_c_ast_const_value(node.left) << self.get_c_ast_const_value(node.right)
        elif node_type is c_ast.Cast:
            target_type = self.cgenerator.visit(node_type.to_type)
            assert target_type in self.ctypes_map
            value = self.get_c_ast_const_value(node.expr)
            return self.ctypes_map[target_type].make_python_value(value)

    @staticmethod
    def parse_c_int(value):
        match = re.match(r'0x([0-9A-Fa-f]+)', value)
        if match:
            return int(match.group(0), 16)
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

    @staticmethod
    def parse_c_string(value):
        if len(value) < 2 or value[0] != '"' or value[-1] != '"':
            raise ValueError('Invalid string value (missing open or close quotes): %s' % value)
        value = value[1:-1]

        value = re.sub(r'\\U([0-9A-Fa-f]{8})', subst_unicode_hex, value)
        value = re.sub(r'\\u([0-9A-Fa-f]{4})', subst_unicode_hex, value)
        value = re.sub(r'\\x([0-9A-Fa-f]{2})', subst_unicode_hex, value)
        value = re.sub(r'\\([0-7]{3})', subst_unicode_oct, value)
        value = re.sub(r'\\(.)', subst_slash_escape, value)
        return value.encode('utf-8')


def subst_unicode_hex(match):
    return chr(int(match.group(1), 16))

def subst_unicode_oct(match):
    return chr(int(match.group(1), 8))

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
    seq = match.group(1)
    if seq in subst_table:
        return chr(subst_table[seq])
    return match.group(0)