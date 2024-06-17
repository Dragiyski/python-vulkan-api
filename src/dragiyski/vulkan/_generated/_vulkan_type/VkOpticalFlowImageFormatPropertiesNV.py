import ctypes, sys

class VkOpticalFlowImageFormatPropertiesNV(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('format', ctypes.c_int),
    ]

sys.modules[__name__] = VkOpticalFlowImageFormatPropertiesNV
