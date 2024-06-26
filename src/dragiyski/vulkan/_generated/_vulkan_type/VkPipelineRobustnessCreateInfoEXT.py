import ctypes

class VkPipelineRobustnessCreateInfoEXT(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('storageBuffers', ctypes.c_int),
        ('uniformBuffers', ctypes.c_int),
        ('vertexInputs', ctypes.c_int),
        ('images', ctypes.c_int),
    ]

    _init_ = []
    _extends_ = {
        'VkComputePipelineCreateInfo',
        'VkGraphicsPipelineCreateInfo',
        'VkPipelineShaderStageCreateInfo',
        'VkRayTracingPipelineCreateInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'storageBuffers': 'storage_buffers',
        'uniformBuffers': 'uniform_buffers',
        'vertexInputs': 'vertex_inputs',
        'images': 'images',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_EXT_pipeline_robustness',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'storageBuffers': 'VkPipelineRobustnessBufferBehaviorEXT',
        'uniformBuffers': 'VkPipelineRobustnessBufferBehaviorEXT',
        'vertexInputs': 'VkPipelineRobustnessBufferBehaviorEXT',
        'images': 'VkPipelineRobustnessImageBehaviorEXT',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_PIPELINE_ROBUSTNESS_CREATE_INFO_EXT'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_PIPELINE_ROBUSTNESS_CREATE_INFO_EXT
        for function in self._init_:
            function(self, *args, **kwargs)

VkPipelineRobustnessCreateInfoEXT._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'storageBuffers': ctypes.c_int,
    'uniformBuffers': ctypes.c_int,
    'vertexInputs': ctypes.c_int,
    'images': ctypes.c_int,
}
