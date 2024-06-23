import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('depth', ctypes.c_float),
        ('stencil', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkClearValue',
    },
    'input_of': {
        'vkCmdClearDepthStencilImage',
    },
    'output_of': set(),
    'member_map': {
        'depth': {'python_name': ['depth']},
        'stencil': {'python_name': ['stencil']},
    }
}
