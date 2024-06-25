import ctypes

class VkVideoEncodeH265SessionParametersCreateInfoKHR(ctypes.Structure):
    pass

from .VkVideoEncodeH265SessionParametersAddInfoKHR import VkVideoEncodeH265SessionParametersAddInfoKHR

VkVideoEncodeH265SessionParametersCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxStdVPSCount', ctypes.c_uint32),
    ('maxStdSPSCount', ctypes.c_uint32),
    ('maxStdPPSCount', ctypes.c_uint32),
    ('pParametersAddInfo', ctypes.POINTER(VkVideoEncodeH265SessionParametersAddInfoKHR)),
]

VkVideoEncodeH265SessionParametersCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'maxStdVPSCount': ctypes.c_uint32,
    'maxStdSPSCount': ctypes.c_uint32,
    'maxStdPPSCount': ctypes.c_uint32,
    'pParametersAddInfo': ctypes.POINTER(VkVideoEncodeH265SessionParametersAddInfoKHR),
}
