import ctypes

class VkDeviceOrHostAddressConstAMDX(ctypes.Union):
    _fields_ = [
        ('deviceAddress', ctypes.c_uint64),
        ('hostAddress', ctypes.c_void_p),
    ]

VkDeviceOrHostAddressConstAMDX._type_ = {
    'deviceAddress': ctypes.c_uint64,
    'hostAddress': ctypes.c_void_p,
}
