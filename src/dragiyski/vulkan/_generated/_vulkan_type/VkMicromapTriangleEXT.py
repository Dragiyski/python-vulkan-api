import ctypes

class VkMicromapTriangleEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'dataOffset': ctypes.c_uint32,
            'subdivisionLevel': ctypes.c_uint16,
            'format': ctypes.c_uint16,
        }

    _fields_ = [
        ('dataOffset', ctypes.c_uint32),
        ('subdivisionLevel', ctypes.c_uint16),
        ('format', ctypes.c_uint16),
    ]
