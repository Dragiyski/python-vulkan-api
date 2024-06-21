import ctypes

class CType(ctypes.Structure):
    pass

from .VkDirectDriverLoadingInfoLUNARG import CType as VkDirectDriverLoadingInfoLUNARG

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('mode', ctypes.c_int),
    ('driverCount', ctypes.c_uint32),
    ('pDrivers', ctypes.POINTER(VkDirectDriverLoadingInfoLUNARG)),
]
