import ctypes

class VkSurfaceCapabilitiesPresentBarrierNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentBarrierSupported', ctypes.c_uint32),
    ]

VkSurfaceCapabilitiesPresentBarrierNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'presentBarrierSupported': ctypes.c_uint32,
}
