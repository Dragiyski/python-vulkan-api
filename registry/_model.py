import re
import sys
import ctypes
from ._xml_parser import parse_xml, Node, get_error_prefix
from ._platform import handle_ctypes, basic_ctypes
from pycparser import CParser, c_generator, c_ast


class Model:
    class XmlParseError(RuntimeError):
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
        
        def add_alias(name, alias, node):
            if name in self.alias_map:
                raise Model.XmlParseError('Duplicate entry "%s" for "%s" in %s' % (name, 'alias', make_path(types_type_node)))
            self.alias_map[name] = alias

        for xml in self.xml:
            for types_node in xml.get_all('types'):
                for types_type_node in types_node.get_all('type'):
                    if types_type_node.get_attribute('category') == 'basetype':
                        if 'name' not in types_type_node.children:
                            continue
                        name = types_type_node.get('name')
                        if name in self.basetype_map:
                            raise Model.XmlParseError('Duplicate entry "%s" for "%s" in %s' % (name, 'basetype', make_path(types_type_node)))
                        self.basetype_map[name] = {
                            'name': types_type_node.get('name'),
                            'node': types_type_node
                        }

                    if types_type_node.get_attribute('category') == 'define':
                        if 'name' not in types_type_node.children:
                            continue
                        name = types_type_node.get('name')
                        if name in self.macro_map:
                            raise Model.XmlParseError('Duplicate entry "%s" for "%s" in %s' % (name, 'define', make_path(types_type_node)))
                        self.macro_map[name] = {
                            'name': types_type_node.get('name'),
                            'node': types_type_node
                        }

                    if types_type_node.get_attribute('category') == 'bitmask':
                        if types_type_node.has_attribute('alias'):
                            if not types_type_node.has_attribute('name'):
                                raise Model.XmlParseError('Missing required attribute @%s for @alias="%s" in %s' % ('name', types_type_node.get_attribute('alias'), make_path(types_type_node)))
                            add_alias(types_type_node.get_attribute('name'), types_type_node.get_attribute('alias'), types_type_node)
                            continue
                        if 'name' not in types_type_node.children:
                            raise Model.XmlParseError('Missing required element <%s> in %s' % ('name', make_path(types_type_node)))
                        name = types_type_node.get('name')
                        if name in self.bitmask_map:
                            raise Model.XmlParseError('Duplicate entry "%s" for "%s" in %s' % (name, 'bitmask', make_path(types_type_node)))
                        self.bitmask_map[name] = {
                            'name': name,
                            'type_node': types_type_node
                        }

                    if types_type_node.get_attribute('category') == 'handle':
                        if types_type_node.has_attribute('alias'):
                            if not types_type_node.has_attribute('name'):
                                raise Model.XmlParseError('Missing required attribute @%s for @alias="%s" in %s' % ('name', types_type_node.get_attribute('alias'), make_path(types_type_node)))
                            add_alias(types_type_node.get_attribute('name'), types_type_node.get_attribute('alias'), types_type_node)
                            continue
                        if 'name' not in types_type_node.children:
                            raise Model.XmlParseError('Missing required element <%s> in %s' % ('name', make_path(types_type_node)))
                        name = types_type_node.get('name').get_text()
                        if name in self.handle_map:
                            raise Model.XmlParseError('Duplicate entry "%s" for "%s" in %s' % (name, 'handle', make_path(types_type_node)))
                        self.handle_map[name] = {
                            'name': name,
                            'node': types_type_node
                        }

                    if types_type_node.get_attribute('category') == 'enum':
                        if types_type_node.has_attribute('alias'):
                            if not types_type_node.has_attribute('name'):
                                raise Model.XmlParseError('Missing required attribute @%s for @alias="%s" in %s' % ('name', types_type_node.get_attribute('alias'), make_path(types_type_node)))
                            add_alias(types_type_node.get_attribute('name'), types_type_node.get_attribute('alias'), types_type_node)
                            continue
                        if not types_type_node.has_attribute('name'):
                            raise Model.XmlParseError('Missing required attribute @%s in %s' % ('name', make_path(types_type_node)))
                        name = types_type_node.get_attribute('name')
                        if name in self.enum_map:
                            raise Model.XmlParseError('Duplicate entry "%s" for "%s" in %s' % (name, 'enum', make_path(types_type_node)))
                        self.enum_map[name] = {
                            'name': name,
                            'type_node': types_type_node
                        }

                    if types_type_node.get_attribute('category') == 'funcpointer':
                        if types_type_node.has_attribute('alias'):
                            if not types_type_node.has_attribute('name'):
                                raise Model.XmlParseError('Missing required attribute @%s for @alias="%s" in %s' % ('name', types_type_node.get_attribute('alias'), make_path(types_type_node)))
                            add_alias(types_type_node.get_attribute('name'), types_type_node.get_attribute('alias'), types_type_node)
                            continue
                        if 'name' not in types_type_node.children:
                            raise Model.XmlParseError('Missing required element <%s> in %s' % ('name', make_path(types_type_node)))
                        name = types_type_node.get('name').get_text()
                        if name in self.callback_map:
                            raise Model.XmlParseError('Duplicate entry "%s" for "%s" in %s' % (name, 'funcpointer', make_path(types_type_node)))
                        self.callback_map[name] = {
                            'name': name,
                            'node': types_type_node
                        }

                    if types_type_node.get_attribute('category') in ['struct', 'union']:
                        if types_type_node.has_attribute('alias'):
                            if not types_type_node.has_attribute('name'):
                                raise Model.XmlParseError('Missing required attribute @%s for @alias="%s" in %s' % ('name', types_type_node.get_attribute('alias'), make_path(types_type_node)))
                            add_alias(types_type_node.get_attribute('name'), types_type_node.get_attribute('alias'), types_type_node)
                            continue
                        if not types_type_node.has_attribute('name'):
                            raise Model.XmlParseError('Missing required attribute @%s in %s' % ('name', make_path(types_type_node)))
                        name = types_type_node.get_attribute('name')
                        class_name = 'ctypes.Structure' if types_type_node.get_attribute('category') == 'struct' else 'ctypes.Union'
                        if name in self.struct_map:
                            raise Model.XmlParseError('Duplicate entry "%s" for "%s" in %s' % (name, 'struct', make_path(types_type_node)))
                        struct = self.struct_map[name] = {
                            'name': name,
                            'node': types_type_node,
                            'class': class_name,
                            'member_map': {},
                            'member_list': []
                        }
                        for member_node in types_type_node.get_all('member'):
                            if 'name' not in member_node.children:
                                raise Model.XmlParseError('Missing required element <%s> in %s' % ('name', make_path(types_type_node)))
                            member_name = member_node.get('name').get_text()
                            member = {
                                'name': member_name,
                                'node': member_node
                            }
                            if 'type' in member_node.children:
                                member['type'] = member_node.get('type').get_text()
                            if member_name in struct['member_map']:
                                raise Model.XmlParseError('Duplicate entry "%s" for "%s %s" in %s' % (member_name, class_name, name, make_path(types_type_node)))
                            struct['member_map'][member_name] = member
                            struct['member_list'].append(member_name)
            
            for enums_node in xml.get_all('enums'):
                if enums_node.get_attribute('type') is None:
                    # List of constants: in this case enums node is meaningless, the constants itself define the values
                    for enum_node in enums_node.get_all('enum'):
                        if not enum_node.has_attribute('name'):
                                raise Model.XmlParseError('Missing required attribute @%s in %s' % ('name', make_path(enum_node)))
                        name = enum_node.get_attribute('name')
                        if enum_node.has_attribute('alias'):
                            add_alias(name, enum_node.get_attribute('alias'), enum_node)
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
                    raise Model.XmlParseError('Unknown enums @type "%s" in %s' % (enums_node.get_attribute('type'), make_path(enums_node)))
                if not enums_node.has_attribute('name'):
                    raise Model.XmlParseError('Missing required attribute @%s in %s' % ('name', make_path(enums_node)))
                enums_name = enums_node.get_attribute('name')
                if enums_name in target_map:
                    raise Model.XmlParseError('Duplicate entry "%s" for "%s" in %s' % (name, 'enum', make_path(enums_node)))
                enums_entry = target_map[enums_name] = {
                    'name': enums_name,
                    'node': enums_node,
                    'values': {}
                }
                for enum_node in enums_node.get_all('enum'):
                    if not enum_node.has_attribute('name'):
                        raise Model.XmlParseError('Missing required attribute @%s in %s' % ('name', make_path(enum_node)))
                    enum_name = enum_node.get_attribute('name')
                    if enum_node.has_attribute('alias'):
                        add_alias(enum_name, enum_node.get_attribute('alias'), enum_node)
                        continue
                    if enum_name in enums_entry['values']:
                        raise Model.XmlParseError('Duplicate entry "%s" for "%s" in %s' % (name, 'enum', make_path(enum_node)))
                    enums_entry['values'][enum_name] = {
                        'name': enum_name,
                        'node': enum_node
                    }
