import ctypes

class CType(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressKHR import CType as VkDeviceOrHostAddressKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('src', ctypes.c_void_p),
    ('dst', VkDeviceOrHostAddressKHR),
    ('mode', ctypes.c_int),
]
