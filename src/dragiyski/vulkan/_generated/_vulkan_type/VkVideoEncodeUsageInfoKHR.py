import ctypes

class VkVideoEncodeUsageInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'videoUsageHints': ctypes.c_uint32,
            'videoContentHints': ctypes.c_uint32,
            'tuningMode': ctypes.c_int,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('videoUsageHints', ctypes.c_uint32),
        ('videoContentHints', ctypes.c_uint32),
        ('tuningMode', ctypes.c_int),
    ]
