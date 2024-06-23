import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('minX', ctypes.c_float),
        ('minY', ctypes.c_float),
        ('minZ', ctypes.c_float),
        ('maxX', ctypes.c_float),
        ('maxY', ctypes.c_float),
        ('maxZ', ctypes.c_float),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'minX': {'python_name': ['min', 'x']},
        'minY': {'python_name': ['min', 'y']},
        'minZ': {'python_name': ['min', 'z']},
        'maxX': {'python_name': ['max', 'x']},
        'maxY': {'python_name': ['max', 'y']},
        'maxZ': {'python_name': ['max', 'z']},
    }
}
