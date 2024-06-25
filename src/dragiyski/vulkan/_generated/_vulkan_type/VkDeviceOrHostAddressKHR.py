import ctypes

class VkDeviceOrHostAddressKHR(ctypes.Union):
    _fields_ = [
        ('deviceAddress', ctypes.c_uint64),
        ('hostAddress', ctypes.c_void_p),
    ]

VkDeviceOrHostAddressKHR._type_ = {
    'deviceAddress': ctypes.c_uint64,
    'hostAddress': ctypes.c_void_p,
}
