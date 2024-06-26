import ctypes

class VkPipelineShaderStageNodeCreateInfoAMDX(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pName', ctypes.c_char_p),
        ('index', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkPipelineShaderStageCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkGetExecutionGraphPipelineNodeIndexAMDX',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pName': 'name',
        'index': 'index',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_AMDX_shader_enqueue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_NODE_CREATE_INFO_AMDX'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_NODE_CREATE_INFO_AMDX
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineShaderStageNodeCreateInfoAMDX._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pName': ctypes.c_char_p,
    'index': ctypes.c_uint32,
}
