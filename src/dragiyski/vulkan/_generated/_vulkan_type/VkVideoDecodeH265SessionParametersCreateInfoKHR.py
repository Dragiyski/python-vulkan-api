import ctypes, sys

class VkVideoDecodeH265SessionParametersCreateInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoDecodeH265SessionParametersCreateInfoKHR

from . import VkVideoDecodeH265SessionParametersAddInfoKHR

VkVideoDecodeH265SessionParametersCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxStdVPSCount', ctypes.c_uint32),
    ('maxStdSPSCount', ctypes.c_uint32),
    ('maxStdPPSCount', ctypes.c_uint32),
    ('pParametersAddInfo', ctypes.POINTER(VkVideoDecodeH265SessionParametersAddInfoKHR)),
]
