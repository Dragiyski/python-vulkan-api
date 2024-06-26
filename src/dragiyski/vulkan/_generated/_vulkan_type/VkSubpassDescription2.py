import ctypes

class VkSubpassDescription2(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkFragmentShadingRateAttachmentInfoKHR',
        'VkMultisampledRenderToSingleSampledInfoEXT',
        'VkRenderPassCreationControlEXT',
        'VkRenderPassSubpassFeedbackCreateInfoEXT',
        'VkSubpassDescriptionDepthStencilResolve',
    }
    _includes_ = {
        'VkAttachmentReference2',
    }
    _included_in_ = {
        'VkRenderPassCreateInfo2',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'pipelineBindPoint': 'pipeline_bind_point',
        'viewMask': 'view_mask',
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
        (1, 2),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkSubpassDescriptionFlags',
        'pipelineBindPoint': 'VkPipelineBindPoint',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SUBPASS_DESCRIPTION_2'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SUBPASS_DESCRIPTION_2
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkAttachmentReference2 import VkAttachmentReference2

VkSubpassDescription2._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('pipelineBindPoint', ctypes.c_int),
    ('viewMask', ctypes.c_uint32),
    ('inputAttachmentCount', ctypes.c_uint32),
    ('pInputAttachments', ctypes.POINTER(VkAttachmentReference2)),
    ('colorAttachmentCount', ctypes.c_uint32),
    ('pColorAttachments', ctypes.POINTER(VkAttachmentReference2)),
    ('pResolveAttachments', ctypes.POINTER(VkAttachmentReference2)),
    ('pDepthStencilAttachment', ctypes.POINTER(VkAttachmentReference2)),
    ('preserveAttachmentCount', ctypes.c_uint32),
    ('pPreserveAttachments', ctypes.POINTER(ctypes.c_uint32)),
]

VkSubpassDescription2._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'pipelineBindPoint': ctypes.c_int,
    'viewMask': ctypes.c_uint32,
    'inputAttachmentCount': ctypes.c_uint32,
    'pInputAttachments': ctypes.POINTER(VkAttachmentReference2),
    'colorAttachmentCount': ctypes.c_uint32,
    'pColorAttachments': ctypes.POINTER(VkAttachmentReference2),
    'pResolveAttachments': ctypes.POINTER(VkAttachmentReference2),
    'pDepthStencilAttachment': ctypes.POINTER(VkAttachmentReference2),
    'preserveAttachmentCount': ctypes.c_uint32,
    'pPreserveAttachments': ctypes.POINTER(ctypes.c_uint32),
}
