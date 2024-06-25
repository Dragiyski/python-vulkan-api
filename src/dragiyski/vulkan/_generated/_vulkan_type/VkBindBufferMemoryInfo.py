import ctypes

class VkBindBufferMemoryInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('buffer', ctypes.c_void_p),
        ('memory', ctypes.c_void_p),
        ('memoryOffset', ctypes.c_uint64),
    ]

VkBindBufferMemoryInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'buffer': ctypes.c_void_p,
    'memory': ctypes.c_void_p,
    'memoryOffset': ctypes.c_uint64,
}
