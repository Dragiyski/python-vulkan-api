from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkScreenSurfaceCreateInfoQNX'
_member_list_ = ['sType', 'pNext', 'flags', 'context', 'window']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SCREEN_SURFACE_CREATE_INFO_QNX',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkScreenSurfaceCreateFlagsQNX',
        'enum': 'VkScreenSurfaceCreateFlagsQNX',
        'is_string': False,
    },
    'context': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'window': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCreateScreenSurfaceQNX',
}
_output_of_ = set()
