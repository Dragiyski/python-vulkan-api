import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoEncodeH264SessionParametersAddInfoKHR import CType as VkVideoEncodeH264SessionParametersAddInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('maxStdSPSCount', ctypes.c_uint32),
    ('maxStdPPSCount', ctypes.c_uint32),
    ('pParametersAddInfo', ctypes.POINTER(VkVideoEncodeH264SessionParametersAddInfoKHR)),
]
