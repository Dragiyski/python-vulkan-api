import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('averageBitrate', ctypes.c_uint64),
        ('maxBitrate', ctypes.c_uint64),
        ('frameRateNumerator', ctypes.c_uint32),
        ('frameRateDenominator', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkVideoEncodeH264RateControlLayerInfoKHR',
        'VkVideoEncodeH265RateControlLayerInfoKHR',
    },
    'includes': set(),
    'included_in': {
        'VkVideoEncodeRateControlInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_RATE_CONTROL_LAYER_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'averageBitrate': {'python_name': ['average', 'bitrate']},
        'maxBitrate': {'python_name': ['max', 'bitrate']},
        'frameRateNumerator': {'python_name': ['frame', 'rate', 'numerator']},
        'frameRateDenominator': {'python_name': ['frame', 'rate', 'denominator']},
    }
}
