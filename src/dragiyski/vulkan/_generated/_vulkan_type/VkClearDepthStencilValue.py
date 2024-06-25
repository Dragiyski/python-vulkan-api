import ctypes

class VkClearDepthStencilValue(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'depth': ctypes.c_float,
            'stencil': ctypes.c_uint32,
        }

    _fields_ = [
        ('depth', ctypes.c_float),
        ('stencil', ctypes.c_uint32),
    ]
