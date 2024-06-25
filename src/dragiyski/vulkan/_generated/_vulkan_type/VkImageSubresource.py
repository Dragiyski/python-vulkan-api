import ctypes

class VkImageSubresource(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'aspectMask': ctypes.c_uint32,
            'mipLevel': ctypes.c_uint32,
            'arrayLayer': ctypes.c_uint32,
        }

    _fields_ = [
        ('aspectMask', ctypes.c_uint32),
        ('mipLevel', ctypes.c_uint32),
        ('arrayLayer', ctypes.c_uint32),
    ]
