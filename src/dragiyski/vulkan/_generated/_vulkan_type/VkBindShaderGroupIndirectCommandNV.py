import ctypes

class VkBindShaderGroupIndirectCommandNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'groupIndex': ctypes.c_uint32,
        }

    _fields_ = [
        ('groupIndex', ctypes.c_uint32),
    ]
