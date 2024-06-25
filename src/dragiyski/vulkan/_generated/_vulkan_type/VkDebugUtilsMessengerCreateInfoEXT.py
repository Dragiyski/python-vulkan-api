import ctypes

class VkDebugUtilsMessengerCreateInfoEXT(ctypes.Structure):
    pass

from .._vulkan_callback.vkDebugUtilsMessengerCallbackEXT import vkDebugUtilsMessengerCallbackEXT

VkDebugUtilsMessengerCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('messageSeverity', ctypes.c_uint32),
    ('messageType', ctypes.c_uint32),
    ('pfnUserCallback', vkDebugUtilsMessengerCallbackEXT),
    ('pUserData', ctypes.c_void_p),
]

VkDebugUtilsMessengerCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'messageSeverity': ctypes.c_uint32,
    'messageType': ctypes.c_uint32,
    'pfnUserCallback': vkDebugUtilsMessengerCallbackEXT,
    'pUserData': ctypes.c_void_p,
}
