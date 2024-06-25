import ctypes

class VkRenderingInfo(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'flags': ctypes.c_uint32,
            'renderArea': VkRect2D,
            'layerCount': ctypes.c_uint32,
            'viewMask': ctypes.c_uint32,
            'colorAttachmentCount': ctypes.c_uint32,
            'pColorAttachments': ctypes.POINTER(VkRenderingAttachmentInfo),
            'pDepthAttachment': ctypes.POINTER(VkRenderingAttachmentInfo),
            'pStencilAttachment': ctypes.POINTER(VkRenderingAttachmentInfo),
        }


from .VkRect2D import VkRect2D
from .VkRenderingAttachmentInfo import VkRenderingAttachmentInfo

VkRenderingInfo._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('renderArea', VkRect2D),
    ('layerCount', ctypes.c_uint32),
    ('viewMask', ctypes.c_uint32),
    ('colorAttachmentCount', ctypes.c_uint32),
    ('pColorAttachments', ctypes.POINTER(VkRenderingAttachmentInfo)),
    ('pDepthAttachment', ctypes.POINTER(VkRenderingAttachmentInfo)),
    ('pStencilAttachment', ctypes.POINTER(VkRenderingAttachmentInfo)),
]
