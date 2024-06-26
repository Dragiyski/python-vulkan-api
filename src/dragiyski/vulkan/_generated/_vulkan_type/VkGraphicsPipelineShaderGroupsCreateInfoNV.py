import ctypes

class VkGraphicsPipelineShaderGroupsCreateInfoNV(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkGraphicsPipelineCreateInfo',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkGraphicsShaderGroupCreateInfoNV',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'groupCount': 'group_count',
        'pGroups': 'groups',
        'pipelineCount': 'pipeline_count',
        'pPipelines': 'pipelines',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_NV_device_generated_commands',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_GRAPHICS_PIPELINE_SHADER_GROUPS_CREATE_INFO_NV'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_GRAPHICS_PIPELINE_SHADER_GROUPS_CREATE_INFO_NV
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkGraphicsShaderGroupCreateInfoNV import VkGraphicsShaderGroupCreateInfoNV

VkGraphicsPipelineShaderGroupsCreateInfoNV._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('groupCount', ctypes.c_uint32),
    ('pGroups', ctypes.POINTER(VkGraphicsShaderGroupCreateInfoNV)),
    ('pipelineCount', ctypes.c_uint32),
    ('pPipelines', ctypes.POINTER(ctypes.c_void_p)),
]

VkGraphicsPipelineShaderGroupsCreateInfoNV._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'groupCount': ctypes.c_uint32,
    'pGroups': ctypes.POINTER(VkGraphicsShaderGroupCreateInfoNV),
    'pipelineCount': ctypes.c_uint32,
    'pPipelines': ctypes.POINTER(ctypes.c_void_p),
}
