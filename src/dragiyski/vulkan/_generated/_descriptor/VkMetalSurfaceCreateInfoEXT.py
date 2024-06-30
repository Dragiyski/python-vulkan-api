from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMetalSurfaceCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'flags', 'pLayer']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_METAL_SURFACE_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkMetalSurfaceCreateFlagsEXT',
        'enum': 'VkMetalSurfaceCreateFlagsEXT',
        'is_string': False,
    },
    'pLayer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCreateMetalSurfaceEXT',
}
_output_of_ = set()
