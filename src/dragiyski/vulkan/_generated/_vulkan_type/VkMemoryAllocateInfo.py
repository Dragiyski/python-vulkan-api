import ctypes

class VkMemoryAllocateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('allocationSize', ctypes.c_uint64),
        ('memoryTypeIndex', ctypes.c_uint32),
    ]

VkMemoryAllocateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'allocationSize': ctypes.c_uint64,
    'memoryTypeIndex': ctypes.c_uint32,
}
