import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('qpI', ctypes.c_int32),
        ('qpP', ctypes.c_int32),
        ('qpB', ctypes.c_int32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkVideoEncodeH264QualityLevelPropertiesKHR',
        'VkVideoEncodeH264RateControlLayerInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'qpI': {'python_name': ['qp', 'i']},
        'qpP': {'python_name': ['qp', 'p']},
        'qpB': {'python_name': ['qp', 'b']},
    }
}
