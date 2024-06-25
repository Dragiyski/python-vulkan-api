import ctypes

class VkSubpassDescriptionDepthStencilResolve(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'depthResolveMode': ctypes.c_uint32,
            'stencilResolveMode': ctypes.c_uint32,
            'pDepthStencilResolveAttachment': ctypes.POINTER(VkAttachmentReference2),
        }


from .VkAttachmentReference2 import VkAttachmentReference2

VkSubpassDescriptionDepthStencilResolve._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('depthResolveMode', ctypes.c_uint32),
    ('stencilResolveMode', ctypes.c_uint32),
    ('pDepthStencilResolveAttachment', ctypes.POINTER(VkAttachmentReference2)),
]
