import ctypes

class VkAttachmentSampleCountInfoAMD(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('colorAttachmentCount', ctypes.c_uint32),
        ('pColorAttachmentSamples', ctypes.POINTER(ctypes.c_uint32)),
        ('depthStencilAttachmentSamples', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkCommandBufferInheritanceInfo',
        'VkGraphicsPipelineCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'colorAttachmentCount': 'color_attachment_count',
        'pColorAttachmentSamples': 'color_attachment_samples',
        'depthStencilAttachmentSamples': 'depth_stencil_attachment_samples',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_dynamic_rendering',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_ATTACHMENT_SAMPLE_COUNT_INFO_AMD'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_ATTACHMENT_SAMPLE_COUNT_INFO_AMD
        for function in self._init_:
            function(self, *args, **kwargs)

VkAttachmentSampleCountInfoAMD._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'colorAttachmentCount': ctypes.c_uint32,
    'pColorAttachmentSamples': ctypes.POINTER(ctypes.c_uint32),
    'depthStencilAttachmentSamples': ctypes.c_uint32,
}
