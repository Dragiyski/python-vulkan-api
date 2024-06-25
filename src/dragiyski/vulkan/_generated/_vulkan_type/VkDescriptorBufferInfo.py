import ctypes

class VkDescriptorBufferInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'buffer': ctypes.c_void_p,
            'offset': ctypes.c_uint64,
            'range': ctypes.c_uint64,
        }

    _fields_ = [
        ('buffer', ctypes.c_void_p),
        ('offset', ctypes.c_uint64),
        ('range', ctypes.c_uint64),
    ]
