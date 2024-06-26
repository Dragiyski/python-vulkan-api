import ctypes

class VkDepthBiasInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('depthBiasConstantFactor', ctypes.c_float),
        ('depthBiasClamp', ctypes.c_float),
        ('depthBiasSlopeFactor', ctypes.c_float),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkDepthBiasRepresentationInfoEXT',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCmdSetDepthBias2EXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'depthBiasConstantFactor': 'depth_bias_constant_factor',
        'depthBiasClamp': 'depth_bias_clamp',
        'depthBiasSlopeFactor': 'depth_bias_slope_factor',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_depth_bias_control',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEPTH_BIAS_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEPTH_BIAS_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkDepthBiasInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'depthBiasConstantFactor': ctypes.c_float,
    'depthBiasClamp': ctypes.c_float,
    'depthBiasSlopeFactor': ctypes.c_float,
}
