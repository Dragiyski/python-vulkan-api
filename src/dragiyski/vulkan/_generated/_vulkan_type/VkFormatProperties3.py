import ctypes

class VkFormatProperties3(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'linearTilingFeatures': ctypes.c_uint64,
            'optimalTilingFeatures': ctypes.c_uint64,
            'bufferFeatures': ctypes.c_uint64,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('linearTilingFeatures', ctypes.c_uint64),
        ('optimalTilingFeatures', ctypes.c_uint64),
        ('bufferFeatures', ctypes.c_uint64),
    ]
