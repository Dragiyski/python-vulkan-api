import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('dynamicStateCount', ctypes.c_uint32),
        ('pDynamicStates', ctypes.POINTER(ctypes.c_int)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkGraphicsPipelineCreateInfo',
        'VkRayTracingPipelineCreateInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_DYNAMIC_STATE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineDynamicStateCreateFlags'},
        'dynamicStateCount': {'python_name': ['dynamic', 'state', 'count']},
        'pDynamicStates': {'python_name': ['p', 'dynamic', 'states'], 'len': [['dynamicStateCount']], 'type': 'VkDynamicState'},
    }
}
