import ctypes

class VkPhysicalDeviceToolProperties(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'name': ctypes.ARRAY(ctypes.c_char, 256),
            'version': ctypes.ARRAY(ctypes.c_char, 256),
            'purposes': ctypes.c_uint32,
            'description': ctypes.ARRAY(ctypes.c_char, 256),
            'layer': ctypes.ARRAY(ctypes.c_char, 256),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('name', ctypes.ARRAY(ctypes.c_char, 256)),
        ('version', ctypes.ARRAY(ctypes.c_char, 256)),
        ('purposes', ctypes.c_uint32),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
        ('layer', ctypes.ARRAY(ctypes.c_char, 256)),
    ]
