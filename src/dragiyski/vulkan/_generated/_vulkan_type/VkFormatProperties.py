import ctypes

class VkFormatProperties(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'linearTilingFeatures': ctypes.c_uint32,
            'optimalTilingFeatures': ctypes.c_uint32,
            'bufferFeatures': ctypes.c_uint32,
        }

    _fields_ = [
        ('linearTilingFeatures', ctypes.c_uint32),
        ('optimalTilingFeatures', ctypes.c_uint32),
        ('bufferFeatures', ctypes.c_uint32),
    ]
