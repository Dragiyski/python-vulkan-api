import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('taskCount', ctypes.c_uint32),
        ('firstTask', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'taskCount': {'python_name': ['task', 'count']},
        'firstTask': {'python_name': ['first', 'task']},
    }
}
