import ctypes

class VkPhysicalDeviceSubgroupProperties(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'subgroupSize': ctypes.c_uint32,
            'supportedStages': ctypes.c_uint32,
            'supportedOperations': ctypes.c_uint32,
            'quadOperationsInAllStages': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('subgroupSize', ctypes.c_uint32),
        ('supportedStages', ctypes.c_uint32),
        ('supportedOperations', ctypes.c_uint32),
        ('quadOperationsInAllStages', ctypes.c_uint32),
    ]
