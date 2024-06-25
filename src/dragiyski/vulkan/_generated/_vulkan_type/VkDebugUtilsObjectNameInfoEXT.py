import ctypes

class VkDebugUtilsObjectNameInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'objectType': ctypes.c_int,
            'objectHandle': ctypes.c_uint64,
            'pObjectName': ctypes.c_char_p,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('objectType', ctypes.c_int),
        ('objectHandle', ctypes.c_uint64),
        ('pObjectName', ctypes.c_char_p),
    ]
