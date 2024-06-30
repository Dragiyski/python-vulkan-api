from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCopyBufferToImageInfo2'
_member_list_ = ['sType', 'pNext', 'srcBuffer', 'dstImage', 'dstImageLayout', 'regionCount', 'pRegions']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_COPY_BUFFER_TO_IMAGE_INFO_2',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'srcBuffer': {
        'type': CIntType('c_void_p'),
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
        'type': CPointerType(CComplexType('VkBufferImageCopy2')),
        'type_name': 'VkBufferImageCopy2',
        'structure': 'VkBufferImageCopy2',
        'length': [['regionCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkBufferImageCopy2',
}
_included_in_ = set()
_input_of_ = {
    'vkCmdCopyBufferToImage2',
}
_output_of_ = set()
