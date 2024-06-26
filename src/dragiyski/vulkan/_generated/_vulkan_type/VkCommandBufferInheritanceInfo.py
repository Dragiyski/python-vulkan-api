import ctypes

class VkCommandBufferInheritanceInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('renderPass', ctypes.c_void_p),
        ('subpass', ctypes.c_uint32),
        ('framebuffer', ctypes.c_void_p),
        ('occlusionQueryEnable', ctypes.c_uint32),
        ('queryFlags', ctypes.c_uint32),
        ('pipelineStatistics', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkAttachmentSampleCountInfoAMD',
        'VkCommandBufferInheritanceConditionalRenderingInfoEXT',
        'VkCommandBufferInheritanceRenderPassTransformInfoQCOM',
        'VkCommandBufferInheritanceRenderingInfo',
        'VkCommandBufferInheritanceViewportScissorInfoNV',
        'VkExternalFormatANDROID',
        'VkMultiviewPerViewAttributesInfoNVX',
        'VkRenderingAttachmentLocationInfoKHR',
        'VkRenderingInputAttachmentIndexInfoKHR',
    }
    _includes_ = set()
    _included_in_ = {
        'VkCommandBufferBeginInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'renderPass': 'render_pass',
        'subpass': 'subpass',
        'framebuffer': 'framebuffer',
        'occlusionQueryEnable': 'occlusion_query_enable',
        'queryFlags': 'query_flags',
        'pipelineStatistics': 'pipeline_statistics',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'queryFlags': 'VkQueryControlFlags',
        'pipelineStatistics': 'VkQueryPipelineStatisticFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_COMMAND_BUFFER_INHERITANCE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkCommandBufferInheritanceInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'renderPass': ctypes.c_void_p,
    'subpass': ctypes.c_uint32,
    'framebuffer': ctypes.c_void_p,
    'occlusionQueryEnable': ctypes.c_uint32,
    'queryFlags': ctypes.c_uint32,
    'pipelineStatistics': ctypes.c_uint32,
}
