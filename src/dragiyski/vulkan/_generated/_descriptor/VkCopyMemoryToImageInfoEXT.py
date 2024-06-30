from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCopyMemoryToImageInfoEXT'
_member_list_ = ['sType', 'pNext', 'flags', 'dstImage', 'dstImageLayout', 'regionCount', 'pRegions']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_COPY_MEMORY_TO_IMAGE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkHostImageCopyFlagsEXT',
        'enum': 'VkHostImageCopyFlagsEXT',
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
        'type': CPointerType(CComplexType('VkMemoryToImageCopyEXT')),
        'type_name': 'VkMemoryToImageCopyEXT',
        'structure': 'VkMemoryToImageCopyEXT',
        'length': [['regionCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkMemoryToImageCopyEXT',
}
_included_in_ = set()
_input_of_ = {
    'vkCopyMemoryToImageEXT',
}
_output_of_ = set()
