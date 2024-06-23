import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('srcOffset', ctypes.c_uint64),
        ('dstOffset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdCopyBuffer',
    },
    'output_of': set(),
    'member_map': {
        'srcOffset': {'python_name': ['src', 'offset']},
        'dstOffset': {'python_name': ['dst', 'offset']},
        'size': {'python_name': ['size']},
    }
}
