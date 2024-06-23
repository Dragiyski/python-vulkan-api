import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('bufferAddress', ctypes.c_uint64),
        ('size', ctypes.c_uint32),
        ('indexType', ctypes.c_int),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'bufferAddress': {'python_name': ['buffer', 'address']},
        'size': {'python_name': ['size']},
        'indexType': {'python_name': ['index', 'type'], 'type': 'VkIndexType'},
    }
}
