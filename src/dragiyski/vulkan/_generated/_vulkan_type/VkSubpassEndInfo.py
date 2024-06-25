import ctypes

class VkSubpassEndInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
    ]

VkSubpassEndInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
}
