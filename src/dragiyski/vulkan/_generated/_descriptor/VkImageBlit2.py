from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImageBlit2'
_member_list_ = ['sType', 'pNext', 'srcSubresource', 'srcOffsets', 'dstSubresource', 'dstOffsets']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMAGE_BLIT_2',
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
_extended_by_ = {
    'VkCopyCommandTransformInfoQCOM',
}
_includes_ = {
    'VkImageSubresourceLayers',
    'VkOffset3D',
}
_included_in_ = {
    'VkBlitImageInfo2',
}
_input_of_ = set()
_output_of_ = set()
