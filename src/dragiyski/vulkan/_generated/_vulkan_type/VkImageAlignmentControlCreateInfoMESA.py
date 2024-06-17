import ctypes, sys

class VkImageAlignmentControlCreateInfoMESA(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maximumRequestedAlignment', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkImageAlignmentControlCreateInfoMESA
