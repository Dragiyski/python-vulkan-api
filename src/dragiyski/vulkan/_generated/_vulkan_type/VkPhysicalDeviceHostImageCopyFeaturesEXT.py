import ctypes, sys

class VkPhysicalDeviceHostImageCopyFeaturesEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('hostImageCopy', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkPhysicalDeviceHostImageCopyFeaturesEXT
