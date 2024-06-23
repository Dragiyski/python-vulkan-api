import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('pipelineAddress', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'pipelineAddress': {'python_name': ['pipeline', 'address']},
    }
}
