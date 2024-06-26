import ctypes

class VkSparseMemoryBind(ctypes.Structure):
    _fields_ = [
        ('resourceOffset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
        ('memory', ctypes.c_void_p),
        ('memoryOffset', ctypes.c_uint64),
        ('flags', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkSparseBufferMemoryBindInfo',
        'VkSparseImageOpaqueMemoryBindInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'resourceOffset': 'resource_offset',
        'size': 'size',
        'memory': 'memory',
        'memoryOffset': 'memory_offset',
        'flags': 'flags',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'flags': 'VkSparseMemoryBindFlags',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkSparseMemoryBind._type_ = {
    'resourceOffset': ctypes.c_uint64,
    'size': ctypes.c_uint64,
    'memory': ctypes.c_void_p,
    'memoryOffset': ctypes.c_uint64,
    'flags': ctypes.c_uint32,
}
