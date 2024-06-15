import ctypes, sys

class VkDispatchGraphInfoAMDX(ctypes.Structure):
    pass

sys.modules[__name__] = VkDispatchGraphInfoAMDX

from . import VkDeviceOrHostAddressConstAMDX

VkDispatchGraphInfoAMDX._fields_ = [
    ('nodeIndex', ctypes.c_uint32),
    ('payloadCount', ctypes.c_uint32),
    ('payloads', VkDeviceOrHostAddressConstAMDX),
    ('payloadStride', ctypes.c_uint64),
]
