import ctypes, sys

class VkVideoProfileListInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoProfileListInfoKHR

from . import VkVideoProfileInfoKHR

VkVideoProfileListInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('profileCount', ctypes.c_uint32),
    ('pProfiles', ctypes.POINTER(VkVideoProfileInfoKHR)),
]
