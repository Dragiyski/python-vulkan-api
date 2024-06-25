import ctypes

class VkPhysicalDeviceMaintenance3Properties(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'maxPerSetDescriptors': ctypes.c_uint32,
            'maxMemoryAllocationSize': ctypes.c_uint64,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxPerSetDescriptors', ctypes.c_uint32),
        ('maxMemoryAllocationSize', ctypes.c_uint64),
    ]
