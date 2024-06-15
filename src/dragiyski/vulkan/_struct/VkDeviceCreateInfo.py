import ctypes, sys

class VkDeviceCreateInfo(ctypes.Structure):
    pass

sys.modules[__name__] = VkDeviceCreateInfo

from . import VkPhysicalDeviceFeatures
from . import VkDeviceQueueCreateInfo

VkDeviceCreateInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('queueCreateInfoCount', ctypes.c_uint32),
    ('pQueueCreateInfos', ctypes.POINTER(VkDeviceQueueCreateInfo)),
    ('enabledLayerCount', ctypes.c_uint32),
    ('ppEnabledLayerNames', ctypes.POINTER(ctypes.c_char_p)),
    ('enabledExtensionCount', ctypes.c_uint32),
    ('ppEnabledExtensionNames', ctypes.POINTER(ctypes.c_char_p)),
    ('pEnabledFeatures', ctypes.POINTER(VkPhysicalDeviceFeatures)),
]
