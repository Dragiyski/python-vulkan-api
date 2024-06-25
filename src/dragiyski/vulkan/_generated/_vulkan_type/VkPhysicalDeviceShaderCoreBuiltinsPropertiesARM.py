import ctypes

class VkPhysicalDeviceShaderCoreBuiltinsPropertiesARM(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'shaderCoreMask': ctypes.c_uint64,
            'shaderCoreCount': ctypes.c_uint32,
            'shaderWarpsPerCore': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderCoreMask', ctypes.c_uint64),
        ('shaderCoreCount', ctypes.c_uint32),
        ('shaderWarpsPerCore', ctypes.c_uint32),
    ]
