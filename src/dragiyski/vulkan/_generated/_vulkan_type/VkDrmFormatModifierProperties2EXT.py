import ctypes

class VkDrmFormatModifierProperties2EXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'drmFormatModifier': ctypes.c_uint64,
            'drmFormatModifierPlaneCount': ctypes.c_uint32,
            'drmFormatModifierTilingFeatures': ctypes.c_uint64,
        }

    _fields_ = [
        ('drmFormatModifier', ctypes.c_uint64),
        ('drmFormatModifierPlaneCount', ctypes.c_uint32),
        ('drmFormatModifierTilingFeatures', ctypes.c_uint64),
    ]
