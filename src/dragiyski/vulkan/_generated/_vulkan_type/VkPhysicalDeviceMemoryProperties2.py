import ctypes, sys

class VkPhysicalDeviceMemoryProperties2(ctypes.Structure):
    pass

sys.modules[__name__] = VkPhysicalDeviceMemoryProperties2

from . import VkPhysicalDeviceMemoryProperties

VkPhysicalDeviceMemoryProperties2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryProperties', VkPhysicalDeviceMemoryProperties),
]
