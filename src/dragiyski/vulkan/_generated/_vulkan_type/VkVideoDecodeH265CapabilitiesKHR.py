import ctypes

class VkVideoDecodeH265CapabilitiesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxLevelIdc', ctypes.c_int),
    ]

VkVideoDecodeH265CapabilitiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxLevelIdc': ctypes.c_int,
}
