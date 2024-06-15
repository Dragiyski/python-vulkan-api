import ctypes, sys

class VkPhysicalDeviceDescriptorPoolOverallocationFeaturesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorPoolOverallocation', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceDescriptorPoolOverallocationFeaturesNV
