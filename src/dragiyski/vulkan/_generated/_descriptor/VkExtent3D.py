from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkExtent3D'
_member_list_ = ['width', 'height', 'depth']
_member_info_ = {
    'width': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'height': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'depth': {
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
    'VkImageCopy',
    'VkImageCopy2',
    'VkImageCreateInfo',
    'VkImageFormatProperties',
    'VkImageResolve',
    'VkImageResolve2',
    'VkImageToMemoryCopyEXT',
    'VkMemoryToImageCopyEXT',
    'VkQueueFamilyProperties',
    'VkSparseImageFormatProperties',
    'VkSparseImageMemoryBind',
    'VkTilePropertiesQCOM',
}
_input_of_ = set()
_output_of_ = set()
