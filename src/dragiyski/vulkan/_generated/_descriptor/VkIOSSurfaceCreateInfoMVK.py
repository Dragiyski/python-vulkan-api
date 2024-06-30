from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkIOSSurfaceCreateInfoMVK'
_member_list_ = ['sType', 'pNext', 'flags', 'pView']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IOS_SURFACE_CREATE_INFO_MVK',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkIOSSurfaceCreateFlagsMVK',
        'enum': 'VkIOSSurfaceCreateFlagsMVK',
        'is_string': False,
    },
    'pView': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCreateIOSSurfaceMVK',
}
_output_of_ = set()
