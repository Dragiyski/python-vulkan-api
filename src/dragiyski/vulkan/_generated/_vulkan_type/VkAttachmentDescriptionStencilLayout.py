import ctypes

class VkAttachmentDescriptionStencilLayout(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stencilInitialLayout', ctypes.c_int),
        ('stencilFinalLayout', ctypes.c_int),
    ]

VkAttachmentDescriptionStencilLayout._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stencilInitialLayout': ctypes.c_int,
    'stencilFinalLayout': ctypes.c_int,
}
