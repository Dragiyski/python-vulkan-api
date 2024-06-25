import ctypes

class VkMemoryType(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'propertyFlags': ctypes.c_uint32,
            'heapIndex': ctypes.c_uint32,
        }

    _fields_ = [
        ('propertyFlags', ctypes.c_uint32),
        ('heapIndex', ctypes.c_uint32),
    ]
