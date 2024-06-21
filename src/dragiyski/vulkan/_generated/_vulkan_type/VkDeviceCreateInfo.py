import ctypes

class CType(ctypes.Structure):
    pass

from .VkDeviceQueueCreateInfo import CType as VkDeviceQueueCreateInfo
from .VkPhysicalDeviceFeatures import CType as VkPhysicalDeviceFeatures

CType._fields_ = [
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
