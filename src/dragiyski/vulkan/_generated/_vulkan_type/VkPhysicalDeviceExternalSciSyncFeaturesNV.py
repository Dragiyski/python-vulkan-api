import ctypes

class VkPhysicalDeviceExternalSciSyncFeaturesNV(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'sciSyncFence': ctypes.c_uint32,
            'sciSyncSemaphore': ctypes.c_uint32,
            'sciSyncImport': ctypes.c_uint32,
            'sciSyncExport': ctypes.c_uint32,
        }

    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('sciSyncFence', ctypes.c_uint32),
        ('sciSyncSemaphore', ctypes.c_uint32),
        ('sciSyncImport', ctypes.c_uint32),
        ('sciSyncExport', ctypes.c_uint32),
    ]
