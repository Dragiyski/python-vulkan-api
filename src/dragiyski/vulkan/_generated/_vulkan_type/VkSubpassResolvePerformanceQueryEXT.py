import ctypes

class VkSubpassResolvePerformanceQueryEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('optimal', ctypes.c_uint32),
    ]

VkSubpassResolvePerformanceQueryEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'optimal': ctypes.c_uint32,
}
