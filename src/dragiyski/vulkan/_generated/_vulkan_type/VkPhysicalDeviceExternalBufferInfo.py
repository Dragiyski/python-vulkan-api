import ctypes

class VkPhysicalDeviceExternalBufferInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('usage', ctypes.c_uint32),
        ('handleType', ctypes.c_uint32),
    ]

VkPhysicalDeviceExternalBufferInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'usage': ctypes.c_uint32,
    'handleType': ctypes.c_uint32,
}
