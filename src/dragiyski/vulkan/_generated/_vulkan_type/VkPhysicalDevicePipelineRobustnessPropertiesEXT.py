import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('defaultRobustnessStorageBuffers', ctypes.c_int),
        ('defaultRobustnessUniformBuffers', ctypes.c_int),
        ('defaultRobustnessVertexInputs', ctypes.c_int),
        ('defaultRobustnessImages', ctypes.c_int),
    ]

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_PIPELINE_ROBUSTNESS_PROPERTIES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'defaultRobustnessStorageBuffers': {'python_name': ['default', 'robustness', 'storage', 'buffers'], 'type': 'VkPipelineRobustnessBufferBehaviorEXT'},
        'defaultRobustnessUniformBuffers': {'python_name': ['default', 'robustness', 'uniform', 'buffers'], 'type': 'VkPipelineRobustnessBufferBehaviorEXT'},
        'defaultRobustnessVertexInputs': {'python_name': ['default', 'robustness', 'vertex', 'inputs'], 'type': 'VkPipelineRobustnessBufferBehaviorEXT'},
        'defaultRobustnessImages': {'python_name': ['default', 'robustness', 'images'], 'type': 'VkPipelineRobustnessImageBehaviorEXT'},
    }
}
