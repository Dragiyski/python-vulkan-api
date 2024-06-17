import ctypes, sys

class VkAttachmentReferenceStencilLayout(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stencilLayout', ctypes.c_int),
    ]

sys.modules[__name__] = VkAttachmentReferenceStencilLayout
