import re
from .xml_parser import Node, parse_xml
from .code import get_preprocessor_lines, CParser, CPreprocessor
from .platform import basic_ctypes, platform_ctypes, object_macro_map, func_macro_map, ctypes_map, handle_type_map, CType, CComplexType, CFunctionPointerType

class GeneratorError(RuntimeError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.__dict__.update(**kwargs)

class Generator:

    def __init__(self):
        self.ctypes_map = {**basic_ctypes, **platform_ctypes}
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
        self.cparser = CParser()
        
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
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: multiple name childrens' % (category), node=type_node)
                        name = type_node.get('name').get_text()
                    else:
                        raise GeneratorError('In <registry>/<types>/<type category="%s">: missing name' % (category), node=type_node)
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
                                raise GeneratorError('Parsed macro name "%s" does not match defined macro name "%s"' % (macro_name, name), node=type_node)
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
                            raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Missing attribute @name' % (category), node=type_node)
                        alias = type_node.get_attribute('alias')
                        if name in self.alias_map:
                            if self.alias_map[name] != alias:
                                raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Duplicate alias "%s" of "%s", previously declared of "%s"' % (category, name, alias, self.alias_map[name]), node=type_node)
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
                            raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Missing attribute @name' % (category), node=type_node)
                        alias = type_node.get_attribute('alias')
                        if name in self.alias_map:
                            if self.alias_map[name] != alias:
                                raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Duplicate alias "%s" of "%s", previously declared of "%s"' % (category, name, alias, self.alias_map[name]), node=type_node)
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
                            raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Missing attribute @name' % (category), node=type_node)
                        alias = type_node.get_attribute('alias')
                        if name in self.alias_map:
                            if self.alias_map[name] != alias:
                                raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Duplicate alias "%s" of "%s", previously declared of "%s"' % (category, name, alias, self.alias_map[name]), node=type_node)
                        else:
                            self.alias_map[name] = alias
                    else:
                        if 'name' not in type_node.children:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Missing child <name>' % (category))
                        elif len(type_node.children['name']) > 1:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate child <name>' % (category))
                        name = type_node.get('name').get_text()
                        if name in self.ctypes_map:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate handle "%s"' % (category, name), node=type_node)
                        if 'type' not in type_node.children:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Missing child <type>' % (category), node=type_node)
                        elif len(type_node.children['type']) > 1:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate child <type>' % (category), node=type_node)
                        handle_type = type_node.get('type').get_text()
                        if handle_type not in handle_type_map:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Unknown handle type "%s%' % (category, handle_type), node=type_node)
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
                            raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Missing attribute @name' % (category), node=type_node)
                        alias = type_node.get_attribute('alias')
                        if name in self.alias_map:
                            if self.alias_map[name] != alias:
                                raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Duplicate alias "%s" of "%s", previously declared of "%s"' % (category, name, alias, self.alias_map[name]), node=type_node)
                        else:
                            self.alias_map[name] = alias
                    else:
                        name = type_node.get_attribute('name')
                        if name is None:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Missing attribute @name' % (category), node=type_node)
                        if name in self.ctypes_map:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate enum "%s" (already present in ctypes_map)' % (category, name), node=type_node)
                        if name in self.enum_map:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate enum "%s" (already present in enum_map)' % (category, name), node=type_node)
                        self.ctypes_map[name] = ctypes_map['c_int']
                        self.enum_map[name] = {
                            'name': name,
                            'type_node': type_node
                        }
                
                elif category in ['struct', 'union']:
                    if type_node.has_attribute('alias'):
                        name = type_node.get_attribute('name')
                        if name is None:
                            raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Missing attribute @name' % category, node=type_node)
                        alias = type_node.get_attribute('alias')
                        if name in self.alias_map:
                            if self.alias_map[name] != alias:
                                raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Duplicate alias "%s" of "%s", previously declared of "%s"' % (category, name, alias, self.alias_map[name]), node=type_node)
                        else:
                            self.alias_map[name] = alias
                    else:
                        constructor = 'Union' if category == 'union' else 'Structure'
                        target_map = self.union_map if category == 'union' else self.struct_map
                        name = type_node.get_attribute('name')
                        if name is None:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Missing attribute @name' % (category), node=type_node)
                        if name in self.ctypes_map:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate enum "%s" (already present in ctypes_map)' % (category, name), node=type_node)
                        if name in target_map:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate enum "%s" (already present in target_map)' % (category, name), node=type_node)
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
                            raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Missing attribute @name' % (category), node=type_node)
                        alias = type_node.get_attribute('alias')
                        if name in self.alias_map:
                            if self.alias_map[name] != alias:
                                raise GeneratorError('In <registry>/<types>/<type category="%s" alias>: Duplicate alias "%s" of "%s", previously declared of "%s"' % (category, name, alias, self.alias_map[name]), node=type_node)
                        else:
                            self.alias_map[name] = alias
                    else:
                        if 'name' not in type_node.children:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Missing child <name>' % (category))
                        elif len(type_node.children['name']) > 1:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate child <name>' % (category))
                        name = type_node.get('name').get_text()
                        if name in self.ctypes_map:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Type conflict "%s"' % (category, name), node=type_node)
                        if name in self.callback_map:
                            raise GeneratorError('In <registry>/<types>/<type category="%s">: Duplicate function pointer "%s"' % (category, name), node=type_node)
                        self.ctypes_map[name] = CFunctionPointerType(name)
                        self.callback_map[name] = {
                            'name': name,
                            'node': type_node
                        }

            # TODO: At this point all types has been collected. Extensions cannot provide more types,
            # TODO: they can only extend the enums and categorize the existing types, i.e.
            # TODO: <type> nodes include everything (with all declared extensions) and extensions
            # TODO: just referrer to the specific types.

            # TODO: The following steps must be initiated in that order:
            # 1. Resolve <enums> node;
            # 2. Resolve enum extensions - might require existing enums values;
            # 3. Resolve structure members - might require enum from core or extensions*;
            # 4. Resolve function pointers - might require structures;
            # 5. Resolve commands

            # * Structure members can be:
            # <int type> <name> : <bit size> = (name, type, bitsize) in _fields_
            # <type> <name> = (name, type) in _fields_ - the trivial case
            # <type> <name>[size] = CArrayType - an array, potentially with size declared as enum constant.

            # <enums> node will have get_attribute('type') in ['enum', 'bitmask'] to signify its type.
            # If that is missing, the <enums> signify constant values.
            # Note: In C enum members are globals:
            # enum VkStructureType {
            #    VK_STRUCTURE_TYPE_APPLICATION_INFO = 0,...
            # }
            # will be at the same scope as:
            # const int VK_STRUCTURE_TYPE_APPLICATION_INFO = 0
            # as such enum member names will be unique and can be referred directly by structures, etc.
            # i.e. <enum>VK_STRUCTURE_TYPE_APPLICATION_INFO</enum> instead of <enum>VkStructureType.VK_STRUCTURE_TYPE_APPLICATION_INFO</enum>