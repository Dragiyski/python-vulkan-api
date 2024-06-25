import ctypes

class VkPhysicalDeviceImageDrmFormatModifierInfoEXT(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'drmFormatModifier': ctypes.c_uint64,
            'sharingMode': ctypes.c_int,
            'queueFamilyIndexCount': ctypes.c_uint32,
            'pQueueFamilyIndices': ctypes.POINTER(ctypes.c_uint32),
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('drmFormatModifier', ctypes.c_uint64),
        ('sharingMode', ctypes.c_int),
        ('queueFamilyIndexCount', ctypes.c_uint32),
        ('pQueueFamilyIndices', ctypes.POINTER(ctypes.c_uint32)),
    ]
