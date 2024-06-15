import ctypes, sys

class VkPhysicalDeviceExternalSciSyncFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('sciSyncFence', ctypes.c_uint32),
        ('sciSyncSemaphore', ctypes.c_uint32),
        ('sciSyncImport', ctypes.c_uint32),
        ('sciSyncExport', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceExternalSciSyncFeaturesNV
