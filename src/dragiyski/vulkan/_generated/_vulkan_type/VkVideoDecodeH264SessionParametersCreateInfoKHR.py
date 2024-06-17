import ctypes, sys

class VkVideoDecodeH264SessionParametersCreateInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoDecodeH264SessionParametersCreateInfoKHR

from . import VkVideoDecodeH264SessionParametersAddInfoKHR

VkVideoDecodeH264SessionParametersCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxStdSPSCount', ctypes.c_uint32),
    ('maxStdPPSCount', ctypes.c_uint32),
    ('pParametersAddInfo', ctypes.POINTER(VkVideoDecodeH264SessionParametersAddInfoKHR)),
]
