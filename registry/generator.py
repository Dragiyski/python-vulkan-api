import re
import pycparser
import pycparser.c_ast
import pycparser.c_generator
from .xml_parser import Node, parse_xml
from .code import get_preprocessor_lines
from .platform import basic_ctypes, platform_ctypes, object_macro_map, func_macro_map, ctypes_map, handle_type_map, CType, CComplexType, CFunctionPointerType


class GeneratorError(RuntimeError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.__dict__.update(**kwargs)


class Generator:
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
        self.root_nodes = []
        self.alias_map = {}
        self.bitmask_map = {}
        self.handle_map = {}
        self.enum_map = {}
        self.struct_map = {}
        self.union_map = {}
        self.callback_map = {}
        self.enum_value_map = {}
        self.bitmask_value_map = {}
        self.const_value_map = {}
        self.value_map = {}
        self.command_map = {}
        self.cparser = CParser()
        self.cgenerator = Generator.CGenerator()

    def add_xml_file(self, file):
        root_node = parse_xml(file, is_file=True)
        self.root_nodes.append(root_node)

        for types_node in root_node.get_all('types'):
            for type_node in types_node.get_all('type'):
                category = type_node.get_attribute('category')
                if category == 'define':
                    if type_node.has_attribute('name'):
                        name = type_node.get_attribute('name')
                    elif 'name' in type_node.children:
                        if len(type_node.children['name']) > 1:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: multiple name childrens' % (category))
                        name = type_node.get('name').get_text()
                    else:
                        raise GeneratorError('In <registry>/<types>/<type category="%s">: missing name' % (category))
                    if name not in self.object_macro_map and name not in self.func_macro_map:
                        code = type_node.get_text()
                        code = get_preprocessor_lines(type_node.get_text())
                        if len(code) > 1:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: unable to parse define node' % (category))
                        elif len(code) < 1:
                            continue
                        code = code[0]
                        func_macro = re.fullmatch('\s*#\s*define\s+(\w+)\s*\(([^)]+)\)(.*)', code)
                        if func_macro is not None:
                            macro_name = func_macro.group(1)
                            if macro_name != name:
                                raise GeneratorError('Parsed macro name "%s" does not match defined macro name "%s"' % (macro_name, name))
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
                            self.func_macro_map[macro_name] = {
                                'arguments': args,
                                'template': template
                            }
                        else:
                            object_macro = re.fullmatch('\s*#\s*define\s+(\w+)\s+(.*)', code)
                            if object_macro is None:
                                raise GeneratorError('In <registry>/<types>/<type category="%s">: unable to parse define node' % (category))
                            self.object_macro_map[object_macro.group(1)] = object_macro.group(2)

                elif category == 'basetype':
                    if type_node.has_attribute('alias'):
                        name = type_node.get_attribute('name')
                        if name is None:
                            raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Missing attribute @name' % (category))
                        alias = type_node.get_attribute('alias')
                        if name in self.alias_map:
                            if self.alias_map[name] != alias:
                                raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Duplicate alias "%s" of "%s", previously declared of "%s"' % (category, name, alias, self.alias_map[name]))
                        else:
                            self.alias_map[name] = alias
                    else:
                        if 'name' not in type_node.children:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Missing child <name>' % (category))
                        elif len(type_node.children['name']) > 1:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate child <name>' % (category))
                        name = type_node.get('name').get_text()
                        if name in self.ctypes_map:
                            continue
                        words = [x.strip() for x in re.split(r'\b', ''.join([x.node_value for x in type_node.get_text_nodes_before(type_node.get('name'))]))]
                        words = [x for x in words if x]
                        if 'typedef' not in words:
                            if words[-1] == 'struct':
                                self.ctypes_map[name] = CType()
                                continue
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Not a typedef or struct' % (category))
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
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: typedef not a base type' % (category))
                        while ptr_count > 0:
                            ctype = ctype.pointer()
                            ptr_count -= 1
                        self.ctypes_map[name] = ctype

                    # Register bitmask and enum nodes (where all enum nodes are c_int, but bitmasks bits can be c_uint64 or c_uint32)
                    # Bitmask bits will be registered later
                    # Finally, add struct and union *prior resolving members*. They are always CComplexType, which will have initially
                    # member_map and member_list empty

                elif category == 'bitmask':
                    if type_node.has_attribute('alias'):
                        name = type_node.get_attribute('name')
                        if name is None:
                            raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Missing attribute @name' % (category))
                        alias = type_node.get_attribute('alias')
                        if name in self.alias_map:
                            if self.alias_map[name] != alias:
                                raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Duplicate alias "%s" of "%s", previously declared of "%s"' % (category, name, alias, self.alias_map[name]))
                        else:
                            self.alias_map[name] = alias
                    else:
                        if 'name' not in type_node.children:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Missing child <name>' % (category))
                        elif len(type_node.children['name']) > 1:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate child <name>' % (category))
                        name = type_node.get('name').get_text()
                        if name in self.ctypes_map:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate entry for %s' % (category, name))
                        if 'type' not in type_node.children:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Missing child <type>' % category)
                        elif len(type_node.children['type']) > 1:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate child <type>' % category)
                        ctype = type_node.get('type').get_text()
                        if ctype not in self.ctypes_map:
                            raise GeneratorError('In <registry>/<types>/<type category="bitmask" name="%s">: Unknown type: %s' % (name, ctype))
                        self.ctypes_map[name] = self.ctypes_map[ctype]
                        self.bitmask_map[name] = {
                            'name': name,
                            'ctype': ctype,
                            'node': type_node
                        }

                elif category == 'handle':
                    if type_node.has_attribute('alias'):
                        name = type_node.get_attribute('name')
                        if name is None:
                            raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Missing attribute @name' % (category))
                        alias = type_node.get_attribute('alias')
                        if name in self.alias_map:
                            if self.alias_map[name] != alias:
                                raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Duplicate alias "%s" of "%s", previously declared of "%s"' % (category, name, alias, self.alias_map[name]))
                        else:
                            self.alias_map[name] = alias
                    else:
                        if 'name' not in type_node.children:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Missing child <name>' % (category))
                        elif len(type_node.children['name']) > 1:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate child <name>' % (category))
                        name = type_node.get('name').get_text()
                        if name in self.ctypes_map:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate handle "%s"' % (category, name))
                        if 'type' not in type_node.children:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Missing child <type>' % (category))
                        elif len(type_node.children['type']) > 1:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate child <type>' % (category))
                        handle_type = type_node.get('type').get_text()
                        if handle_type not in handle_type_map:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Unknown handle type "%s%' % (category, handle_type))
                        self.ctypes_map[name] = handle_type_map[handle_type]
                        self.handle_map[name] = {
                            'name': name,
                            'type': handle_type,
                            'node': type_node
                        }

                elif category == 'enum':
                    if type_node.has_attribute('alias'):
                        name = type_node.get_attribute('name')
                        if name is None:
                            raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Missing attribute @name' % (category))
                        alias = type_node.get_attribute('alias')
                        if name in self.alias_map:
                            if self.alias_map[name] != alias:
                                raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Duplicate alias "%s" of "%s", previously declared of "%s"' % (category, name, alias, self.alias_map[name]))
                        else:
                            self.alias_map[name] = alias
                    else:
                        name = type_node.get_attribute('name')
                        if name is None:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Missing attribute @name' % (category))
                        if name in self.ctypes_map:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate enum "%s" (already present in ctypes_map)' % (category, name))
                        if name in self.enum_map:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate enum "%s" (already present in enum_map)' % (category, name))
                        self.ctypes_map[name] = ctypes_map['c_int']
                        self.enum_map[name] = {
                            'name': name,
                            'type_node': type_node
                        }

                elif category in ['struct', 'union']:
                    if type_node.has_attribute('alias'):
                        name = type_node.get_attribute('name')
                        if name is None:
                            raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Missing attribute @name' % category)
                        alias = type_node.get_attribute('alias')
                        if name in self.alias_map:
                            if self.alias_map[name] != alias:
                                raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Duplicate alias "%s" of "%s", previously declared of "%s"' % (category, name, alias, self.alias_map[name]))
                        else:
                            self.alias_map[name] = alias
                    else:
                        constructor = 'Union' if category == 'union' else 'Structure'
                        target_map = self.union_map if category == 'union' else self.struct_map
                        name = type_node.get_attribute('name')
                        if name is None:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Missing attribute @name' % (category))
                        if name in self.ctypes_map:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate enum "%s" (already present in ctypes_map)' % (category, name))
                        if name in target_map:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate enum "%s" (already present in target_map)' % (category, name))
                        self.ctypes_map[name] = CComplexType(name, constructor)
                        target_map[name] = {
                            'name': name,
                            'class': constructor,
                            'node': type_node
                        }

                elif category == 'funcpointer':
                    category = type_node.get_attribute('category')
                    if type_node.has_attribute('alias'):
                        name = type_node.get_attribute('name')
                        if name is None:
                            raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Missing attribute @name' % (category))
                        alias = type_node.get_attribute('alias')
                        if name in self.alias_map:
                            if self.alias_map[name] != alias:
                                raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Duplicate alias "%s" of "%s", previously declared of "%s"' % (category, name, alias, self.alias_map[name]))
                        else:
                            self.alias_map[name] = alias
                    else:
                        if 'name' not in type_node.children:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Missing child <name>' % (category))
                        elif len(type_node.children['name']) > 1:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate child <name>' % (category))
                        name = type_node.get('name').get_text()
                        if name in self.ctypes_map:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Type conflict "%s"' % (category, name))
                        if name in self.callback_map:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate function pointer "%s"' % (category, name))
                        self.ctypes_map[name] = CFunctionPointerType(name)
                        self.callback_map[name] = {
                            'name': name,
                            'node': type_node
                        }

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
                        'node': enum_node
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
