import ctypes

class VkPhysicalDeviceShaderFloat16Int8Features(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'shaderFloat16': ctypes.c_uint32,
            'shaderInt8': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderFloat16', ctypes.c_uint32),
        ('shaderInt8', ctypes.c_uint32),
    ]
