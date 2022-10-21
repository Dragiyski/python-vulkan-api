import re
from .xml_parser import Node, parse_xml
from .code import get_preprocessor_lines, CParser, CPreprocessor
from .platform import basic_ctypes, platform_ctypes, object_macro_map, func_macro_map

class GeneratorError(RuntimeError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.__dict__.update(**kwargs)

class Generator:

    def __init__(self):
        self.ctype_map = {**basic_ctypes, **platform_ctypes}
        self.object_macro_map = dict(object_macro_map)
        self.func_macro_map = dict(func_macro_map)
        self.root_nodes = []
        self.alias_map = {}
        self.cparser = CParser()
        self.cpreprocessor = CPreprocessor()
        
    def add_xml_file(self, file):
        root_node = parse_xml(file, is_file=True)
        self.root_nodes.append(root_node)
        
        for types_node in root_node.get_all('types'):
            for type_node in types_node.get_all('type'):
                if type_node.get_attribute('category') == 'define':
                    if type_node.has_attribute('name'):
                        name = type_node.get_attribute('name')
                    elif 'name' in type_node.children:
                        if len(type_node.children['name']) > 1:
                            raise GeneratorError('In <registry>/<types>/<type category="define">: multiple name childrens', node=type_node)
                        name = type_node.get('name').get_text()
                    else:
                        raise GeneratorError('In <registry>/<types>/<type category="define">: missing name', node=type_node)
                    if name not in self.object_macro_map and name not in self.func_macro_map:
                        code = type_node.get_text()
                        ast = self.cpreprocessor.process(code)
                        code = get_preprocessor_lines(type_node.get_text())
                        if len(code) > 1:
                            raise GeneratorError('In <registry>/<types>/<type category="define">: unable to parse define node')
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
                                raise GeneratorError('In <registry>/<types>/<type category="define">: unable to parse define node')
                            self.object_macro_map[object_macro.group(1)] = object_macro.group(2)
                
                elif type_node.get_attribute('category') == 'basetype':
                    if type_node.has_attribute('alias'):
                        name = type_node.get_attribute('name')
                        if name is None:
                            raise GeneratorError('In <registry>/<types>/<type category="basetype" alias>: Missing attribute @name', node=type_node)
                        alias = type_node.get_attribute('alias')
                        if name in self.alias_map:
                            if self.alias_map[name] != alias:
                                raise GeneratorError('In <registry>/<types>/<type category="basetype" alias>: Duplicate alias "%s" of "%s", previously declared of "%s"' % (name, alias, self.alias_map[name]), node=type_node)
                        else:
                            self.alias_map[name] = alias
                    else:
                        if 'name' not in type_node.children:
                            raise GeneratorError('In <registry>/<types>/<type category="basetype">: Missing child <name>')
                        elif len(type_node.children['name']) > 1:
                            raise GeneratorError('In <registry>/<types>/<type category="basetype">: Duplicate child <name>')
                        name = type_node.get('name').get_text()
