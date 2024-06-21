import ctypes

class CType(ctypes.Structure):
    pass

from .VkPhysicalDeviceMemoryProperties import CType as VkPhysicalDeviceMemoryProperties

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryProperties', VkPhysicalDeviceMemoryProperties),
]
