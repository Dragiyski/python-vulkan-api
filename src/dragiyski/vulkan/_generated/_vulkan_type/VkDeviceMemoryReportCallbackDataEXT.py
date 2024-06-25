import ctypes

class VkDeviceMemoryReportCallbackDataEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('type', ctypes.c_int),
        ('memoryObjectId', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
        ('objectType', ctypes.c_int),
        ('objectHandle', ctypes.c_uint64),
        ('heapIndex', ctypes.c_uint32),
    ]

VkDeviceMemoryReportCallbackDataEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'type': ctypes.c_int,
    'memoryObjectId': ctypes.c_uint64,
    'size': ctypes.c_uint64,
    'objectType': ctypes.c_int,
    'objectHandle': ctypes.c_uint64,
    'heapIndex': ctypes.c_uint32,
}
