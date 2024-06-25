import ctypes

class VkMultiDrawInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'firstVertex': ctypes.c_uint32,
            'vertexCount': ctypes.c_uint32,
        }

    _fields_ = [
        ('firstVertex', ctypes.c_uint32),
        ('vertexCount', ctypes.c_uint32),
    ]
