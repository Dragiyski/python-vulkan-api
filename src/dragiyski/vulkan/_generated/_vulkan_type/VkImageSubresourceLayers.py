import ctypes

class VkImageSubresourceLayers(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'aspectMask': ctypes.c_uint32,
            'mipLevel': ctypes.c_uint32,
            'baseArrayLayer': ctypes.c_uint32,
            'layerCount': ctypes.c_uint32,
        }

    _fields_ = [
        ('aspectMask', ctypes.c_uint32),
        ('mipLevel', ctypes.c_uint32),
        ('baseArrayLayer', ctypes.c_uint32),
        ('layerCount', ctypes.c_uint32),
    ]
