import ctypes

class VkXlibSurfaceCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('dpy', ctypes.c_void_p),
        ('window', ctypes.c_uint32),
    ]

VkXlibSurfaceCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'dpy': ctypes.c_void_p,
    'window': ctypes.c_uint32,
}
