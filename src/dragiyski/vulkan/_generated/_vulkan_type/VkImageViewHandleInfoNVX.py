import ctypes, sys

class VkImageViewHandleInfoNVX(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('imageView', ctypes.c_void_p),
        ('descriptorType', ctypes.c_int),
        ('sampler', ctypes.c_void_p),
    ]

sys.modules[__name__] = VkImageViewHandleInfoNVX
