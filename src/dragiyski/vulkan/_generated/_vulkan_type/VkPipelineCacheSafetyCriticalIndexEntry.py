import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('pipelineIdentifier', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('pipelineMemorySize', ctypes.c_uint64),
        ('jsonSize', ctypes.c_uint64),
        ('jsonOffset', ctypes.c_uint64),
        ('stageIndexCount', ctypes.c_uint32),
        ('stageIndexStride', ctypes.c_uint32),
        ('stageIndexOffset', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'pipelineIdentifier': {'python_name': ['pipeline', 'identifier']},
        'pipelineMemorySize': {'python_name': ['pipeline', 'memory', 'size']},
        'jsonSize': {'python_name': ['json', 'size']},
        'jsonOffset': {'python_name': ['json', 'offset']},
        'stageIndexCount': {'python_name': ['stage', 'index', 'count']},
        'stageIndexStride': {'python_name': ['stage', 'index', 'stride']},
        'stageIndexOffset': {'python_name': ['stage', 'index', 'offset']},
    }
}
