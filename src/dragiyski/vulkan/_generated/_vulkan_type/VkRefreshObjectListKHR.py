import ctypes

class CType(ctypes.Structure):
    pass

from .VkRefreshObjectKHR import CType as VkRefreshObjectKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('objectCount', ctypes.c_uint32),
    ('pObjects', ctypes.POINTER(VkRefreshObjectKHR)),
]
