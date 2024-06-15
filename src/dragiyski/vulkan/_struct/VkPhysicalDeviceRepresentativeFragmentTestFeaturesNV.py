import ctypes, sys

class VkPhysicalDeviceRepresentativeFragmentTestFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('representativeFragmentTest', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceRepresentativeFragmentTestFeaturesNV
