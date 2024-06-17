import ctypes, sys

class VkInstanceCreateInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkInstanceCreateInfo

from . import VkApplicationInfo

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
