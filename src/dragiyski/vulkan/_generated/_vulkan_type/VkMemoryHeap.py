import ctypes

class VkMemoryHeap(ctypes.Structure):
    _fields_ = [
        ('size', ctypes.c_uint64),
        ('flags', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkPhysicalDeviceMemoryProperties',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'size': 'size',
        'flags': 'flags',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'flags': 'VkMemoryHeapFlags',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkMemoryHeap._type_ = {
    'size': ctypes.c_uint64,
    'flags': ctypes.c_uint32,
}
