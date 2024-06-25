import ctypes

class VkApplicationInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pApplicationName': ctypes.c_char_p,
            'applicationVersion': ctypes.c_uint32,
            'pEngineName': ctypes.c_char_p,
            'engineVersion': ctypes.c_uint32,
            'apiVersion': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pApplicationName', ctypes.c_char_p),
        ('applicationVersion', ctypes.c_uint32),
        ('pEngineName', ctypes.c_char_p),
        ('engineVersion', ctypes.c_uint32),
        ('apiVersion', ctypes.c_uint32),
    ]
