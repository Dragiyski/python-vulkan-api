import ctypes

class VkMemoryGetAndroidHardwareBufferInfoANDROID(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memory', ctypes.c_void_p),
    ]

VkMemoryGetAndroidHardwareBufferInfoANDROID._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'memory': ctypes.c_void_p,
}
