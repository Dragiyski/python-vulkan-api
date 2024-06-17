import ctypes, sys

class VkPhysicalDeviceSubgroupSizeControlFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('subgroupSizeControl', ctypes.c_uint32),
        ('computeFullSubgroups', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceSubgroupSizeControlFeatures
