import ctypes, sys

class VkVideoEncodeH264SessionParametersCreateInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoEncodeH264SessionParametersCreateInfoKHR

from . import VkVideoEncodeH264SessionParametersAddInfoKHR

VkVideoEncodeH264SessionParametersCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxStdSPSCount', ctypes.c_uint32),
    ('maxStdPPSCount', ctypes.c_uint32),
    ('pParametersAddInfo', ctypes.POINTER(VkVideoEncodeH264SessionParametersAddInfoKHR)),
]
