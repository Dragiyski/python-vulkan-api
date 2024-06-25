import ctypes

class VkPhysicalDeviceLineRasterizationFeaturesKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'rectangularLines': ctypes.c_uint32,
            'bresenhamLines': ctypes.c_uint32,
            'smoothLines': ctypes.c_uint32,
            'stippledRectangularLines': ctypes.c_uint32,
            'stippledBresenhamLines': ctypes.c_uint32,
            'stippledSmoothLines': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('rectangularLines', ctypes.c_uint32),
        ('bresenhamLines', ctypes.c_uint32),
        ('smoothLines', ctypes.c_uint32),
        ('stippledRectangularLines', ctypes.c_uint32),
        ('stippledBresenhamLines', ctypes.c_uint32),
        ('stippledSmoothLines', ctypes.c_uint32),
    ]
