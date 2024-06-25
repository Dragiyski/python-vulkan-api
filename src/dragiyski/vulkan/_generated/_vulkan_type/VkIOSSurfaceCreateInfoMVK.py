import ctypes

class VkIOSSurfaceCreateInfoMVK(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('pView', ctypes.c_void_p),
    ]

VkIOSSurfaceCreateInfoMVK._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'pView': ctypes.c_void_p,
}
