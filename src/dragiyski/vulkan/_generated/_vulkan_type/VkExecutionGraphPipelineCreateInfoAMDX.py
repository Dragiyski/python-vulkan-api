import ctypes

class VkExecutionGraphPipelineCreateInfoAMDX(ctypes.Structure):
    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkPipelineCompilerControlCreateInfoAMD',
        'VkPipelineCreationFeedbackCreateInfo',
    }
    _includes_ = {
        'VkPipelineLibraryCreateInfoKHR',
        'VkPipelineShaderStageCreateInfo',
    }
    _included_in_ = set()
    _input_of_ = {
        'vkCreateExecutionGraphPipelinesAMDX',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'stageCount': 'stage_count',
        'pStages': 'stages',
        'pLibraryInfo': 'library_info',
        'layout': 'layout',
        'basePipelineHandle': 'base_pipeline_handle',
        'basePipelineIndex': 'base_pipeline_index',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_AMDX_shader_enqueue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkPipelineCreateFlags',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_EXECUTION_GRAPH_PIPELINE_CREATE_INFO_AMDX'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_EXECUTION_GRAPH_PIPELINE_CREATE_INFO_AMDX
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkPipelineLibraryCreateInfoKHR import VkPipelineLibraryCreateInfoKHR
from .VkPipelineShaderStageCreateInfo import VkPipelineShaderStageCreateInfo

VkExecutionGraphPipelineCreateInfoAMDX._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('stageCount', ctypes.c_uint32),
    ('pStages', ctypes.POINTER(VkPipelineShaderStageCreateInfo)),
    ('pLibraryInfo', ctypes.POINTER(VkPipelineLibraryCreateInfoKHR)),
    ('layout', ctypes.c_void_p),
    ('basePipelineHandle', ctypes.c_void_p),
    ('basePipelineIndex', ctypes.c_int32),
]

VkExecutionGraphPipelineCreateInfoAMDX._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'stageCount': ctypes.c_uint32,
    'pStages': ctypes.POINTER(VkPipelineShaderStageCreateInfo),
    'pLibraryInfo': ctypes.POINTER(VkPipelineLibraryCreateInfoKHR),
    'layout': ctypes.c_void_p,
    'basePipelineHandle': ctypes.c_void_p,
    'basePipelineIndex': ctypes.c_int32,
}
