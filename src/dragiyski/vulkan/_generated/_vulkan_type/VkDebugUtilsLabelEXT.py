import ctypes

class VkDebugUtilsLabelEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pLabelName': ctypes.c_char_p,
            'color': ctypes.ARRAY(ctypes.c_float, 4),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pLabelName', ctypes.c_char_p),
        ('color', ctypes.ARRAY(ctypes.c_float, 4)),
    ]
