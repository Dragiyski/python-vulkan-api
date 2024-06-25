import ctypes

class VkVideoDecodeH265ProfileInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stdProfileIdc', ctypes.c_int),
    ]

VkVideoDecodeH265ProfileInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stdProfileIdc': ctypes.c_int,
}
