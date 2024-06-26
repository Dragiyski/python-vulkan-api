import ctypes

class VkMemoryType(ctypes.Structure):
    _fields_ = [
        ('propertyFlags', ctypes.c_uint32),
        ('heapIndex', ctypes.c_uint32),
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
        'propertyFlags': 'property_flags',
        'heapIndex': 'heap_index',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'propertyFlags': 'VkMemoryPropertyFlags',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)

VkMemoryType._type_ = {
    'propertyFlags': ctypes.c_uint32,
    'heapIndex': ctypes.c_uint32,
}
