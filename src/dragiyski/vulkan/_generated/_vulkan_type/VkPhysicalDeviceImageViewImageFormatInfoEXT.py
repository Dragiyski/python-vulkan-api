import ctypes, sys

class VkPhysicalDeviceImageViewImageFormatInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageViewType', ctypes.c_int),
    ]

sys.modules[__name__] = VkPhysicalDeviceImageViewImageFormatInfoEXT
