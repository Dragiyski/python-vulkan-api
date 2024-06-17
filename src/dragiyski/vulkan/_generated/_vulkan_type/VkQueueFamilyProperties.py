import ctypes, sys

class VkQueueFamilyProperties(ctypes.Structure):
    pass

sys.modules[__name__] = VkQueueFamilyProperties

from . import VkExtent3D

VkQueueFamilyProperties._fields_ = [
    ('queueFlags', ctypes.c_uint32),
    ('queueCount', ctypes.c_uint32),
    ('timestampValidBits', ctypes.c_uint32),
    ('minImageTransferGranularity', VkExtent3D),
]
