import re
import sys
import ctypes
from ._xml_parser import parse_xml, Node, get_error_prefix
from ._platform import handle_ctypes, basic_ctypes
from pycparser import CParser, c_generator, c_ast


class Model:
    def XmlSyntaxError(RuntimeError):
        pass
    
    def __init__(self, *files):
        from ._platform import basic_ctypes, platform_ctypes
        self.xml = [parse_xml(file, is_file=True) for file in files]
        self.ctypes = {**basic_ctypes, **platform_ctypes}
        self.basic_ctypes = basic_ctypes

        self.alias_map = {}
        self.basetype_map = {}
        self.macro_map = {}
        self.bitmask_map = {}
        self.handle_map = {}
        self.enum_map = {}
        self.callback_map = {}

        def make_path(node):
            if node.parent_node is None:
                return node.node_name
            return '%s/%s' % (make_path(node.parent_node), node.node_name)

        for xml in self.xml:
            for types_node in xml.get_all('types'):
                for types_type_node in types_node.get_all('type'):
                    if types_type_node.get_attribute('category') == 'basetype':
                        if 'name' not in types_type_node.children:
                            continue
                        self.basetype_map[types_type_node.get('name')] = {
                            'name': types_type_node.get('name'),
                            'node': types_type_node
                        }

                    if types_type_node.get_attribute('category') == 'define':
                        if 'name' not in types_type_node.children:
                            continue
                        self.macro_map[types_type_node.get('name')] = {
                            'name': types_type_node.get('name'),
                            'node': types_type_node
                        }
                        
                    if types_type_node.get_attribute('category') == 'bitmask':
                        if types_type_node.has_attribute('alias'):
                            if not types_type_node.has_attribute('name'):
                                raise Model.XmlSyntaxError('Missing required attribute @%s for @alias="%s" in %s' % ('name', types_type_node.get_attribute('alias'), make_path(types_type_node)))
                            self.alias_map[types_type_node.get_attribute('name')] = types_type_node.get_attribute('alias')
                            continue
                        if 'name' not in types_type_node.children:
                            raise Model.XmlSyntaxError('Missing required element <%s> in %s' % ('name', make_path(types_type_node)))
                        name = types_type_node.get_attribute('name')
                        self.bitmask_map[name] = {
                            'name': name,
                            'type_node': types_type_node
                        }
                        
                    if types_type_node.get_attribute('category') == 'handle':
                        if types_type_node.has_attribute('alias'):
                            if not types_type_node.has_attribute('name'):
                                raise Model.XmlSyntaxError('Missing required attribute @%s for @alias="%s" in %s' % ('name', types_type_node.get_attribute('alias'), make_path(types_type_node)))
                            self.alias_map[types_type_node.get_attribute('name')] = types_type_node.get_attribute('alias')
                            continue
                        if 'name' not in types_type_node.children:
                            raise Model.XmlSyntaxError('Missing required element <%s> in %s' % ('name', make_path(types_type_node)))
                        name = types_type_node.get('name').get_text()
                        self.handle_map[name] = {
                            'name': name,
                            'node': types_type_node
                        }
                    
                    if types_type_node.get_attribute('category') == 'enum':
                        if types_type_node.has_attribute('alias'):
                            if not types_type_node.has_attribute('name'):
                                raise Model.XmlSyntaxError('Missing required attribute @%s for @alias="%s" in %s' % ('name', types_type_node.get_attribute('alias'), make_path(types_type_node)))
                            self.alias_map[types_type_node.get_attribute('name')] = types_type_node.get_attribute('alias')
                            continue
                        if not types_type_node.has_attribute('name'):
                            raise Model.XmlSyntaxError('Missing required attribute @%s in %s' % ('name', make_path(types_type_node)))
                        name = types_type_node.get_attribute('name')
                        self.enum_map[name] = {
                            'name': name,
                            'type_node': types_type_node
                        }
                        
                    if types_type_node.get_attribute('category') == 'funcpointer':
                        if types_type_node.has_attribute('alias'):
                            if not types_type_node.has_attribute('name'):
                                raise Model.XmlSyntaxError('Missing required attribute @%s for @alias="%s" in %s' % ('name', types_type_node.get_attribute('alias'), make_path(types_type_node)))
                            self.alias_map[types_type_node.get_attribute('name')] = types_type_node.get_attribute('alias')
                            continue
                        if 'name' not in types_type_node.children:
                            raise Model.XmlSyntaxError('Missing required element <%s> in %s' % ('name', make_path(types_type_node)))
                        name = types_type_node.get('name').get_text()
                        self.handle_map[name] = {
                            'name': name,
                            'node': types_type_node
                        }
                    
                    if types_type_node.get_attribute('category') == 'struct':
                        if types_type_node.has_attribute('alias'):
                            if not types_type_node.has_attribute('name'):
                                raise Model.XmlSyntaxError('Missing required attribute @%s for @alias="%s" in %s' % ('name', types_type_node.get_attribute('alias'), make_path(types_type_node)))
                            self.alias_map[types_type_node.get_attribute('name')] = types_type_node.get_attribute('alias')
                            continue
                        if not types_type_node.has_attribute('name'):
                            raise Model.XmlSyntaxError('Missing required attribute @%s in %s' % ('name', make_path(types_type_node)))
                        name = types_type_node.get_attribute('name')
