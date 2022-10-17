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
        self.struct_map = {}
        self.enum_value_map = {}
        self.bitmask_value_map = {}
        self.const_value_map = {}

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

                    if types_type_node.get_attribute('category') in ['struct', 'union']:
                        if types_type_node.has_attribute('alias'):
                            if not types_type_node.has_attribute('name'):
                                raise Model.XmlSyntaxError('Missing required attribute @%s for @alias="%s" in %s' % ('name', types_type_node.get_attribute('alias'), make_path(types_type_node)))
                            self.alias_map[types_type_node.get_attribute('name')] = types_type_node.get_attribute('alias')
                            continue
                        if not types_type_node.has_attribute('name'):
                            raise Model.XmlSyntaxError('Missing required attribute @%s in %s' % ('name', make_path(types_type_node)))
                        name = types_type_node.get_attribute('name')
                        class_name = 'ctypes.Structure' if types_type_node.get_attribute('category') == 'struct' else 'ctypes.Union'
                        struct = self.struct_map[name] = {
                            'name': name,
                            'node': types_type_node,
                            'member_map': {},
                            'member_list': []
                        }
                        for member_node in types_type_node.get_all('member'):
                            if 'name' not in types_type_node.children:
                                raise Model.XmlSyntaxError('Missing required element <%s> in %s' % ('name', make_path(types_type_node)))
                            member_name = member_node.get('name').get_text()
                            member = {
                                'name': member_name,
                                'node': member_node
                            }
                            if 'type' in member_node.children:
                                member['type'] = member_node.get('type').get_text()
                            struct['member_map'][member_name] = member
                            struct['member_list'].append(member_name)
            
            for enums_node in xml.get_all('enums'):
                if enums_node.get_attribute('type') is None:
                    # List of constants: in this case enums node is meaningless, the constants itself define the values
                    for enum_node in enums_node.get_all('enum'):
                        if not enum_node.has_attribute('name'):
                                raise Model.XmlSyntaxError('Missing required attribute @%s in %s' % ('name', make_path(enum_node)))
                        name = enum_node.get_attribute('name')
                        if enum_node.has_attribute('alias'):
                            self.alias_map[name] = enum_node.get_attribute('alias')
                            continue
                        self.const_value_map[name] = {
                            'name': name,
                            'node': enum_node
                        }
                        continue
                elif enums_node.get_attribute('type') == 'enum':
                    target_map = self.enum_value_map
                elif enums_node.get_attribute('type') == 'bitmask':
                    target_map = self.bitmask_value_map
                else:
                    raise Model.XmlSyntaxError('Unknown enums @type "%s" in %s' % (enums_node.get_attribute('type'), make_path(enums_node)))
                if not enums_node.has_attribute('name'):
                    raise Model.XmlSyntaxError('Missing required attribute @%s in %s' % ('name', make_path(enums_node)))
                enums_name = enums_node.get_attribute('name')
                enums_entry = target_map[enums_name] = {
                    'name': enums_name,
                    'node': enums_node,
                    'values': {}
                }
                for enum_node in enums_node.get_all('enum'):
                    if not enum_node.has_attribute('name'):
                        raise Model.XmlSyntaxError('Missing required attribute @%s in %s' % ('name', make_path(enum_node)))
                    enum_name = enum_node.get_attribute('name')
                    if enum_node.has_attribute('alias'):
                        self.alias_map[enum_name] = enum_node.get_attribute('alias')
                        continue
                    enums_entry['values'][enum_name] = {
                        'name': enum_name,
                        'node': enum_node
                    }
