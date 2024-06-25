import ctypes

class VkDisplayModePropertiesKHR(ctypes.Structure):
    pass

from .VkDisplayModeParametersKHR import VkDisplayModeParametersKHR

VkDisplayModePropertiesKHR._fields_ = [
    ('displayMode', ctypes.c_void_p),
    ('parameters', VkDisplayModeParametersKHR),
]

VkDisplayModePropertiesKHR._type_ = {
    'displayMode': ctypes.c_void_p,
    'parameters': VkDisplayModeParametersKHR,
}
