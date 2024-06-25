import ctypes

class VkImportFenceFdInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fence', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('handleType', ctypes.c_uint32),
        ('fd', ctypes.c_int),
    ]

VkImportFenceFdInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'fence': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'handleType': ctypes.c_uint32,
    'fd': ctypes.c_int,
}
