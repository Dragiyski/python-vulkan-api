import ctypes, sys

class VkPhysicalDeviceFragmentDensityMap2FeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fragmentDensityMapDeferred', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceFragmentDensityMap2FeaturesEXT
