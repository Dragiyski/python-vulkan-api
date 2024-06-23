import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('pixelX', ctypes.c_uint32),
        ('pixelY', ctypes.c_uint32),
        ('sample', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkCoarseSampleOrderCustomNV',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'pixelX': {'python_name': ['pixel', 'x']},
        'pixelY': {'python_name': ['pixel', 'y']},
        'sample': {'python_name': ['sample']},
    }
}
