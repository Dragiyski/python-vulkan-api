from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBlitImageInfo2'
_member_list_ = ['sType', 'pNext', 'srcImage', 'srcImageLayout', 'dstImage', 'dstImageLayout', 'regionCount', 'pRegions', 'filter']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_BLIT_IMAGE_INFO_2',
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
        'type': CPointerType(CComplexType('VkImageBlit2')),
        'type_name': 'VkImageBlit2',
        'structure': 'VkImageBlit2',
        'length': [['regionCount']],
        'is_string': False,
    },
    'filter': {
        'type': CIntType('c_int'),
        'type_name': 'VkFilter',
        'enum': 'VkFilter',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkBlitImageCubicWeightsInfoQCOM',
}
_includes_ = {
    'VkImageBlit2',
}
_included_in_ = set()
_input_of_ = {
    'vkCmdBlitImage2',
}
_output_of_ = set()
