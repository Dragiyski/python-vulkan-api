import ctypes, sys

class VkDirectDriverLoadingListLUNARG(ctypes.Structure):
    pass

sys.modules[__name__] = VkDirectDriverLoadingListLUNARG

from . import VkDirectDriverLoadingInfoLUNARG

VkDirectDriverLoadingListLUNARG._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('mode', ctypes.c_int),
    ('driverCount', ctypes.c_uint32),
    ('pDrivers', ctypes.POINTER(VkDirectDriverLoadingInfoLUNARG)),
]
