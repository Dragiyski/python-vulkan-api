import ctypes

class VkPhysicalDeviceSubgroupSizeControlFeatures(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'subgroupSizeControl': ctypes.c_uint32,
            'computeFullSubgroups': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('subgroupSizeControl', ctypes.c_uint32),
        ('computeFullSubgroups', ctypes.c_uint32),
    ]
