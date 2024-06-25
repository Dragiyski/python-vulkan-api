import ctypes

class VkVertexInputBindingDescription2EXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'binding': ctypes.c_uint32,
            'stride': ctypes.c_uint32,
            'inputRate': ctypes.c_int,
            'divisor': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('binding', ctypes.c_uint32),
        ('stride', ctypes.c_uint32),
        ('inputRate', ctypes.c_int),
        ('divisor', ctypes.c_uint32),
    ]
