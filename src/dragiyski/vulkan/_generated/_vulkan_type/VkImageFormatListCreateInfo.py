import ctypes

class VkImageFormatListCreateInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'viewFormatCount': ctypes.c_uint32,
            'pViewFormats': ctypes.POINTER(ctypes.c_int),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('viewFormatCount', ctypes.c_uint32),
        ('pViewFormats', ctypes.POINTER(ctypes.c_int)),
    ]
