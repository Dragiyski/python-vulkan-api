import ctypes

class VkDepthBiasRepresentationInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('depthBiasRepresentation', ctypes.c_int),
        ('depthBiasExact', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkDepthBiasInfoEXT',
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
        'depthBiasRepresentation': 'depth_bias_representation',
        'depthBiasExact': 'depth_bias_exact',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_depth_bias_control',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'depthBiasRepresentation': 'VkDepthBiasRepresentationEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_DEPTH_BIAS_REPRESENTATION_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_DEPTH_BIAS_REPRESENTATION_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkDepthBiasRepresentationInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'depthBiasRepresentation': ctypes.c_int,
    'depthBiasExact': ctypes.c_uint32,
}
