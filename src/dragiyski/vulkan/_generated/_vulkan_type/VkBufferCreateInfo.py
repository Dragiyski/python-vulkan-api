import ctypes

class VkBufferCreateInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'size': ctypes.c_uint64,
            'usage': ctypes.c_uint32,
            'sharingMode': ctypes.c_int,
            'queueFamilyIndexCount': ctypes.c_uint32,
            'pQueueFamilyIndices': ctypes.POINTER(ctypes.c_uint32),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('size', ctypes.c_uint64),
        ('usage', ctypes.c_uint32),
        ('sharingMode', ctypes.c_int),
        ('queueFamilyIndexCount', ctypes.c_uint32),
        ('pQueueFamilyIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]
