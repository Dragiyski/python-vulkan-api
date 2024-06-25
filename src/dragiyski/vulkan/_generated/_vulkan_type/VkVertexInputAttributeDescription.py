import ctypes

class VkVertexInputAttributeDescription(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'location': ctypes.c_uint32,
            'binding': ctypes.c_uint32,
            'format': ctypes.c_int,
            'offset': ctypes.c_uint32,
        }

    _fields_ = [
        ('location', ctypes.c_uint32),
        ('binding', ctypes.c_uint32),
        ('format', ctypes.c_int),
        ('offset', ctypes.c_uint32),
    ]
