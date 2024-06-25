import ctypes

class VkVertexInputBindingDescription(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'binding': ctypes.c_uint32,
            'stride': ctypes.c_uint32,
            'inputRate': ctypes.c_int,
        }

    _fields_ = [
        ('binding', ctypes.c_uint32),
        ('stride', ctypes.c_uint32),
        ('inputRate', ctypes.c_int),
    ]
