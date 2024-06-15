import ctypes, sys

class VkPhysicalDeviceMaintenance5FeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maintenance5', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceMaintenance5FeaturesKHR
