import ctypes, sys

class VkDeviceQueueCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('queueFamilyIndex', ctypes.c_uint32),
        ('queueCount', ctypes.c_uint32),
        ('pQueuePriorities', ctypes.POINTER(ctypes.c_float)),
    ]

sys.modules[__name__] = VkDeviceQueueCreateInfo
