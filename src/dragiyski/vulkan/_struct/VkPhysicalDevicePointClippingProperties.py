import ctypes, sys

class VkPhysicalDevicePointClippingProperties(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pointClippingBehavior', ctypes.c_int),
    ]

sys.modules[__name__] = VkPhysicalDevicePointClippingProperties
