import ctypes

class VkVideoEncodeSessionParametersGetInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('videoSessionParameters', ctypes.c_void_p),
    ]

VkVideoEncodeSessionParametersGetInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'videoSessionParameters': ctypes.c_void_p,
}
