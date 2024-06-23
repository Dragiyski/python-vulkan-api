import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('indexCount', ctypes.c_uint32),
        ('instanceCount', ctypes.c_uint32),
        ('firstIndex', ctypes.c_uint32),
        ('vertexOffset', ctypes.c_int32),
        ('firstInstance', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'indexCount': {'python_name': ['index', 'count']},
        'instanceCount': {'python_name': ['instance', 'count']},
        'firstIndex': {'python_name': ['first', 'index']},
        'vertexOffset': {'python_name': ['vertex', 'offset']},
        'firstInstance': {'python_name': ['first', 'instance']},
    }
}
