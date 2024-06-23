import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('rasterizationSamples', ctypes.c_uint32),
        ('sampleShadingEnable', ctypes.c_uint32),
        ('minSampleShading', ctypes.c_float),
        ('pSampleMask', ctypes.POINTER(ctypes.c_uint32)),
        ('alphaToCoverageEnable', ctypes.c_uint32),
        ('alphaToOneEnable', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkPipelineCoverageModulationStateCreateInfoNV',
        'VkPipelineCoverageReductionStateCreateInfoNV',
        'VkPipelineCoverageToColorStateCreateInfoNV',
        'VkPipelineSampleLocationsStateCreateInfoEXT',
    },
    'includes': set(),
    'included_in': {
        'VkGraphicsPipelineCreateInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_MULTISAMPLE_STATE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineMultisampleStateCreateFlags'},
        'rasterizationSamples': {'python_name': ['rasterization', 'samples'], 'type': 'VkSampleCountFlagBits'},
        'sampleShadingEnable': {'python_name': ['sample', 'shading', 'enable']},
        'minSampleShading': {'python_name': ['min', 'sample', 'shading']},
        'pSampleMask': {'python_name': ['p', 'sample', 'mask'], 'len': [['latexmath:[\\lceil{\\mathit{rasterizationSamples} \\over 32}\\rceil]']]},
        'alphaToCoverageEnable': {'python_name': ['alpha', 'to', 'coverage', 'enable']},
        'alphaToOneEnable': {'python_name': ['alpha', 'to', 'one', 'enable']},
    }
}
