import ctypes

class VkDispatchGraphCountInfoAMDX(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'count': ctypes.c_uint32,
            'infos': VkDeviceOrHostAddressConstAMDX,
            'stride': ctypes.c_uint64,
        }


from .VkDeviceOrHostAddressConstAMDX import VkDeviceOrHostAddressConstAMDX

VkDispatchGraphCountInfoAMDX._fields_ = [
    ('count', ctypes.c_uint32),
    ('infos', VkDeviceOrHostAddressConstAMDX),
    ('stride', ctypes.c_uint64),
]
