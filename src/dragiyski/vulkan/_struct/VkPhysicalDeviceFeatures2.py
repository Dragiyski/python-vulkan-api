import ctypes, sys

class VkPhysicalDeviceFeatures2(ctypes.Structure):
    pass

sys.modules[__name__] = VkPhysicalDeviceFeatures2

from . import VkPhysicalDeviceFeatures

VkPhysicalDeviceFeatures2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('features', VkPhysicalDeviceFeatures),
]
