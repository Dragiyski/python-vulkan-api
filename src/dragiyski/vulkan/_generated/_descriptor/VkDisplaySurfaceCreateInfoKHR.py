from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDisplaySurfaceCreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'flags', 'displayMode', 'planeIndex', 'planeStackIndex', 'transform', 'globalAlpha', 'alphaMode', 'imageExtent']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DISPLAY_SURFACE_CREATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkDisplaySurfaceCreateFlagsKHR',
        'enum': 'VkDisplaySurfaceCreateFlagsKHR',
        'is_string': False,
    },
    'displayMode': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'planeIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'planeStackIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'transform': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSurfaceTransformFlagBitsKHR',
        'is_string': False,
    },
    'globalAlpha': {
        'type': CFloatType('c_float'),
        'is_string': False,
    },
    'alphaMode': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkDisplayPlaneAlphaFlagBitsKHR',
        'is_string': False,
    },
    'imageExtent': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkExtent2D',
}
_included_in_ = set()
_input_of_ = {
    'vkCreateDisplayPlaneSurfaceKHR',
}
_output_of_ = set()
