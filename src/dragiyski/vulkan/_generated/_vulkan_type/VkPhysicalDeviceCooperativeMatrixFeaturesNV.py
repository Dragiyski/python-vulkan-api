import ctypes, sys

class VkPhysicalDeviceCooperativeMatrixFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('cooperativeMatrix', ctypes.c_uint32),
        ('cooperativeMatrixRobustBufferAccess', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceCooperativeMatrixFeaturesNV
