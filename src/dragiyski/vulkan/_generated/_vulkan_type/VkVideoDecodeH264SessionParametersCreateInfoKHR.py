import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoDecodeH264SessionParametersAddInfoKHR import CType as VkVideoDecodeH264SessionParametersAddInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxStdSPSCount', ctypes.c_uint32),
    ('maxStdPPSCount', ctypes.c_uint32),
    ('pParametersAddInfo', ctypes.POINTER(VkVideoDecodeH264SessionParametersAddInfoKHR)),
]
