from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSubresourceLayout'
_member_list_ = ['offset', 'size', 'rowPitch', 'arrayPitch', 'depthPitch']
_member_info_ = {
    'offset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'size': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'rowPitch': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'arrayPitch': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'depthPitch': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkImageDrmFormatModifierExplicitCreateInfoEXT',
    'VkSubresourceLayout2KHR',
}
_input_of_ = set()
_output_of_ = {
    'vkGetImageSubresourceLayout',
}
