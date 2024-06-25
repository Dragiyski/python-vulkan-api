import ctypes

class VkDisplayPlaneProperties2KHR(ctypes.Structure):
    pass

from .VkDisplayPlanePropertiesKHR import VkDisplayPlanePropertiesKHR

VkDisplayPlaneProperties2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displayPlaneProperties', VkDisplayPlanePropertiesKHR),
]

VkDisplayPlaneProperties2KHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'displayPlaneProperties': VkDisplayPlanePropertiesKHR,
}
