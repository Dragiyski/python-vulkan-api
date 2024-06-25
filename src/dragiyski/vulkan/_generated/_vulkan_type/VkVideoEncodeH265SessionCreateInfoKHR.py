import ctypes

class VkVideoEncodeH265SessionCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('useMaxLevelIdc', ctypes.c_uint32),
        ('maxLevelIdc', ctypes.c_int),
    ]

VkVideoEncodeH265SessionCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'useMaxLevelIdc': ctypes.c_uint32,
    'maxLevelIdc': ctypes.c_int,
}
