import ctypes

class VkPhysicalDeviceExternalSciSync2FeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('sciSyncFence', ctypes.c_uint32),
        ('sciSyncSemaphore2', ctypes.c_uint32),
        ('sciSyncImport', ctypes.c_uint32),
        ('sciSyncExport', ctypes.c_uint32),
    ]

VkPhysicalDeviceExternalSciSync2FeaturesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'sciSyncFence': ctypes.c_uint32,
    'sciSyncSemaphore2': ctypes.c_uint32,
    'sciSyncImport': ctypes.c_uint32,
    'sciSyncExport': ctypes.c_uint32,
}
