import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('srcColorBlendFactor', ctypes.c_int),
        ('dstColorBlendFactor', ctypes.c_int),
        ('colorBlendOp', ctypes.c_int),
        ('srcAlphaBlendFactor', ctypes.c_int),
        ('dstAlphaBlendFactor', ctypes.c_int),
        ('alphaBlendOp', ctypes.c_int),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdSetColorBlendEquationEXT',
    },
    'output_of': set(),
    'member_map': {
        'srcColorBlendFactor': {'python_name': ['src', 'color', 'blend', 'factor'], 'type': 'VkBlendFactor'},
        'dstColorBlendFactor': {'python_name': ['dst', 'color', 'blend', 'factor'], 'type': 'VkBlendFactor'},
        'colorBlendOp': {'python_name': ['color', 'blend', 'op'], 'type': 'VkBlendOp'},
        'srcAlphaBlendFactor': {'python_name': ['src', 'alpha', 'blend', 'factor'], 'type': 'VkBlendFactor'},
        'dstAlphaBlendFactor': {'python_name': ['dst', 'alpha', 'blend', 'factor'], 'type': 'VkBlendFactor'},
        'alphaBlendOp': {'python_name': ['alpha', 'blend', 'op'], 'type': 'VkBlendOp'},
    }
}
