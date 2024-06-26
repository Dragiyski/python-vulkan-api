import ctypes

class VkRenderingInputAttachmentIndexInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('colorAttachmentCount', ctypes.c_uint32),
        ('pColorAttachmentInputIndices', ctypes.POINTER(ctypes.c_uint32)),
        ('pDepthInputAttachmentIndex', ctypes.POINTER(ctypes.c_uint32)),
        ('pStencilInputAttachmentIndex', ctypes.POINTER(ctypes.c_uint32)),
    ]

    _init_ = []
    _extends_ = {
        'VkCommandBufferInheritanceInfo',
        'VkGraphicsPipelineCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCmdSetRenderingInputAttachmentIndicesKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'colorAttachmentCount': 'color_attachment_count',
        'pColorAttachmentInputIndices': 'color_attachment_input_indices',
        'pDepthInputAttachmentIndex': 'depth_input_attachment_index',
        'pStencilInputAttachmentIndex': 'stencil_input_attachment_index',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_dynamic_rendering_local_read',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_RENDERING_INPUT_ATTACHMENT_INDEX_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_RENDERING_INPUT_ATTACHMENT_INDEX_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkRenderingInputAttachmentIndexInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'colorAttachmentCount': ctypes.c_uint32,
    'pColorAttachmentInputIndices': ctypes.POINTER(ctypes.c_uint32),
    'pDepthInputAttachmentIndex': ctypes.POINTER(ctypes.c_uint32),
    'pStencilInputAttachmentIndex': ctypes.POINTER(ctypes.c_uint32),
}
