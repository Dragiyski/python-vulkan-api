import ctypes

class VkDebugUtilsObjectTagInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'objectType': ctypes.c_int,
            'objectHandle': ctypes.c_uint64,
            'tagName': ctypes.c_uint64,
            'tagSize': ctypes.c_size_t,
            'pTag': ctypes.c_void_p,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('objectType', ctypes.c_int),
        ('objectHandle', ctypes.c_uint64),
        ('tagName', ctypes.c_uint64),
        ('tagSize', ctypes.c_size_t),
        ('pTag', ctypes.c_void_p),
    ]
