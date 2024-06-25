import ctypes

class VkDispatchGraphInfoAMDX(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'nodeIndex': ctypes.c_uint32,
            'payloadCount': ctypes.c_uint32,
            'payloads': VkDeviceOrHostAddressConstAMDX,
            'payloadStride': ctypes.c_uint64,
        }


from .VkDeviceOrHostAddressConstAMDX import VkDeviceOrHostAddressConstAMDX

VkDispatchGraphInfoAMDX._fields_ = [
    ('nodeIndex', ctypes.c_uint32),
    ('payloadCount', ctypes.c_uint32),
    ('payloads', VkDeviceOrHostAddressConstAMDX),
    ('payloadStride', ctypes.c_uint64),
]
