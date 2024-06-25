import ctypes

class VkPhysicalDeviceExternalImageFormatInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('handleType', ctypes.c_uint32),
    ]

VkPhysicalDeviceExternalImageFormatInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'handleType': ctypes.c_uint32,
}
