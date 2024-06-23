import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('storageBuffers', ctypes.c_int),
        ('uniformBuffers', ctypes.c_int),
        ('vertexInputs', ctypes.c_int),
        ('images', ctypes.c_int),
    ]

descriptor = {
    'extends': {
        'VkComputePipelineCreateInfo',
        'VkGraphicsPipelineCreateInfo',
        'VkPipelineShaderStageCreateInfo',
        'VkRayTracingPipelineCreateInfoKHR',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_ROBUSTNESS_CREATE_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'storageBuffers': {'python_name': ['storage', 'buffers'], 'type': 'VkPipelineRobustnessBufferBehaviorEXT'},
        'uniformBuffers': {'python_name': ['uniform', 'buffers'], 'type': 'VkPipelineRobustnessBufferBehaviorEXT'},
        'vertexInputs': {'python_name': ['vertex', 'inputs'], 'type': 'VkPipelineRobustnessBufferBehaviorEXT'},
        'images': {'python_name': ['images'], 'type': 'VkPipelineRobustnessImageBehaviorEXT'},
    }
}
