import ctypes

class VkPhysicalDevice4444FormatsFeaturesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'formatA4R4G4B4': ctypes.c_uint32,
            'formatA4B4G4R4': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('formatA4R4G4B4', ctypes.c_uint32),
        ('formatA4B4G4R4', ctypes.c_uint32),
    ]
