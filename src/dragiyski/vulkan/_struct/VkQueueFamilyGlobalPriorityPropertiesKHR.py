import ctypes, sys

class VkQueueFamilyGlobalPriorityPropertiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('priorityCount', ctypes.c_uint32),
        ('priorities', ctypes.ARRAY(ctypes.c_int, 16)),
    ]

sys.modules[__name__] = VkQueueFamilyGlobalPriorityPropertiesKHR
