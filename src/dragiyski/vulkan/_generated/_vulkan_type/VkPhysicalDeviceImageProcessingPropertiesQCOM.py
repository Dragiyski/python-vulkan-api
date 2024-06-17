import ctypes, sys

class VkPhysicalDeviceImageProcessingPropertiesQCOM(ctypes.Structure):
    pass

sys.modules[__name__] = VkPhysicalDeviceImageProcessingPropertiesQCOM

from . import VkExtent2D

VkPhysicalDeviceImageProcessingPropertiesQCOM._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxWeightFilterPhases', ctypes.c_uint32),
    ('maxWeightFilterDimension', VkExtent2D),
    ('maxBlockMatchRegion', VkExtent2D),
    ('maxBoxFilterBlockSize', VkExtent2D),
]
