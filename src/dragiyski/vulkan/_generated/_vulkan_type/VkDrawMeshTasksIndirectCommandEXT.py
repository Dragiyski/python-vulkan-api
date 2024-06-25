import ctypes

class VkDrawMeshTasksIndirectCommandEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'groupCountX': ctypes.c_uint32,
            'groupCountY': ctypes.c_uint32,
            'groupCountZ': ctypes.c_uint32,
        }

    _fields_ = [
        ('groupCountX', ctypes.c_uint32),
        ('groupCountY', ctypes.c_uint32),
        ('groupCountZ', ctypes.c_uint32),
    ]
