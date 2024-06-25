import ctypes

class VkDisplayPlaneCapabilities2KHR(ctypes.Structure):
    pass

from .VkDisplayPlaneCapabilitiesKHR import VkDisplayPlaneCapabilitiesKHR

VkDisplayPlaneCapabilities2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('capabilities', VkDisplayPlaneCapabilitiesKHR),
]

VkDisplayPlaneCapabilities2KHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'capabilities': VkDisplayPlaneCapabilitiesKHR,
}
