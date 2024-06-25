import ctypes

class VkSubpassDescription(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'flags': ctypes.c_uint32,
            'pipelineBindPoint': ctypes.c_int,
            'inputAttachmentCount': ctypes.c_uint32,
            'pInputAttachments': ctypes.POINTER(VkAttachmentReference),
            'colorAttachmentCount': ctypes.c_uint32,
            'pColorAttachments': ctypes.POINTER(VkAttachmentReference),
            'pResolveAttachments': ctypes.POINTER(VkAttachmentReference),
            'pDepthStencilAttachment': ctypes.POINTER(VkAttachmentReference),
            'preserveAttachmentCount': ctypes.c_uint32,
            'pPreserveAttachments': ctypes.POINTER(ctypes.c_uint32),
        }


from .VkAttachmentReference import VkAttachmentReference

VkSubpassDescription._fields_ = [
    ('flags', ctypes.c_uint32),
    ('pipelineBindPoint', ctypes.c_int),
    ('inputAttachmentCount', ctypes.c_uint32),
    ('pInputAttachments', ctypes.POINTER(VkAttachmentReference)),
    ('colorAttachmentCount', ctypes.c_uint32),
    ('pColorAttachments', ctypes.POINTER(VkAttachmentReference)),
    ('pResolveAttachments', ctypes.POINTER(VkAttachmentReference)),
    ('pDepthStencilAttachment', ctypes.POINTER(VkAttachmentReference)),
    ('preserveAttachmentCount', ctypes.c_uint32),
    ('pPreserveAttachments', ctypes.POINTER(ctypes.c_uint32)),
]
