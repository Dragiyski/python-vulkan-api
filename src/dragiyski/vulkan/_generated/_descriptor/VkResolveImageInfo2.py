from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkResolveImageInfo2'
_member_list_ = ['sType', 'pNext', 'srcImage', 'srcImageLayout', 'dstImage', 'dstImageLayout', 'regionCount', 'pRegions']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_RESOLVE_IMAGE_INFO_2',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'srcImage': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'srcImageLayout': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageLayout',
        'enum': 'VkImageLayout',
        'is_string': False,
    },
    'dstImage': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'dstImageLayout': {
        'type': CIntType('c_int'),
        'type_name': 'VkImageLayout',
        'enum': 'VkImageLayout',
        'is_string': False,
    },
    'regionCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pRegions': {
        'type': CPointerType(CComplexType('VkImageResolve2')),
        'type_name': 'VkImageResolve2',
        'structure': 'VkImageResolve2',
        'length': [['regionCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkImageResolve2',
}
_included_in_ = set()
_input_of_ = {
    'vkCmdResolveImage2',
}
_output_of_ = set()
