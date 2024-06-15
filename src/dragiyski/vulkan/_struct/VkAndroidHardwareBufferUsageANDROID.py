import ctypes, sys

class VkAndroidHardwareBufferUsageANDROID(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('androidHardwareBufferUsage', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkAndroidHardwareBufferUsageANDROID
