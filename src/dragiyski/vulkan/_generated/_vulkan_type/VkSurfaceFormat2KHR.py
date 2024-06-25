import ctypes

class VkSurfaceFormat2KHR(ctypes.Structure):
    pass

from .VkSurfaceFormatKHR import VkSurfaceFormatKHR

VkSurfaceFormat2KHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('surfaceFormat', VkSurfaceFormatKHR),
]

VkSurfaceFormat2KHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'surfaceFormat': VkSurfaceFormatKHR,
}
