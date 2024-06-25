import ctypes

class VkShadingRatePaletteNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'shadingRatePaletteEntryCount': ctypes.c_uint32,
            'pShadingRatePaletteEntries': ctypes.POINTER(ctypes.c_int),
        }

    _fields_ = [
        ('shadingRatePaletteEntryCount', ctypes.c_uint32),
        ('pShadingRatePaletteEntries', ctypes.POINTER(ctypes.c_int)),
    ]
