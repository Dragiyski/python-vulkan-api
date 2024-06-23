import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoEncodeH264QpKHR import CType as VkVideoEncodeH264QpKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('preferredRateControlFlags', ctypes.c_uint32),
    ('preferredGopFrameCount', ctypes.c_uint32),
    ('preferredIdrPeriod', ctypes.c_uint32),
    ('preferredConsecutiveBFrameCount', ctypes.c_uint32),
    ('preferredTemporalLayerCount', ctypes.c_uint32),
    ('preferredConstantQp', VkVideoEncodeH264QpKHR),
    ('preferredMaxL0ReferenceCount', ctypes.c_uint32),
    ('preferredMaxL1ReferenceCount', ctypes.c_uint32),
    ('preferredStdEntropyCodingModeFlag', ctypes.c_uint32),
]

descriptor = {
    'extends': {
        'VkVideoEncodeQualityLevelPropertiesKHR',
    },
    'extended_by': set(),
    'includes': {
        'VkVideoEncodeH264QpKHR',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_QUALITY_LEVEL_PROPERTIES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'preferredRateControlFlags': {'python_name': ['preferred', 'rate', 'control', 'flags'], 'type': 'VkVideoEncodeH264RateControlFlagsKHR'},
        'preferredGopFrameCount': {'python_name': ['preferred', 'gop', 'frame', 'count']},
        'preferredIdrPeriod': {'python_name': ['preferred', 'idr', 'period']},
        'preferredConsecutiveBFrameCount': {'python_name': ['preferred', 'consecutive', 'bframe', 'count']},
        'preferredTemporalLayerCount': {'python_name': ['preferred', 'temporal', 'layer', 'count']},
        'preferredConstantQp': {'python_name': ['preferred', 'constant', 'qp'], 'type': 'VkVideoEncodeH264QpKHR'},
        'preferredMaxL0ReferenceCount': {'python_name': ['preferred', 'max', 'l0reference', 'count']},
        'preferredMaxL1ReferenceCount': {'python_name': ['preferred', 'max', 'l1reference', 'count']},
        'preferredStdEntropyCodingModeFlag': {'python_name': ['preferred', 'std', 'entropy', 'coding', 'mode', 'flag']},
    }
}
