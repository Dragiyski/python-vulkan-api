from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSurfaceFormatKHR'
_member_list_ = ['format', 'colorSpace']
_member_info_ = {
    'format': {
        'type': CIntType('c_int'),
        'type_name': 'VkFormat',
        'enum': 'VkFormat',
        'is_string': False,
    },
    'colorSpace': {
        'type': CIntType('c_int'),
        'type_name': 'VkColorSpaceKHR',
        'enum': 'VkColorSpaceKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkSurfaceFormat2KHR',
}
_input_of_ = set()
_output_of_ = {
    'vkGetPhysicalDeviceSurfaceFormatsKHR',
}
