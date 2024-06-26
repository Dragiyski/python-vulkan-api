import ctypes

class VkShaderCreateInfoEXT(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkPipelineShaderStageRequiredSubgroupSizeCreateInfo',
        'VkValidationFeaturesEXT',
    }
    _includes_ = {
        'VkPushConstantRange',
        'VkSpecializationInfo',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCreateShadersEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'stage': 'stage',
        'nextStage': 'next_stage',
        'codeType': 'code_type',
        'codeSize': 'code_size',
        'pCode': 'code',
        'pName': 'name',
        'setLayoutCount': 'set_layout_count',
        'pSetLayouts': 'set_layouts',
        'pushConstantRangeCount': 'push_constant_range_count',
        'pPushConstantRanges': 'push_constant_ranges',
        'pSpecializationInfo': 'specialization_info',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_shader_object',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkShaderCreateFlagsEXT',
        'nextStage': 'VkShaderStageFlags',
        'codeType': 'VkShaderCodeTypeEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SHADER_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SHADER_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkPushConstantRange import VkPushConstantRange
from .VkSpecializationInfo import VkSpecializationInfo

VkShaderCreateInfoEXT._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('stage', ctypes.c_uint32),
    ('nextStage', ctypes.c_uint32),
    ('codeType', ctypes.c_int),
    ('codeSize', ctypes.c_size_t),
    ('pCode', ctypes.c_void_p),
    ('pName', ctypes.c_char_p),
    ('setLayoutCount', ctypes.c_uint32),
    ('pSetLayouts', ctypes.POINTER(ctypes.c_void_p)),
    ('pushConstantRangeCount', ctypes.c_uint32),
    ('pPushConstantRanges', ctypes.POINTER(VkPushConstantRange)),
    ('pSpecializationInfo', ctypes.POINTER(VkSpecializationInfo)),
]

VkShaderCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'stage': ctypes.c_uint32,
    'nextStage': ctypes.c_uint32,
    'codeType': ctypes.c_int,
    'codeSize': ctypes.c_size_t,
    'pCode': ctypes.c_void_p,
    'pName': ctypes.c_char_p,
    'setLayoutCount': ctypes.c_uint32,
    'pSetLayouts': ctypes.POINTER(ctypes.c_void_p),
    'pushConstantRangeCount': ctypes.c_uint32,
    'pPushConstantRanges': ctypes.POINTER(VkPushConstantRange),
    'pSpecializationInfo': ctypes.POINTER(VkSpecializationInfo),
}
