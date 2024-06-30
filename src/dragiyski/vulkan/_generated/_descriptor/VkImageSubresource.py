from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageSubresource'
_member_list_ = ['aspectMask', 'mipLevel', 'arrayLayer']
_member_info_ = {
    'aspectMask': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageAspectFlags',
        'enum': 'VkImageAspectFlags',
        'is_string': False,
    },
    'mipLevel': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'arrayLayer': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkImageSubresource2KHR',
    'VkSparseImageMemoryBind',
}
_input_of_ = {
    'vkGetImageSubresourceLayout',
}
_output_of_ = set()
