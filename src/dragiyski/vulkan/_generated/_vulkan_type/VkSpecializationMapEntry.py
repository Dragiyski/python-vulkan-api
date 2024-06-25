import ctypes

class VkSpecializationMapEntry(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'constantID': ctypes.c_uint32,
            'offset': ctypes.c_uint32,
            'size': ctypes.c_size_t,
        }

    _fields_ = [
        ('constantID', ctypes.c_uint32),
        ('offset', ctypes.c_uint32),
        ('size', ctypes.c_size_t),
    ]
