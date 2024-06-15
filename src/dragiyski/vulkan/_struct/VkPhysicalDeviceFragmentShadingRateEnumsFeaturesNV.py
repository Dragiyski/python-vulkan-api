import ctypes, sys

class VkPhysicalDeviceFragmentShadingRateEnumsFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fragmentShadingRateEnums', ctypes.c_uint32),
        ('supersampleFragmentShadingRates', ctypes.c_uint32),
        ('noInvocationFragmentShadingRates', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceFragmentShadingRateEnumsFeaturesNV
