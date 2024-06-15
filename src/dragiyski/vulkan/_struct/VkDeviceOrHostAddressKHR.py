import ctypes, sys

class VkDeviceOrHostAddressKHR(ctypes.Union):
    _fields_ = [
        ('deviceAddress', ctypes.c_uint64),
        ('hostAddress', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkDeviceOrHostAddressKHR
