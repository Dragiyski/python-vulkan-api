import ctypes

class CType(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstAMDX import CType as VkDeviceOrHostAddressConstAMDX

CType._fields_ = [
    ('count', ctypes.c_uint32),
    ('infos', VkDeviceOrHostAddressConstAMDX),
    ('stride', ctypes.c_uint64),
]
