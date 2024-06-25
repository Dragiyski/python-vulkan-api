import ctypes

class VkDeviceOrHostAddressConstKHR(ctypes.Union):
    _fields_ = [
        ('deviceAddress', ctypes.c_uint64),
        ('hostAddress', ctypes.c_void_p),
    ]

VkDeviceOrHostAddressConstKHR._type_ = {
    'deviceAddress': ctypes.c_uint64,
    'hostAddress': ctypes.c_void_p,
}
