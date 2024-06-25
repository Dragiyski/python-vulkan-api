import ctypes

class VkPhysicalDeviceShaderImageAtomicInt64FeaturesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'shaderImageInt64Atomics': ctypes.c_uint32,
            'sparseImageInt64Atomics': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('shaderImageInt64Atomics', ctypes.c_uint32),
        ('sparseImageInt64Atomics', ctypes.c_uint32),
    ]
