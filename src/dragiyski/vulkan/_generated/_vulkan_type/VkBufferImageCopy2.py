import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent3D import CType as VkExtent3D
from .VkImageSubresourceLayers import CType as VkImageSubresourceLayers
from .VkOffset3D import CType as VkOffset3D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('bufferOffset', ctypes.c_uint64),
    ('bufferRowLength', ctypes.c_uint32),
    ('bufferImageHeight', ctypes.c_uint32),
    ('imageSubresource', VkImageSubresourceLayers),
    ('imageOffset', VkOffset3D),
    ('imageExtent', VkExtent3D),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkCopyCommandTransformInfoQCOM',
    },
    'includes': {
        'VkExtent3D',
        'VkImageSubresourceLayers',
        'VkOffset3D',
    },
    'included_in': {
        'VkCopyBufferToImageInfo2',
        'VkCopyImageToBufferInfo2',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BUFFER_IMAGE_COPY_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'bufferOffset': {'python_name': ['buffer', 'offset']},
        'bufferRowLength': {'python_name': ['buffer', 'row', 'length']},
        'bufferImageHeight': {'python_name': ['buffer', 'image', 'height']},
        'imageSubresource': {'python_name': ['image', 'subresource'], 'type': 'VkImageSubresourceLayers'},
        'imageOffset': {'python_name': ['image', 'offset'], 'type': 'VkOffset3D'},
        'imageExtent': {'python_name': ['image', 'extent'], 'type': 'VkExtent3D'},
    }
}
