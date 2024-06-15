import ctypes, sys

class VkVideoEncodeH265SessionParametersCreateInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoEncodeH265SessionParametersCreateInfoKHR

from . import VkVideoEncodeH265SessionParametersAddInfoKHR

VkVideoEncodeH265SessionParametersCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxStdVPSCount', ctypes.c_uint32),
    ('maxStdSPSCount', ctypes.c_uint32),
    ('maxStdPPSCount', ctypes.c_uint32),
    ('pParametersAddInfo', ctypes.POINTER(VkVideoEncodeH265SessionParametersAddInfoKHR)),
]
