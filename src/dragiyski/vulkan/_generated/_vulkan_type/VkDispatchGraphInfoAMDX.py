import ctypes

class VkDispatchGraphInfoAMDX(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstAMDX import VkDeviceOrHostAddressConstAMDX

VkDispatchGraphInfoAMDX._fields_ = [
    ('nodeIndex', ctypes.c_uint32),
    ('payloadCount', ctypes.c_uint32),
    ('payloads', VkDeviceOrHostAddressConstAMDX),
    ('payloadStride', ctypes.c_uint64),
]

VkDispatchGraphInfoAMDX._type_ = {
    'nodeIndex': ctypes.c_uint32,
    'payloadCount': ctypes.c_uint32,
    'payloads': VkDeviceOrHostAddressConstAMDX,
    'payloadStride': ctypes.c_uint64,
}
