from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageSubresourceRange'
_member_list_ = ['aspectMask', 'baseMipLevel', 'levelCount', 'baseArrayLayer', 'layerCount']
_member_info_ = {
    'aspectMask': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkImageAspectFlags',
        'enum': 'VkImageAspectFlags',
        'is_string': False,
    },
    'baseMipLevel': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'levelCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'baseArrayLayer': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'layerCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkHostImageLayoutTransitionInfoEXT',
    'VkImageMemoryBarrier',
    'VkImageMemoryBarrier2',
    'VkImageViewCreateInfo',
}
_input_of_ = {
    'vkCmdClearColorImage',
    'vkCmdClearDepthStencilImage',
}
_output_of_ = set()
