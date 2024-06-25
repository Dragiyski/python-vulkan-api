import ctypes

class VkVideoSessionParametersUpdateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('updateSequenceCount', ctypes.c_uint32),
    ]

VkVideoSessionParametersUpdateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'updateSequenceCount': ctypes.c_uint32,
}
