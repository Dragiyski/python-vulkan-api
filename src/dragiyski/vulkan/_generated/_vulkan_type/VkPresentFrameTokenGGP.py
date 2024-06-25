import ctypes

class VkPresentFrameTokenGGP(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('frameToken', ctypes.c_uint32),
    ]

VkPresentFrameTokenGGP._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'frameToken': ctypes.c_uint32,
}
