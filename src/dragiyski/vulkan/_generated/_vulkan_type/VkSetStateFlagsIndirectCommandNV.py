import ctypes

class VkSetStateFlagsIndirectCommandNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'data': ctypes.c_uint32,
        }

    _fields_ = [
        ('data', ctypes.c_uint32),
    ]
