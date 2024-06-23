import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('consumer', ctypes.c_uint64),
        ('producer', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkNativeBufferANDROID',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'consumer': {'python_name': ['consumer']},
        'producer': {'python_name': ['producer']},
    }
}
