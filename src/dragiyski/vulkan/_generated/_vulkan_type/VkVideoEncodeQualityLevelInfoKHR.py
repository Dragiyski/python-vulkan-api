import ctypes

class VkVideoEncodeQualityLevelInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('qualityLevel', ctypes.c_uint32),
    ]

VkVideoEncodeQualityLevelInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'qualityLevel': ctypes.c_uint32,
}
