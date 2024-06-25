import ctypes

class VkQueueFamilyProperties2(ctypes.Structure):
    pass

from .VkQueueFamilyProperties import VkQueueFamilyProperties

VkQueueFamilyProperties2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('queueFamilyProperties', VkQueueFamilyProperties),
]

VkQueueFamilyProperties2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'queueFamilyProperties': VkQueueFamilyProperties,
}
