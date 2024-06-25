import ctypes

class VkSurfaceProtectedCapabilitiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('supportsProtected', ctypes.c_uint32),
    ]

VkSurfaceProtectedCapabilitiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'supportsProtected': ctypes.c_uint32,
}
