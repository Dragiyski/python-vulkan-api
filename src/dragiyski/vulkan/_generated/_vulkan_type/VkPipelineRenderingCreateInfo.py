import ctypes

class VkPipelineRenderingCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('viewMask', ctypes.c_uint32),
        ('colorAttachmentCount', ctypes.c_uint32),
        ('pColorAttachmentFormats', ctypes.POINTER(ctypes.c_int)),
        ('depthAttachmentFormat', ctypes.c_int),
        ('stencilAttachmentFormat', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = {
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
        'viewMask': 'view_mask',
        'colorAttachmentCount': 'color_attachment_count',
        'pColorAttachmentFormats': 'color_attachment_formats',
        'depthAttachmentFormat': 'depth_attachment_format',
        'stencilAttachmentFormat': 'stencil_attachment_format',
    }
    _vk_versions_ = {
        (1, 3),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'pColorAttachmentFormats': 'VkFormat',
        'depthAttachmentFormat': 'VkFormat',
        'stencilAttachmentFormat': 'VkFormat',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_RENDERING_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_RENDERING_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineRenderingCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'viewMask': ctypes.c_uint32,
    'colorAttachmentCount': ctypes.c_uint32,
    'pColorAttachmentFormats': ctypes.POINTER(ctypes.c_int),
    'depthAttachmentFormat': ctypes.c_int,
    'stencilAttachmentFormat': ctypes.c_int,
}
