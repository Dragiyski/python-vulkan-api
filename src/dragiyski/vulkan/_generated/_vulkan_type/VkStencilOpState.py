import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('failOp', ctypes.c_int),
        ('passOp', ctypes.c_int),
        ('depthFailOp', ctypes.c_int),
        ('compareOp', ctypes.c_int),
        ('compareMask', ctypes.c_uint32),
        ('writeMask', ctypes.c_uint32),
        ('reference', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkPipelineDepthStencilStateCreateInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'failOp': {'python_name': ['fail', 'op'], 'type': 'VkStencilOp'},
        'passOp': {'python_name': ['pass', 'op'], 'type': 'VkStencilOp'},
        'depthFailOp': {'python_name': ['depth', 'fail', 'op'], 'type': 'VkStencilOp'},
        'compareOp': {'python_name': ['compare', 'op'], 'type': 'VkCompareOp'},
        'compareMask': {'python_name': ['compare', 'mask']},
        'writeMask': {'python_name': ['write', 'mask']},
        'reference': {'python_name': ['reference']},
    }
}
