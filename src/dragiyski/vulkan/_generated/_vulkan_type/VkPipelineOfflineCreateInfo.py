import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('pipelineIdentifier', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('matchControl', ctypes.c_int),
        ('poolEntrySize', ctypes.c_uint64),
    ]

descriptor = {
    'extends': {
        'VkComputePipelineCreateInfo',
        'VkGraphicsPipelineCreateInfo',
        'VkRayTracingPipelineCreateInfoKHR',
        'VkRayTracingPipelineCreateInfoNV',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_OFFLINE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'pipelineIdentifier': {'python_name': ['pipeline', 'identifier']},
        'matchControl': {'python_name': ['match', 'control'], 'type': 'VkPipelineMatchControl'},
        'poolEntrySize': {'python_name': ['pool', 'entry', 'size']},
    }
}
