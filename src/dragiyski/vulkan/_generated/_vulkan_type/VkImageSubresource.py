import ctypes, sys

class VkImageSubresource(ctypes.Structure):
    _fields_ = [
        ('aspectMask', ctypes.c_uint32),
        ('mipLevel', ctypes.c_uint32),
        ('arrayLayer', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkImageSubresource
