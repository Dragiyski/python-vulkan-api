import ctypes

class VkPhysicalDeviceMemoryProperties(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'memoryTypeCount': ctypes.c_uint32,
            'memoryTypes': ctypes.ARRAY(VkMemoryType, 32),
            'memoryHeapCount': ctypes.c_uint32,
            'memoryHeaps': ctypes.ARRAY(VkMemoryHeap, 16),
        }


from .VkMemoryHeap import VkMemoryHeap
from .VkMemoryType import VkMemoryType

VkPhysicalDeviceMemoryProperties._fields_ = [
    ('memoryTypeCount', ctypes.c_uint32),
    ('memoryTypes', ctypes.ARRAY(VkMemoryType, 32)),
    ('memoryHeapCount', ctypes.c_uint32),
    ('memoryHeaps', ctypes.ARRAY(VkMemoryHeap, 16)),
]
