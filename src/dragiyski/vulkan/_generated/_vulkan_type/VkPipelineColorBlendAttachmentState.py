import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('blendEnable', ctypes.c_uint32),
        ('srcColorBlendFactor', ctypes.c_int),
        ('dstColorBlendFactor', ctypes.c_int),
        ('colorBlendOp', ctypes.c_int),
        ('srcAlphaBlendFactor', ctypes.c_int),
        ('dstAlphaBlendFactor', ctypes.c_int),
        ('alphaBlendOp', ctypes.c_int),
        ('colorWriteMask', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkPipelineColorBlendStateCreateInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'blendEnable': {'python_name': ['blend', 'enable']},
        'srcColorBlendFactor': {'python_name': ['src', 'color', 'blend', 'factor'], 'type': 'VkBlendFactor'},
        'dstColorBlendFactor': {'python_name': ['dst', 'color', 'blend', 'factor'], 'type': 'VkBlendFactor'},
        'colorBlendOp': {'python_name': ['color', 'blend', 'op'], 'type': 'VkBlendOp'},
        'srcAlphaBlendFactor': {'python_name': ['src', 'alpha', 'blend', 'factor'], 'type': 'VkBlendFactor'},
        'dstAlphaBlendFactor': {'python_name': ['dst', 'alpha', 'blend', 'factor'], 'type': 'VkBlendFactor'},
        'alphaBlendOp': {'python_name': ['alpha', 'blend', 'op'], 'type': 'VkBlendOp'},
        'colorWriteMask': {'python_name': ['color', 'write', 'mask'], 'type': 'VkColorComponentFlags'},
    }
}
