import ctypes, sys

class VkPhysicalDeviceFragmentDensityMapOffsetPropertiesQCOM(ctypes.Structure):
    pass

sys.modules[__name__] = VkPhysicalDeviceFragmentDensityMapOffsetPropertiesQCOM

from . import VkExtent2D

VkPhysicalDeviceFragmentDensityMapOffsetPropertiesQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('fragmentDensityOffsetGranularity', VkExtent2D),
]
