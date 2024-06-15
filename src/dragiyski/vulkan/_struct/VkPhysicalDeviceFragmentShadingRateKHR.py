import ctypes, sys

class VkPhysicalDeviceFragmentShadingRateKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkPhysicalDeviceFragmentShadingRateKHR

from . import VkExtent2D

VkPhysicalDeviceFragmentShadingRateKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('sampleCounts', ctypes.c_uint32),
    ('fragmentSize', VkExtent2D),
]
