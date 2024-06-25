import ctypes

class VkDispatchGraphCountInfoAMDX(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstAMDX import VkDeviceOrHostAddressConstAMDX

VkDispatchGraphCountInfoAMDX._fields_ = [
    ('count', ctypes.c_uint32),
    ('infos', VkDeviceOrHostAddressConstAMDX),
    ('stride', ctypes.c_uint64),
]

VkDispatchGraphCountInfoAMDX._type_ = {
    'count': ctypes.c_uint32,
    'infos': VkDeviceOrHostAddressConstAMDX,
    'stride': ctypes.c_uint64,
}
