import ctypes

class CType(ctypes.Structure):
    pass

from .VkMemoryHeap import CType as VkMemoryHeap
from .VkMemoryType import CType as VkMemoryType

CType._fields_ = [
    ('memoryTypeCount', ctypes.c_uint32),
    ('memoryTypes', ctypes.ARRAY(VkMemoryType, 32)),
    ('memoryHeapCount', ctypes.c_uint32),
    ('memoryHeaps', ctypes.ARRAY(VkMemoryHeap, 16)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkMemoryHeap',
        'VkMemoryType',
    },
    'included_in': {
        'VkPhysicalDeviceMemoryProperties2',
    },
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceMemoryProperties',
    },
    'member_map': {
        'memoryTypeCount': {'python_name': ['memory', 'type', 'count']},
        'memoryTypes': {'python_name': ['memory', 'types'], 'len': [['memoryTypeCount']], 'type': 'VkMemoryType'},
        'memoryHeapCount': {'python_name': ['memory', 'heap', 'count']},
        'memoryHeaps': {'python_name': ['memory', 'heaps'], 'len': [['memoryHeapCount']], 'type': 'VkMemoryHeap'},
    }
}
