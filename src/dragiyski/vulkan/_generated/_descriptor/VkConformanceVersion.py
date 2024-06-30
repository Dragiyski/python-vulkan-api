from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkConformanceVersion'
_member_list_ = ['major', 'minor', 'subminor', 'patch']
_member_info_ = {
    'major': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'minor': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'subminor': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
    'patch': {
        'type': CIntType('c_uint8'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkPhysicalDeviceDriverProperties',
    'VkPhysicalDeviceVulkan12Properties',
}
_input_of_ = set()
_output_of_ = set()
