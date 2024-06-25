import ctypes

class VkAndroidHardwareBufferUsageANDROID(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('androidHardwareBufferUsage', ctypes.c_uint64),
    ]

VkAndroidHardwareBufferUsageANDROID._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'androidHardwareBufferUsage': ctypes.c_uint64,
}
