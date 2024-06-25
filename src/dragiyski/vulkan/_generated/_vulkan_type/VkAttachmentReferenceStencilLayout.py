import ctypes

class VkAttachmentReferenceStencilLayout(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stencilLayout', ctypes.c_int),
    ]

VkAttachmentReferenceStencilLayout._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stencilLayout': ctypes.c_int,
}
