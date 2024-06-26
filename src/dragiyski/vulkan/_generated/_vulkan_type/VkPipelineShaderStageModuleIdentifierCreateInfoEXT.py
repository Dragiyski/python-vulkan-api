import ctypes

class VkPipelineShaderStageModuleIdentifierCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('identifierSize', ctypes.c_uint32),
        ('pIdentifier', ctypes.POINTER(ctypes.c_uint8)),
    ]

    _init_ = []
    _extends_ = {
        'VkPipelineShaderStageCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'identifierSize': 'identifier_size',
        'pIdentifier': 'identifier',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_shader_module_identifier',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_MODULE_IDENTIFIER_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_MODULE_IDENTIFIER_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineShaderStageModuleIdentifierCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'identifierSize': ctypes.c_uint32,
    'pIdentifier': ctypes.POINTER(ctypes.c_uint8),
}
