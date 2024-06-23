import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('coverageToColorEnable', ctypes.c_uint32),
        ('coverageToColorLocation', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_COVERAGE_TO_COLOR_STATE_CREATE_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineCoverageToColorStateCreateFlagsNV'},
        'coverageToColorEnable': {'python_name': ['coverage', 'to', 'color', 'enable']},
        'coverageToColorLocation': {'python_name': ['coverage', 'to', 'color', 'location']},
    }
}
