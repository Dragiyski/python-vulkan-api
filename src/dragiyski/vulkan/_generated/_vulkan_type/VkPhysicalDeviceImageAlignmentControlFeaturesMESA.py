import ctypes, sys

class VkPhysicalDeviceImageAlignmentControlFeaturesMESA(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageAlignmentControl', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceImageAlignmentControlFeaturesMESA
