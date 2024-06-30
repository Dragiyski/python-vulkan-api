from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageResolve2'
_member_list_ = ['sType', 'pNext', 'srcSubresource', 'srcOffset', 'dstSubresource', 'dstOffset', 'extent']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMAGE_RESOLVE_2',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
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
_included_in_ = {
    'VkResolveImageInfo2',
}
_input_of_ = set()
_output_of_ = set()
