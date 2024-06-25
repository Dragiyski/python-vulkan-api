import ctypes

class VkDrawIndirectCommand(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'vertexCount': ctypes.c_uint32,
            'instanceCount': ctypes.c_uint32,
            'firstVertex': ctypes.c_uint32,
            'firstInstance': ctypes.c_uint32,
        }

    _fields_ = [
        ('vertexCount', ctypes.c_uint32),
        ('instanceCount', ctypes.c_uint32),
        ('firstVertex', ctypes.c_uint32),
        ('firstInstance', ctypes.c_uint32),
    ]
