import ctypes

class VkVideoDecodeAV1ProfileInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stdProfile', ctypes.c_int),
        ('filmGrainSupport', ctypes.c_uint32),
    ]

VkVideoDecodeAV1ProfileInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stdProfile': ctypes.c_int,
    'filmGrainSupport': ctypes.c_uint32,
}
