import ctypes

class VkVideoProfileListInfoKHR(ctypes.Structure):
    pass

from .VkVideoProfileInfoKHR import VkVideoProfileInfoKHR

VkVideoProfileListInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('profileCount', ctypes.c_uint32),
    ('pProfiles', ctypes.POINTER(VkVideoProfileInfoKHR)),
]

VkVideoProfileListInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'profileCount': ctypes.c_uint32,
    'pProfiles': ctypes.POINTER(VkVideoProfileInfoKHR),
}
