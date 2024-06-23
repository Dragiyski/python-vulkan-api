import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('firstIndex', ctypes.c_uint32),
        ('indexCount', ctypes.c_uint32),
        ('vertexOffset', ctypes.c_int32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdDrawMultiIndexedEXT',
    },
    'output_of': set(),
    'member_map': {
        'firstIndex': {'python_name': ['first', 'index']},
        'indexCount': {'python_name': ['index', 'count']},
        'vertexOffset': {'python_name': ['vertex', 'offset']},
    }
}
