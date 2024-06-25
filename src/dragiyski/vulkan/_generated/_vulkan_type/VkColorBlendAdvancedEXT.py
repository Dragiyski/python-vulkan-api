import ctypes

class VkColorBlendAdvancedEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'advancedBlendOp': ctypes.c_int,
            'srcPremultiplied': ctypes.c_uint32,
            'dstPremultiplied': ctypes.c_uint32,
            'blendOverlap': ctypes.c_int,
            'clampResults': ctypes.c_uint32,
        }

    _fields_ = [
        ('advancedBlendOp', ctypes.c_int),
        ('srcPremultiplied', ctypes.c_uint32),
        ('dstPremultiplied', ctypes.c_uint32),
        ('blendOverlap', ctypes.c_int),
        ('clampResults', ctypes.c_uint32),
    ]
