import ctypes

class VkDeviceMemoryReportCallbackDataEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'type': ctypes.c_int,
            'memoryObjectId': ctypes.c_uint64,
            'size': ctypes.c_uint64,
            'objectType': ctypes.c_int,
            'objectHandle': ctypes.c_uint64,
            'heapIndex': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('type', ctypes.c_int),
        ('memoryObjectId', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
        ('objectType', ctypes.c_int),
        ('objectHandle', ctypes.c_uint64),
        ('heapIndex', ctypes.c_uint32),
    ]
