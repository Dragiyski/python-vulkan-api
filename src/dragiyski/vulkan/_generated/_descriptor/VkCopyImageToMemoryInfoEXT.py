from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCopyImageToMemoryInfoEXT'
_member_list_ = ['sType', 'pNext', 'flags', 'srcImage', 'srcImageLayout', 'regionCount', 'pRegions']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_COPY_IMAGE_TO_MEMORY_INFO_EXT',
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
    'regionCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pRegions': {
        'type': CPointerType(CComplexType('VkImageToMemoryCopyEXT')),
        'type_name': 'VkImageToMemoryCopyEXT',
        'structure': 'VkImageToMemoryCopyEXT',
        'length': [['regionCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkImageToMemoryCopyEXT',
}
_included_in_ = set()
_input_of_ = {
    'vkCopyImageToMemoryEXT',
}
_output_of_ = set()
