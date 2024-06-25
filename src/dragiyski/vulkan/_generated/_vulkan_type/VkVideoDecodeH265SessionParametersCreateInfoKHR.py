import ctypes

class VkVideoDecodeH265SessionParametersCreateInfoKHR(ctypes.Structure):
    pass

from .VkVideoDecodeH265SessionParametersAddInfoKHR import VkVideoDecodeH265SessionParametersAddInfoKHR

VkVideoDecodeH265SessionParametersCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxStdVPSCount', ctypes.c_uint32),
    ('maxStdSPSCount', ctypes.c_uint32),
    ('maxStdPPSCount', ctypes.c_uint32),
    ('pParametersAddInfo', ctypes.POINTER(VkVideoDecodeH265SessionParametersAddInfoKHR)),
]

VkVideoDecodeH265SessionParametersCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxStdVPSCount': ctypes.c_uint32,
    'maxStdSPSCount': ctypes.c_uint32,
    'maxStdPPSCount': ctypes.c_uint32,
    'pParametersAddInfo': ctypes.POINTER(VkVideoDecodeH265SessionParametersAddInfoKHR),
}
