import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_float),
        ('y', ctypes.c_float),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkHdrMetadataEXT',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'x': {'python_name': ['x']},
        'y': {'python_name': ['y']},
    }
}
