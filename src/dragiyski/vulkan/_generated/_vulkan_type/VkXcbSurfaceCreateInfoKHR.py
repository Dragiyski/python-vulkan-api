import ctypes

class VkXcbSurfaceCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('connection', ctypes.c_void_p),
        ('window', ctypes.c_uint32),
    ]

VkXcbSurfaceCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'connection': ctypes.c_void_p,
    'window': ctypes.c_uint32,
}
