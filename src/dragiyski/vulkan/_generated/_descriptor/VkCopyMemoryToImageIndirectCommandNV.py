from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCopyMemoryToImageIndirectCommandNV'
_member_list_ = ['srcAddress', 'bufferRowLength', 'bufferImageHeight', 'imageSubresource', 'imageOffset', 'imageExtent']
_member_info_ = {
    'srcAddress': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'bufferRowLength': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'bufferImageHeight': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'imageSubresource': {
        'type': CComplexType('VkImageSubresourceLayers'),
        'type_name': 'VkImageSubresourceLayers',
        'structure': 'VkImageSubresourceLayers',
        'is_string': False,
    },
    'imageOffset': {
        'type': CComplexType('VkOffset3D'),
        'type_name': 'VkOffset3D',
        'structure': 'VkOffset3D',
        'is_string': False,
    },
    'imageExtent': {
        'type': CComplexType('VkExtent3D'),
        'type_name': 'VkExtent3D',
        'structure': 'VkExtent3D',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkExtent3D',
    'VkImageSubresourceLayers',
    'VkOffset3D',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
