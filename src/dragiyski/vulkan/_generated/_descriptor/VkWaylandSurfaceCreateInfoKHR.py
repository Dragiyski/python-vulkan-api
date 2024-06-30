from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkWaylandSurfaceCreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'flags', 'display', 'surface']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_WAYLAND_SURFACE_CREATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkWaylandSurfaceCreateFlagsKHR',
        'enum': 'VkWaylandSurfaceCreateFlagsKHR',
        'is_string': False,
    },
    'display': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'surface': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCreateWaylandSurfaceKHR',
}
_output_of_ = set()
