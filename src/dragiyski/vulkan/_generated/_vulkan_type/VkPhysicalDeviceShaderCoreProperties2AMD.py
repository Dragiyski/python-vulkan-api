import ctypes

class VkPhysicalDeviceShaderCoreProperties2AMD(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'shaderCoreFeatures': ctypes.c_uint32,
            'activeComputeUnitCount': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderCoreFeatures', ctypes.c_uint32),
        ('activeComputeUnitCount', ctypes.c_uint32),
    ]
