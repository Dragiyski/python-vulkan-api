import ctypes

class VkVideoEncodeH264SessionCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('useMaxLevelIdc', ctypes.c_uint32),
        ('maxLevelIdc', ctypes.c_int),
    ]

VkVideoEncodeH264SessionCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'useMaxLevelIdc': ctypes.c_uint32,
    'maxLevelIdc': ctypes.c_int,
}
