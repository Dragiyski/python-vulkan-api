import ctypes

class VkPhysicalDeviceShaderCorePropertiesARM(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pixelRate': ctypes.c_uint32,
            'texelRate': ctypes.c_uint32,
            'fmaRate': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pixelRate', ctypes.c_uint32),
        ('texelRate', ctypes.c_uint32),
        ('fmaRate', ctypes.c_uint32),
    ]
