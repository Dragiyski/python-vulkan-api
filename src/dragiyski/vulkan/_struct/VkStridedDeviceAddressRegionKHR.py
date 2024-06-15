import ctypes, sys

class VkStridedDeviceAddressRegionKHR(ctypes.Structure):
    _fields_ = [
        ('deviceAddress', ctypes.c_uint64),
        ('stride', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]

sys.modules[__name__] = VkStridedDeviceAddressRegionKHR
