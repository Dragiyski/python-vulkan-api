import ctypes, sys

class VkDispatchGraphCountInfoAMDX(ctypes.Structure):
    pass

sys.modules[__name__] = VkDispatchGraphCountInfoAMDX

from . import VkDeviceOrHostAddressConstAMDX

VkDispatchGraphCountInfoAMDX._fields_ = [
    ('count', ctypes.c_uint32),
    ('infos', VkDeviceOrHostAddressConstAMDX),
    ('stride', ctypes.c_uint64),
]
