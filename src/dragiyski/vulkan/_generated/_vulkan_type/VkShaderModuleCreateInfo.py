import ctypes

class VkShaderModuleCreateInfo(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('codeSize', ctypes.c_size_t),
        ('pCode', ctypes.POINTER(ctypes.c_uint32)),
    ]

    _init_ = []
    _extends_ = {
        'VkPipelineShaderStageCreateInfo',
    }
    _extended_by_ = {
        'VkShaderModuleValidationCacheCreateInfoEXT',
        'VkValidationFeaturesEXT',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCreateShaderModule',
        'vkGetShaderModuleCreateInfoIdentifierEXT',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'codeSize': 'code_size',
        'pCode': 'code',
    }
    _vk_versions_ = {
        (1, 0),
    }
    _vk_extensions_ = set()
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkShaderModuleCreateFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_SHADER_MODULE_CREATE_INFO'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_SHADER_MODULE_CREATE_INFO
        for function in self._init_:
            function(self, *args, **kwargs)

VkShaderModuleCreateInfo._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'codeSize': ctypes.c_size_t,
    'pCode': ctypes.POINTER(ctypes.c_uint32),
}
