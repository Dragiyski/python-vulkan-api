import ctypes

class VkDrawMeshTasksIndirectCommandNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'taskCount': ctypes.c_uint32,
            'firstTask': ctypes.c_uint32,
        }

    _fields_ = [
        ('taskCount', ctypes.c_uint32),
        ('firstTask', ctypes.c_uint32),
    ]
