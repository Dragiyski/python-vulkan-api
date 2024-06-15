import ctypes, sys

class VkDeviceMemoryOpaqueCaptureAddressInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memory', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkDeviceMemoryOpaqueCaptureAddressInfo
