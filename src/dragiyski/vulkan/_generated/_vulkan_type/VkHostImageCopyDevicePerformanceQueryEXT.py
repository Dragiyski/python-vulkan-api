import ctypes

class VkHostImageCopyDevicePerformanceQueryEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('optimalDeviceAccess', ctypes.c_uint32),
        ('identicalMemoryLayout', ctypes.c_uint32),
    ]

VkHostImageCopyDevicePerformanceQueryEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'optimalDeviceAccess': ctypes.c_uint32,
    'identicalMemoryLayout': ctypes.c_uint32,
}
