from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkOffset3D'
_member_list_ = ['x', 'y', 'z']
_member_info_ = {
    'x': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
    'y': {
        'type': CIntType('c_int32'),
        'is_string': False,
    },
    'z': {
        'type': CIntType('c_int32'),
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
    'VkSparseImageMemoryBind',
}
_input_of_ = set()
_output_of_ = set()
