import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoEncodeH265SessionParametersAddInfoKHR import CType as VkVideoEncodeH265SessionParametersAddInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxStdVPSCount', ctypes.c_uint32),
    ('maxStdSPSCount', ctypes.c_uint32),
    ('maxStdPPSCount', ctypes.c_uint32),
    ('pParametersAddInfo', ctypes.POINTER(VkVideoEncodeH265SessionParametersAddInfoKHR)),
]
