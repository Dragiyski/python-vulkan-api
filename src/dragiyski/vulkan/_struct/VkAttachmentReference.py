import ctypes, sys

class VkAttachmentReference(ctypes.Structure):
    _fields_ = [
        ('attachment', ctypes.c_uint32),
        ('layout', ctypes.c_int),
    ]

sys.modules[__name__] = VkAttachmentReference
