import ctypes

class VkPhysicalDeviceSubgroupSizeControlProperties(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'minSubgroupSize': ctypes.c_uint32,
            'maxSubgroupSize': ctypes.c_uint32,
            'maxComputeWorkgroupSubgroups': ctypes.c_uint32,
            'requiredSubgroupSizeStages': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('minSubgroupSize', ctypes.c_uint32),
        ('maxSubgroupSize', ctypes.c_uint32),
        ('maxComputeWorkgroupSubgroups', ctypes.c_uint32),
        ('requiredSubgroupSizeStages', ctypes.c_uint32),
    ]
