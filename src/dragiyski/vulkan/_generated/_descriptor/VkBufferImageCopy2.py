from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkBufferImageCopy2'
_member_list_ = ['sType', 'pNext', 'bufferOffset', 'bufferRowLength', 'bufferImageHeight', 'imageSubresource', 'imageOffset', 'imageExtent']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_BUFFER_IMAGE_COPY_2',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'bufferOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'bufferRowLength': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'bufferImageHeight': {
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
_extended_by_ = {
    'VkCopyCommandTransformInfoQCOM',
}
_includes_ = {
    'VkExtent3D',
    'VkImageSubresourceLayers',
    'VkOffset3D',
}
_included_in_ = {
    'VkCopyBufferToImageInfo2',
    'VkCopyImageToBufferInfo2',
}
_input_of_ = set()
_output_of_ = set()
