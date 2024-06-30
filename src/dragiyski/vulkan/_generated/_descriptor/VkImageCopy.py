from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageCopy'
_member_list_ = ['srcSubresource', 'srcOffset', 'dstSubresource', 'dstOffset', 'extent']
_member_info_ = {
    'srcSubresource': {
        'type': CComplexType('VkImageSubresourceLayers'),
        'type_name': 'VkImageSubresourceLayers',
        'structure': 'VkImageSubresourceLayers',
        'is_string': False,
    },
    'srcOffset': {
        'type': CComplexType('VkOffset3D'),
        'type_name': 'VkOffset3D',
        'structure': 'VkOffset3D',
        'is_string': False,
    },
    'dstSubresource': {
        'type': CComplexType('VkImageSubresourceLayers'),
        'type_name': 'VkImageSubresourceLayers',
        'structure': 'VkImageSubresourceLayers',
        'is_string': False,
    },
    'dstOffset': {
        'type': CComplexType('VkOffset3D'),
        'type_name': 'VkOffset3D',
        'structure': 'VkOffset3D',
        'is_string': False,
    },
    'extent': {
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
_input_of_ = {
    'vkCmdCopyImage',
}
_output_of_ = set()
