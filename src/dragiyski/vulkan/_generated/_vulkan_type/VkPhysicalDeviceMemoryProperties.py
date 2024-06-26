import ctypes

class VkPhysicalDeviceMemoryProperties(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkMemoryHeap',
        'VkMemoryType',
    }
    _included_in_ = {
        'VkPhysicalDeviceMemoryProperties2',
    }
    _input_of_ = set()
    _output_of_ = {
        'vkGetPhysicalDeviceMemoryProperties',
    }
    _python_name_ = {
        'memoryTypeCount': 'memory_type_count',
        'memoryTypes': 'memory_types',
        'memoryHeapCount': 'memory_heap_count',
        'memoryHeaps': 'memory_heaps',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = dict()

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkMemoryHeap import VkMemoryHeap
from .VkMemoryType import VkMemoryType

VkPhysicalDeviceMemoryProperties._fields_ = [
    ('memoryTypeCount', ctypes.c_uint32),
    ('memoryTypes', ctypes.ARRAY(VkMemoryType, 32)),
    ('memoryHeapCount', ctypes.c_uint32),
    ('memoryHeaps', ctypes.ARRAY(VkMemoryHeap, 16)),
]

VkPhysicalDeviceMemoryProperties._type_ = {
    'memoryTypeCount': ctypes.c_uint32,
    'memoryTypes': ctypes.ARRAY(VkMemoryType, 32),
    'memoryHeapCount': ctypes.c_uint32,
    'memoryHeaps': ctypes.ARRAY(VkMemoryHeap, 16),
}
