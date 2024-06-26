import ctypes

class VkPipelineRasterizationStateCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('depthClampEnable', ctypes.c_uint32),
        ('rasterizerDiscardEnable', ctypes.c_uint32),
        ('polygonMode', ctypes.c_int),
        ('cullMode', ctypes.c_uint32),
        ('frontFace', ctypes.c_int),
        ('depthBiasEnable', ctypes.c_uint32),
        ('depthBiasConstantFactor', ctypes.c_float),
        ('depthBiasClamp', ctypes.c_float),
        ('depthBiasSlopeFactor', ctypes.c_float),
        ('lineWidth', ctypes.c_float),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkDepthBiasRepresentationInfoEXT',
        'VkPipelineRasterizationConservativeStateCreateInfoEXT',
        'VkPipelineRasterizationDepthClipStateCreateInfoEXT',
        'VkPipelineRasterizationLineStateCreateInfoKHR',
        'VkPipelineRasterizationProvokingVertexStateCreateInfoEXT',
        'VkPipelineRasterizationStateRasterizationOrderAMD',
        'VkPipelineRasterizationStateStreamCreateInfoEXT',
    }
    _includes_ = set()
    _included_in_ = {
        'VkGraphicsPipelineCreateInfo',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'depthClampEnable': 'depth_clamp_enable',
        'rasterizerDiscardEnable': 'rasterizer_discard_enable',
        'polygonMode': 'polygon_mode',
        'cullMode': 'cull_mode',
        'frontFace': 'front_face',
        'depthBiasEnable': 'depth_bias_enable',
        'depthBiasConstantFactor': 'depth_bias_constant_factor',
        'depthBiasClamp': 'depth_bias_clamp',
        'depthBiasSlopeFactor': 'depth_bias_slope_factor',
        'lineWidth': 'line_width',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkPipelineRasterizationStateCreateFlags',
        'polygonMode': 'VkPolygonMode',
        'cullMode': 'VkCullModeFlags',
        'frontFace': 'VkFrontFace',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_STATE_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_RASTERIZATION_STATE_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineRasterizationStateCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'depthClampEnable': ctypes.c_uint32,
    'rasterizerDiscardEnable': ctypes.c_uint32,
    'polygonMode': ctypes.c_int,
    'cullMode': ctypes.c_uint32,
    'frontFace': ctypes.c_int,
    'depthBiasEnable': ctypes.c_uint32,
    'depthBiasConstantFactor': ctypes.c_float,
    'depthBiasClamp': ctypes.c_float,
    'depthBiasSlopeFactor': ctypes.c_float,
    'lineWidth': ctypes.c_float,
}
