import ctypes

class VkMemoryRequirements(ctypes.Structure):
    _fields_ = [
        ('size', ctypes.c_uint64),
        ('alignment', ctypes.c_uint64),
        ('memoryTypeBits', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = {
        'VkMemoryRequirements2',
        'VkVideoSessionMemoryRequirementsKHR',
    }
    _input_of_ = set()
    _output_of_ = {
        'vkGetBufferMemoryRequirements',
        'vkGetImageMemoryRequirements',
    }
    _python_name_ = {
        'size': 'size',
        'alignment': 'alignment',
        'memoryTypeBits': 'memory_type_bits',
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

VkMemoryRequirements._type_ = {
    'size': ctypes.c_uint64,
    'alignment': ctypes.c_uint64,
    'memoryTypeBits': ctypes.c_uint32,
}
