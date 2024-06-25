import ctypes

class VkLatencySurfaceCapabilitiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('presentModeCount', ctypes.c_uint32),
        ('pPresentModes', ctypes.POINTER(ctypes.c_int)),
    ]

VkLatencySurfaceCapabilitiesNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'presentModeCount': ctypes.c_uint32,
    'pPresentModes': ctypes.POINTER(ctypes.c_int),
}
