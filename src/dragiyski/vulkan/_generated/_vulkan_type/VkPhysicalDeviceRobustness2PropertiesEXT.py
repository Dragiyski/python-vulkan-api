import ctypes

class VkPhysicalDeviceRobustness2PropertiesEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'robustStorageBufferAccessSizeAlignment': ctypes.c_uint64,
            'robustUniformBufferAccessSizeAlignment': ctypes.c_uint64,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('robustStorageBufferAccessSizeAlignment', ctypes.c_uint64),
        ('robustUniformBufferAccessSizeAlignment', ctypes.c_uint64),
    ]
