import ctypes

class VkPhysicalDeviceMemoryProperties2(ctypes.Structure):
    pass

from .VkPhysicalDeviceMemoryProperties import VkPhysicalDeviceMemoryProperties

VkPhysicalDeviceMemoryProperties2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('memoryProperties', VkPhysicalDeviceMemoryProperties),
]

VkPhysicalDeviceMemoryProperties2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'memoryProperties': VkPhysicalDeviceMemoryProperties,
}
