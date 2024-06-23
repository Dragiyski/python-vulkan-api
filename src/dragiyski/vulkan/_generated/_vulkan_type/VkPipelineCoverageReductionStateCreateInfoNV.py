import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('coverageReductionMode', ctypes.c_int),
    ]

descriptor = {
    'extends': {
        'VkPipelineMultisampleStateCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_COVERAGE_REDUCTION_STATE_CREATE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineCoverageReductionStateCreateFlagsNV'},
        'coverageReductionMode': {'python_name': ['coverage', 'reduction', 'mode'], 'type': 'VkCoverageReductionModeNV'},
    }
}
