import ctypes, sys

class VkAttachmentReference2(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('attachment', ctypes.c_uint32),
        ('layout', ctypes.c_int),
        ('aspectMask', ctypes.c_uint32),
    ]

sys.modules[__name__] = VkAttachmentReference2
