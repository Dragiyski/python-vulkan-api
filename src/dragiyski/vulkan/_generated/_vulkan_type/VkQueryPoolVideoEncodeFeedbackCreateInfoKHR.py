import ctypes

class VkQueryPoolVideoEncodeFeedbackCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('encodeFeedbackFlags', ctypes.c_uint32),
    ]

VkQueryPoolVideoEncodeFeedbackCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'encodeFeedbackFlags': ctypes.c_uint32,
}
