import ctypes, sys

class VkDebugUtilsMessengerCreateInfoEXT(ctypes.Structure):
    pass

sys.modules[__name__] = VkDebugUtilsMessengerCreateInfoEXT

from .._vulkan_callback import vkDebugUtilsMessengerCallbackEXT

VkDebugUtilsMessengerCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('messageSeverity', ctypes.c_uint32),
    ('messageType', ctypes.c_uint32),
    ('pfnUserCallback', ctypes.POINTER(vkDebugUtilsMessengerCallbackEXT)),
    ('pUserData', ctypes.c_void_p),
]
