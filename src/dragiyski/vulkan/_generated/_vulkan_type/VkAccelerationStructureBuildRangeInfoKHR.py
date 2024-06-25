import ctypes

class VkAccelerationStructureBuildRangeInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'primitiveCount': ctypes.c_uint32,
            'primitiveOffset': ctypes.c_uint32,
            'firstVertex': ctypes.c_uint32,
            'transformOffset': ctypes.c_uint32,
        }

    _fields_ = [
        ('primitiveCount', ctypes.c_uint32),
        ('primitiveOffset', ctypes.c_uint32),
        ('firstVertex', ctypes.c_uint32),
        ('transformOffset', ctypes.c_uint32),
    ]
