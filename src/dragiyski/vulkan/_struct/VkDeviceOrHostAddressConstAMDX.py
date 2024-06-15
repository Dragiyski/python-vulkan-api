import ctypes, sys

class VkDeviceOrHostAddressConstAMDX(ctypes.Union):
    _fields_ = [
        ('deviceAddress', ctypes.c_uint64),
        ('hostAddress', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkDeviceOrHostAddressConstAMDX
