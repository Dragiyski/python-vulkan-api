import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('constantID', ctypes.c_uint32),
        ('offset', ctypes.c_uint32),
        ('size', ctypes.c_size_t),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkSpecializationInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'constantID': {'python_name': ['constant', 'id']},
        'offset': {'python_name': ['offset']},
        'size': {'python_name': ['size']},
    }
}
