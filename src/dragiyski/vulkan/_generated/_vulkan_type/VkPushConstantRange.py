import ctypes

class VkPushConstantRange(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'stageFlags': ctypes.c_uint32,
            'offset': ctypes.c_uint32,
            'size': ctypes.c_uint32,
        }

    _fields_ = [
        ('stageFlags', ctypes.c_uint32),
        ('offset', ctypes.c_uint32),
        ('size', ctypes.c_uint32),
    ]
