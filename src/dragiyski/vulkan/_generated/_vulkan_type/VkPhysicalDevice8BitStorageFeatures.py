import ctypes

class VkPhysicalDevice8BitStorageFeatures(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('storageBuffer8BitAccess', ctypes.c_uint32),
        ('uniformAndStorageBuffer8BitAccess', ctypes.c_uint32),
        ('storagePushConstant8', ctypes.c_uint32),
    ]

VkPhysicalDevice8BitStorageFeatures._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'storageBuffer8BitAccess': ctypes.c_uint32,
    'uniformAndStorageBuffer8BitAccess': ctypes.c_uint32,
    'storagePushConstant8': ctypes.c_uint32,
}
