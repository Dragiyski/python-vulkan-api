import ctypes, sys

class VkPhysicalDeviceFragmentDensityMapOffsetFeaturesQCOM(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fragmentDensityMapOffset', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceFragmentDensityMapOffsetFeaturesQCOM
