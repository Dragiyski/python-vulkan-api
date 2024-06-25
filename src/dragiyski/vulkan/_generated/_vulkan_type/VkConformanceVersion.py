import ctypes

class VkConformanceVersion(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'major': ctypes.c_uint8,
            'minor': ctypes.c_uint8,
            'subminor': ctypes.c_uint8,
            'patch': ctypes.c_uint8,
        }

    _fields_ = [
        ('major', ctypes.c_uint8),
        ('minor', ctypes.c_uint8),
        ('subminor', ctypes.c_uint8),
        ('patch', ctypes.c_uint8),
    ]
