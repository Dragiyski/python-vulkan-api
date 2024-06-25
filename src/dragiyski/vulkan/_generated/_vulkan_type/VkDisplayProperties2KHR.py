import ctypes

class VkDisplayProperties2KHR(ctypes.Structure):
    pass

from .VkDisplayPropertiesKHR import VkDisplayPropertiesKHR

VkDisplayProperties2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('displayProperties', VkDisplayPropertiesKHR),
]

VkDisplayProperties2KHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'displayProperties': VkDisplayPropertiesKHR,
}
