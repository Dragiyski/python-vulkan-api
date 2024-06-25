import ctypes

class VkPhysicalDeviceProperties2(ctypes.Structure):
    pass

from .VkPhysicalDeviceProperties import VkPhysicalDeviceProperties

VkPhysicalDeviceProperties2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('properties', VkPhysicalDeviceProperties),
]

VkPhysicalDeviceProperties2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'properties': VkPhysicalDeviceProperties,
}
