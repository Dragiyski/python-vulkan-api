import ctypes

class VkSurfaceCapabilities2KHR(ctypes.Structure):
    pass

from .VkSurfaceCapabilitiesKHR import VkSurfaceCapabilitiesKHR

VkSurfaceCapabilities2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('surfaceCapabilities', VkSurfaceCapabilitiesKHR),
]

VkSurfaceCapabilities2KHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'surfaceCapabilities': VkSurfaceCapabilitiesKHR,
}
