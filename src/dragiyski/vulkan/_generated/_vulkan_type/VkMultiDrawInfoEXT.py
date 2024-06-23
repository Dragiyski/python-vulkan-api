import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('firstVertex', ctypes.c_uint32),
        ('vertexCount', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdDrawMultiEXT',
    },
    'output_of': set(),
    'member_map': {
        'firstVertex': {'python_name': ['first', 'vertex']},
        'vertexCount': {'python_name': ['vertex', 'count']},
    }
}
