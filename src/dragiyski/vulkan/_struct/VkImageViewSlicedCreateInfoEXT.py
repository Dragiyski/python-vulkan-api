import ctypes, sys

class VkImageViewSlicedCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('sliceOffset', ctypes.c_uint32),
        ('sliceCount', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkImageViewSlicedCreateInfoEXT
