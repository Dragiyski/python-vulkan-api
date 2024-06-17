import ctypes, sys

class VkPhysicalDevice16BitStorageFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('storageBuffer16BitAccess', ctypes.c_uint32),
        ('uniformAndStorageBuffer16BitAccess', ctypes.c_uint32),
        ('storagePushConstant16', ctypes.c_uint32),
        ('storageInputOutput16', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDevice16BitStorageFeatures
