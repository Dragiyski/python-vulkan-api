import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('compilerControlFlags', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkComputePipelineCreateInfo',
        'VkExecutionGraphPipelineCreateInfoAMDX',
        'VkGraphicsPipelineCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_COMPILER_CONTROL_CREATE_INFO_AMD', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'compilerControlFlags': {'python_name': ['compiler', 'control', 'flags'], 'type': 'VkPipelineCompilerControlFlagsAMD'},
    }
}
