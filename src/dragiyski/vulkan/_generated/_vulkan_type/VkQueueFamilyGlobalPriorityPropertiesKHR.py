import ctypes

class VkQueueFamilyGlobalPriorityPropertiesKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'priorityCount': ctypes.c_uint32,
            'priorities': ctypes.ARRAY(ctypes.c_int, 16),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('priorityCount', ctypes.c_uint32),
        ('priorities', ctypes.ARRAY(ctypes.c_int, 16)),
    ]
