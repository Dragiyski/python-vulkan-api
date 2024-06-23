import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('stageFlags', ctypes.c_uint32),
        ('offset', ctypes.c_uint32),
        ('size', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkPipelineLayoutCreateInfo',
        'VkShaderCreateInfoEXT',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'stageFlags': {'python_name': ['stage', 'flags'], 'type': 'VkShaderStageFlags'},
        'offset': {'python_name': ['offset']},
        'size': {'python_name': ['size']},
    }
}
