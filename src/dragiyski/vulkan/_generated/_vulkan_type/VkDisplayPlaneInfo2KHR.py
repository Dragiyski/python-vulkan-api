import ctypes

class VkDisplayPlaneInfo2KHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('mode', ctypes.c_void_p),
        ('planeIndex', ctypes.c_uint32),
    ]

VkDisplayPlaneInfo2KHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'mode': ctypes.c_void_p,
    'planeIndex': ctypes.c_uint32,
}
