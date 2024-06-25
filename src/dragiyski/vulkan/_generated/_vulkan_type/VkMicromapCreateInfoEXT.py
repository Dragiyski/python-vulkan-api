import ctypes

class VkMicromapCreateInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'createFlags': ctypes.c_uint32,
            'buffer': ctypes.c_void_p,
            'offset': ctypes.c_uint64,
            'size': ctypes.c_uint64,
            'type': ctypes.c_int,
            'deviceAddress': ctypes.c_uint64,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('createFlags', ctypes.c_uint32),
        ('buffer', ctypes.c_void_p),
        ('offset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
        ('type', ctypes.c_int),
        ('deviceAddress', ctypes.c_uint64),
    ]
