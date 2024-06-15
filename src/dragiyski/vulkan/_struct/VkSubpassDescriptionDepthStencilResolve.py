import ctypes, sys

class VkSubpassDescriptionDepthStencilResolve(ctypes.Structure):
    pass

sys.modules[__name__] = VkSubpassDescriptionDepthStencilResolve

from . import VkAttachmentReference2

VkSubpassDescriptionDepthStencilResolve._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('depthResolveMode', ctypes.c_uint32),
    ('stencilResolveMode', ctypes.c_uint32),
    ('pDepthStencilResolveAttachment', ctypes.POINTER(VkAttachmentReference2)),
]
