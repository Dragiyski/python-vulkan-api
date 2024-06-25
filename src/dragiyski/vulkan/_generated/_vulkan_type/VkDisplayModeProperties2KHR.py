import ctypes

class VkDisplayModeProperties2KHR(ctypes.Structure):
    pass

from .VkDisplayModePropertiesKHR import VkDisplayModePropertiesKHR

VkDisplayModeProperties2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displayModeProperties', VkDisplayModePropertiesKHR),
]

VkDisplayModeProperties2KHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'displayModeProperties': VkDisplayModePropertiesKHR,
}
