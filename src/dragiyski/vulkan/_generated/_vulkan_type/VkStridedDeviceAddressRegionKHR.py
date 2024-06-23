import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('deviceAddress', ctypes.c_uint64),
        ('stride', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdTraceRaysIndirectKHR',
        'vkCmdTraceRaysKHR',
    },
    'output_of': set(),
    'member_map': {
        'deviceAddress': {'python_name': ['device', 'address']},
        'stride': {'python_name': ['stride']},
        'size': {'python_name': ['size']},
    }
}
