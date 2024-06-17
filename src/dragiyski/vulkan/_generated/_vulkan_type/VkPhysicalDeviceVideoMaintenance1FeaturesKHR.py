import ctypes, sys

class VkPhysicalDeviceVideoMaintenance1FeaturesKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('videoMaintenance1', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceVideoMaintenance1FeaturesKHR
