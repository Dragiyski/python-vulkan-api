import ctypes

class VkBindVideoSessionMemoryInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'memoryBindIndex': ctypes.c_uint32,
            'memory': ctypes.c_void_p,
            'memoryOffset': ctypes.c_uint64,
            'memorySize': ctypes.c_uint64,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memoryBindIndex', ctypes.c_uint32),
        ('memory', ctypes.c_void_p),
        ('memoryOffset', ctypes.c_uint64),
        ('memorySize', ctypes.c_uint64),
    ]
