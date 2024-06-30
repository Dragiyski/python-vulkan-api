from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageSubresourceLayers'
_member_list_ = ['aspectMask', 'mipLevel', 'baseArrayLayer', 'layerCount']
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
    'VkBufferImageCopy',
    'VkBufferImageCopy2',
    'VkCopyMemoryToImageIndirectCommandNV',
    'VkImageBlit',
    'VkImageBlit2',
    'VkImageCopy',
    'VkImageCopy2',
    'VkImageResolve',
    'VkImageResolve2',
    'VkImageToMemoryCopyEXT',
    'VkMemoryToImageCopyEXT',
}
_input_of_ = {
    'vkCmdCopyMemoryToImageIndirectNV',
}
_output_of_ = set()
