import ctypes

class VkDisplayModeCreateInfoKHR(ctypes.Structure):
    pass

from .VkDisplayModeParametersKHR import VkDisplayModeParametersKHR

VkDisplayModeCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('parameters', VkDisplayModeParametersKHR),
]

VkDisplayModeCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'parameters': VkDisplayModeParametersKHR,
}
