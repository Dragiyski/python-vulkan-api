import ctypes

class VkPhysicalDeviceRobustness2FeaturesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'robustBufferAccess2': ctypes.c_uint32,
            'robustImageAccess2': ctypes.c_uint32,
            'nullDescriptor': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('robustBufferAccess2', ctypes.c_uint32),
        ('robustImageAccess2', ctypes.c_uint32),
        ('nullDescriptor', ctypes.c_uint32),
    ]
