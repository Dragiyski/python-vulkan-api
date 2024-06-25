import ctypes

class VkDrawIndexedIndirectCommand(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'indexCount': ctypes.c_uint32,
            'instanceCount': ctypes.c_uint32,
            'firstIndex': ctypes.c_uint32,
            'vertexOffset': ctypes.c_int32,
            'firstInstance': ctypes.c_uint32,
        }

    _fields_ = [
        ('indexCount', ctypes.c_uint32),
        ('instanceCount', ctypes.c_uint32),
        ('firstIndex', ctypes.c_uint32),
        ('vertexOffset', ctypes.c_int32),
        ('firstInstance', ctypes.c_uint32),
    ]
