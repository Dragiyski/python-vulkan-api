import ctypes, sys

class VkHostImageCopyDevicePerformanceQueryEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('optimalDeviceAccess', ctypes.c_uint32),
        ('identicalMemoryLayout', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkHostImageCopyDevicePerformanceQueryEXT
