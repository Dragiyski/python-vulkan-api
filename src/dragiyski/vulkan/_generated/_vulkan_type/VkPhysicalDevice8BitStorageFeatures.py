import ctypes

class VkPhysicalDevice8BitStorageFeatures(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'storageBuffer8BitAccess': ctypes.c_uint32,
            'uniformAndStorageBuffer8BitAccess': ctypes.c_uint32,
            'storagePushConstant8': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('storageBuffer8BitAccess', ctypes.c_uint32),
        ('uniformAndStorageBuffer8BitAccess', ctypes.c_uint32),
        ('storagePushConstant8', ctypes.c_uint32),
    ]
