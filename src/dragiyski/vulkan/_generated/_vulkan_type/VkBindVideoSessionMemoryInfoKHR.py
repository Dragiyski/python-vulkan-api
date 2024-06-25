import ctypes

class VkBindVideoSessionMemoryInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memoryBindIndex', ctypes.c_uint32),
        ('memory', ctypes.c_void_p),
        ('memoryOffset', ctypes.c_uint64),
        ('memorySize', ctypes.c_uint64),
    ]

VkBindVideoSessionMemoryInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'memoryBindIndex': ctypes.c_uint32,
    'memory': ctypes.c_void_p,
    'memoryOffset': ctypes.c_uint64,
    'memorySize': ctypes.c_uint64,
}
