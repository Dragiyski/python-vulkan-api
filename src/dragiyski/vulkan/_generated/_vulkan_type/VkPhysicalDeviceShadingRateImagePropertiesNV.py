import ctypes, sys

class VkPhysicalDeviceShadingRateImagePropertiesNV(ctypes.Structure):
    pass

sys.modules[__name__] = VkPhysicalDeviceShadingRateImagePropertiesNV

from . import VkExtent2D

VkPhysicalDeviceShadingRateImagePropertiesNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('shadingRateTexelSize', VkExtent2D),
    ('shadingRatePaletteSize', ctypes.c_uint32),
    ('shadingRateMaxCoarseSamples', ctypes.c_uint32),
]
