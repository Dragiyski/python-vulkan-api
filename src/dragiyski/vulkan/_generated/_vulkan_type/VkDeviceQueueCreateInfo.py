import ctypes

class VkDeviceQueueCreateInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'queueFamilyIndex': ctypes.c_uint32,
            'queueCount': ctypes.c_uint32,
            'pQueuePriorities': ctypes.POINTER(ctypes.c_float),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('queueFamilyIndex', ctypes.c_uint32),
        ('queueCount', ctypes.c_uint32),
        ('pQueuePriorities', ctypes.POINTER(ctypes.c_float)),
    ]
