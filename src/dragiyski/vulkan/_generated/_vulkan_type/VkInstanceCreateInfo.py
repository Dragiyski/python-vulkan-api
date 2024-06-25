import ctypes

class VkInstanceCreateInfo(ctypes.Structure):
    pass

from .VkApplicationInfo import VkApplicationInfo

VkInstanceCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pApplicationInfo', ctypes.POINTER(VkApplicationInfo)),
    ('enabledLayerCount', ctypes.c_uint32),
    ('ppEnabledLayerNames', ctypes.POINTER(ctypes.c_char_p)),
    ('enabledExtensionCount', ctypes.c_uint32),
    ('ppEnabledExtensionNames', ctypes.POINTER(ctypes.c_char_p)),
]

VkInstanceCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'pApplicationInfo': ctypes.POINTER(VkApplicationInfo),
    'enabledLayerCount': ctypes.c_uint32,
    'ppEnabledLayerNames': ctypes.POINTER(ctypes.c_char_p),
    'enabledExtensionCount': ctypes.c_uint32,
    'ppEnabledExtensionNames': ctypes.POINTER(ctypes.c_char_p),
}
