import ctypes

class CType(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstKHR import CType as VkDeviceOrHostAddressConstKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('src', VkDeviceOrHostAddressConstKHR),
    ('dst', ctypes.c_void_p),
    ('mode', ctypes.c_int),
]
