import ctypes

class VkBufferViewCreateInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'buffer': ctypes.c_void_p,
            'format': ctypes.c_int,
            'offset': ctypes.c_uint64,
            'range': ctypes.c_uint64,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('buffer', ctypes.c_void_p),
        ('format', ctypes.c_int),
        ('offset', ctypes.c_uint64),
        ('range', ctypes.c_uint64),
    ]
