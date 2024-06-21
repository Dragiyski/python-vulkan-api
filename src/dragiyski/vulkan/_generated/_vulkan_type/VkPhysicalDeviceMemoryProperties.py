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
