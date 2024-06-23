import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent3D import CType as VkExtent3D
from .VkImageSubresource import CType as VkImageSubresource
from .VkOffset3D import CType as VkOffset3D

CType._fields_ = [
    ('subresource', VkImageSubresource),
    ('offset', VkOffset3D),
    ('extent', VkExtent3D),
    ('memory', ctypes.c_void_p),
    ('memoryOffset', ctypes.c_uint64),
    ('flags', ctypes.c_uint32),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkExtent3D',
        'VkImageSubresource',
        'VkOffset3D',
    },
    'included_in': {
        'VkSparseImageMemoryBindInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'subresource': {'python_name': ['subresource'], 'type': 'VkImageSubresource'},
        'offset': {'python_name': ['offset'], 'type': 'VkOffset3D'},
        'extent': {'python_name': ['extent'], 'type': 'VkExtent3D'},
        'memory': {'python_name': ['memory']},
        'memoryOffset': {'python_name': ['memory', 'offset']},
        'flags': {'python_name': ['flags'], 'type': 'VkSparseMemoryBindFlags'},
    }
}
