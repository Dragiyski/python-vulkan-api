import ctypes

class VkMultiDrawIndexedInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'firstIndex': ctypes.c_uint32,
            'indexCount': ctypes.c_uint32,
            'vertexOffset': ctypes.c_int32,
        }

    _fields_ = [
        ('firstIndex', ctypes.c_uint32),
        ('indexCount', ctypes.c_uint32),
        ('vertexOffset', ctypes.c_int32),
    ]
