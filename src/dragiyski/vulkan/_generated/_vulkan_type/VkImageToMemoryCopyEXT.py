import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent3D import CType as VkExtent3D
from .VkImageSubresourceLayers import CType as VkImageSubresourceLayers
from .VkOffset3D import CType as VkOffset3D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pHostPointer', ctypes.c_void_p),
    ('memoryRowLength', ctypes.c_uint32),
    ('memoryImageHeight', ctypes.c_uint32),
    ('imageSubresource', VkImageSubresourceLayers),
    ('imageOffset', VkOffset3D),
    ('imageExtent', VkExtent3D),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkExtent3D',
        'VkImageSubresourceLayers',
        'VkOffset3D',
    },
    'included_in': {
        'VkCopyImageToMemoryInfoEXT',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMAGE_TO_MEMORY_COPY_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pHostPointer': {'python_name': ['p', 'host', 'pointer']},
        'memoryRowLength': {'python_name': ['memory', 'row', 'length']},
        'memoryImageHeight': {'python_name': ['memory', 'image', 'height']},
        'imageSubresource': {'python_name': ['image', 'subresource'], 'type': 'VkImageSubresourceLayers'},
        'imageOffset': {'python_name': ['image', 'offset'], 'type': 'VkOffset3D'},
        'imageExtent': {'python_name': ['image', 'extent'], 'type': 'VkExtent3D'},
    }
}
