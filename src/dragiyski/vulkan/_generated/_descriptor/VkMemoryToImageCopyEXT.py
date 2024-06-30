from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMemoryToImageCopyEXT'
_member_list_ = ['sType', 'pNext', 'pHostPointer', 'memoryRowLength', 'memoryImageHeight', 'imageSubresource', 'imageOffset', 'imageExtent']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_MEMORY_TO_IMAGE_COPY_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pHostPointer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'memoryRowLength': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'memoryImageHeight': {
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
_included_in_ = {
    'VkCopyMemoryToImageInfoEXT',
}
_input_of_ = set()
_output_of_ = set()
