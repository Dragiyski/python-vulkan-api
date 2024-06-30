from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkApplicationInfo'
_member_list_ = ['sType', 'pNext', 'pApplicationName', 'applicationVersion', 'pEngineName', 'engineVersion', 'apiVersion']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_APPLICATION_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pApplicationName': {
        'type': CStringType('c_char_p'),
        'length': [],
        'is_string': True,
    },
    'applicationVersion': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pEngineName': {
        'type': CStringType('c_char_p'),
        'length': [],
        'is_string': True,
    },
    'engineVersion': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'apiVersion': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkInstanceCreateInfo',
}
_input_of_ = set()
_output_of_ = set()
