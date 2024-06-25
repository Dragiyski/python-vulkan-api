import ctypes

class VkVideoDecodeAV1CapabilitiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxLevel', ctypes.c_int),
    ]

VkVideoDecodeAV1CapabilitiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxLevel': ctypes.c_int,
}
