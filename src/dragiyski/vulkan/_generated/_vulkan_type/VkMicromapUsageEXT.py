import ctypes

class VkMicromapUsageEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'count': ctypes.c_uint32,
            'subdivisionLevel': ctypes.c_uint32,
            'format': ctypes.c_uint32,
        }

    _fields_ = [
        ('count', ctypes.c_uint32),
        ('subdivisionLevel', ctypes.c_uint32),
        ('format', ctypes.c_uint32),
    ]
