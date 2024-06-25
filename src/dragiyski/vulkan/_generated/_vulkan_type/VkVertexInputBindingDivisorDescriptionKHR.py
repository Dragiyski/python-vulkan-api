import ctypes

class VkVertexInputBindingDivisorDescriptionKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'binding': ctypes.c_uint32,
            'divisor': ctypes.c_uint32,
        }

    _fields_ = [
        ('binding', ctypes.c_uint32),
        ('divisor', ctypes.c_uint32),
    ]
