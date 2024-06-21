import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoProfileInfoKHR import CType as VkVideoProfileInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('profileCount', ctypes.c_uint32),
    ('pProfiles', ctypes.POINTER(VkVideoProfileInfoKHR)),
]
