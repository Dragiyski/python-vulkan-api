import ctypes

class VkDirectFBSurfaceCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('dfb', ctypes.c_void_p),
        ('surface', ctypes.c_void_p),
    ]

VkDirectFBSurfaceCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'dfb': ctypes.c_void_p,
    'surface': ctypes.c_void_p,
}
