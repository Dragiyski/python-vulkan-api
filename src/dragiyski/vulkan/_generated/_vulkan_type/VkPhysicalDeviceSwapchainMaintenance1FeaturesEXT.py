import ctypes, sys

class VkPhysicalDeviceSwapchainMaintenance1FeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('swapchainMaintenance1', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceSwapchainMaintenance1FeaturesEXT
