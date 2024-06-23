import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('patchControlPoints', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkPipelineTessellationDomainOriginStateCreateInfo',
    },
    'includes': set(),
    'included_in': {
        'VkGraphicsPipelineCreateInfo',
        'VkGraphicsShaderGroupCreateInfoNV',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_TESSELLATION_STATE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineTessellationStateCreateFlags'},
        'patchControlPoints': {'python_name': ['patch', 'control', 'points']},
    }
}
