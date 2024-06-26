import ctypes

class VkSubpassDescription(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = set()
    _includes_ = {
        'VkAttachmentReference',
    }
    _included_in_ = {
        'VkRenderPassCreateInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'flags': 'flags',
        'pipelineBindPoint': 'pipeline_bind_point',
        'inputAttachmentCount': 'input_attachment_count',
        'pInputAttachments': 'input_attachments',
        'colorAttachmentCount': 'color_attachment_count',
        'pColorAttachments': 'color_attachments',
        'pResolveAttachments': 'resolve_attachments',
        'pDepthStencilAttachment': 'depth_stencil_attachment',
        'preserveAttachmentCount': 'preserve_attachment_count',
        'pPreserveAttachments': 'preserve_attachments',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'flags': 'VkSubpassDescriptionFlags',
        'pipelineBindPoint': 'VkPipelineBindPoint',
    }

    def __init__(self, *args, **kwargs):
        super().__init__()
        for function in self._init_:
            function(self, *args, **kwargs)


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

VkSubpassDescription._type_ = {
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
