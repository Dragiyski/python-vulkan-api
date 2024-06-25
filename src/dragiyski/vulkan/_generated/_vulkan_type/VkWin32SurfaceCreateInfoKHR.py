import ctypes

class VkWin32SurfaceCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('hinstance', ctypes.c_void_p),
        ('hwnd', ctypes.c_void_p),
    ]

VkWin32SurfaceCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'hinstance': ctypes.c_void_p,
    'hwnd': ctypes.c_void_p,
}
