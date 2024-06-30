from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageBlit'
_member_list_ = ['srcSubresource', 'srcOffsets', 'dstSubresource', 'dstOffsets']
_member_info_ = {
    'srcSubresource': {
        'type': CComplexType('VkImageSubresourceLayers'),
        'type_name': 'VkImageSubresourceLayers',
        'structure': 'VkImageSubresourceLayers',
        'is_string': False,
    },
    'srcOffsets': {
        'type': CArrayType(CComplexType('VkOffset3D'), 2),
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
    'dstOffsets': {
        'type': CArrayType(CComplexType('VkOffset3D'), 2),
        'type_name': 'VkOffset3D',
        'structure': 'VkOffset3D',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkImageSubresourceLayers',
    'VkOffset3D',
}
_included_in_ = set()
_input_of_ = {
    'vkCmdBlitImage',
}
_output_of_ = set()
