import ctypes, sys

class VkPhysicalDeviceFragmentShadingRateEnumsPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxFragmentShadingRateInvocationCount', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceFragmentShadingRateEnumsPropertiesNV
