import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('frameISize', ctypes.c_uint32),
        ('framePSize', ctypes.c_uint32),
        ('frameBSize', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkVideoEncodeH264RateControlLayerInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'frameISize': {'python_name': ['frame', 'isize']},
        'framePSize': {'python_name': ['frame', 'psize']},
        'frameBSize': {'python_name': ['frame', 'bsize']},
    }
}
