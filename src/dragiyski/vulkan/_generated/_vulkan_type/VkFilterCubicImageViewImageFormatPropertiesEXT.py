import ctypes

class VkFilterCubicImageViewImageFormatPropertiesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'filterCubic': ctypes.c_uint32,
            'filterCubicMinmax': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('filterCubic', ctypes.c_uint32),
        ('filterCubicMinmax', ctypes.c_uint32),
    ]
