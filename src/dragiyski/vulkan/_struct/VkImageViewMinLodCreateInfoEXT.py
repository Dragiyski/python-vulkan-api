import ctypes, sys

class VkImageViewMinLodCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('minLod', ctypes.c_float),
    ]

sys.modules[__name__] = VkImageViewMinLodCreateInfoEXT
