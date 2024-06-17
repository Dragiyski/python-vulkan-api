import ctypes, sys

class VkPhysicalDeviceLayeredDriverPropertiesMSFT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('underlyingAPI', ctypes.c_int),
    ]

sys.modules[__name__] = VkPhysicalDeviceLayeredDriverPropertiesMSFT
