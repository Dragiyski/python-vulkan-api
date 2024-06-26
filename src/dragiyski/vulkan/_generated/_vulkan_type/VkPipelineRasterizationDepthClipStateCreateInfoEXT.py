import ctypes

class VkPipelineRasterizationDepthClipStateCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('depthClipEnable', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkPipelineRasterizationStateCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'depthClipEnable': 'depth_clip_enable',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_depth_clip_enable',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkPipelineRasterizationDepthClipStateCreateFlagsEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_DEPTH_CLIP_STATE_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_DEPTH_CLIP_STATE_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineRasterizationDepthClipStateCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'depthClipEnable': ctypes.c_uint32,
}
