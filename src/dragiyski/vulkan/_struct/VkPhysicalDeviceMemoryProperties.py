import ctypes, sys

class VkPhysicalDeviceMemoryProperties(ctypes.Structure):
    pass

sys.modules[__name__] = VkPhysicalDeviceMemoryProperties

from . import VkMemoryType
from . import VkMemoryHeap

VkPhysicalDeviceMemoryProperties._fields_ = [
    ('memoryTypeCount', ctypes.c_uint32),
    ('memoryTypes', ctypes.ARRAY(VkMemoryType, 32)),
    ('memoryHeapCount', ctypes.c_uint32),
    ('memoryHeaps', ctypes.ARRAY(VkMemoryHeap, 16)),
]
