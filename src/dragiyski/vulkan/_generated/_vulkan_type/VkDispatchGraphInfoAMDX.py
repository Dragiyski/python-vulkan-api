import ctypes

class CType(ctypes.Structure):
    pass

from .VkDeviceOrHostAddressConstAMDX import CType as VkDeviceOrHostAddressConstAMDX

CType._fields_ = [
    ('nodeIndex', ctypes.c_uint32),
    ('payloadCount', ctypes.c_uint32),
    ('payloads', VkDeviceOrHostAddressConstAMDX),
    ('payloadStride', ctypes.c_uint64),
]
