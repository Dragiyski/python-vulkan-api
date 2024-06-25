import ctypes

class VkStencilOpState(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'failOp': ctypes.c_int,
            'passOp': ctypes.c_int,
            'depthFailOp': ctypes.c_int,
            'compareOp': ctypes.c_int,
            'compareMask': ctypes.c_uint32,
            'writeMask': ctypes.c_uint32,
            'reference': ctypes.c_uint32,
        }

    _fields_ = [
        ('failOp', ctypes.c_int),
        ('passOp', ctypes.c_int),
        ('depthFailOp', ctypes.c_int),
        ('compareOp', ctypes.c_int),
        ('compareMask', ctypes.c_uint32),
        ('writeMask', ctypes.c_uint32),
        ('reference', ctypes.c_uint32),
    ]
