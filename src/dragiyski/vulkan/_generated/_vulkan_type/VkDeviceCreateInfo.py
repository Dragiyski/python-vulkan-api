import ctypes

class VkDeviceCreateInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'queueCreateInfoCount': ctypes.c_uint32,
            'pQueueCreateInfos': ctypes.POINTER(VkDeviceQueueCreateInfo),
            'enabledLayerCount': ctypes.c_uint32,
            'ppEnabledLayerNames': ctypes.POINTER(ctypes.c_char_p),
            'enabledExtensionCount': ctypes.c_uint32,
            'ppEnabledExtensionNames': ctypes.POINTER(ctypes.c_char_p),
            'pEnabledFeatures': ctypes.POINTER(VkPhysicalDeviceFeatures),
        }


from .VkDeviceQueueCreateInfo import VkDeviceQueueCreateInfo
from .VkPhysicalDeviceFeatures import VkPhysicalDeviceFeatures

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
