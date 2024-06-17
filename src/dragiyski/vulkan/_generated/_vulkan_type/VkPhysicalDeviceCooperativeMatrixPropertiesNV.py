import ctypes, sys

class VkPhysicalDeviceCooperativeMatrixPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('cooperativeMatrixSupportedStages', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceCooperativeMatrixPropertiesNV
