import ctypes

class VkPhysicalDeviceMemoryBudgetPropertiesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'heapBudget': ctypes.ARRAY(ctypes.c_uint64, 16),
            'heapUsage': ctypes.ARRAY(ctypes.c_uint64, 16),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('heapBudget', ctypes.ARRAY(ctypes.c_uint64, 16)),
        ('heapUsage', ctypes.ARRAY(ctypes.c_uint64, 16)),
    ]
