import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoEncodeH265QpKHR import CType as VkVideoEncodeH265QpKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('preferredRateControlFlags', ctypes.c_uint32),
    ('preferredGopFrameCount', ctypes.c_uint32),
    ('preferredIdrPeriod', ctypes.c_uint32),
    ('preferredConsecutiveBFrameCount', ctypes.c_uint32),
    ('preferredSubLayerCount', ctypes.c_uint32),
    ('preferredConstantQp', VkVideoEncodeH265QpKHR),
    ('preferredMaxL0ReferenceCount', ctypes.c_uint32),
    ('preferredMaxL1ReferenceCount', ctypes.c_uint32),
]

descriptor = {
    'extends': {
        'VkVideoEncodeQualityLevelPropertiesKHR',
    },
    'extended_by': set(),
    'includes': {
        'VkVideoEncodeH265QpKHR',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_QUALITY_LEVEL_PROPERTIES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'preferredRateControlFlags': {'python_name': ['preferred', 'rate', 'control', 'flags'], 'type': 'VkVideoEncodeH265RateControlFlagsKHR'},
        'preferredGopFrameCount': {'python_name': ['preferred', 'gop', 'frame', 'count']},
        'preferredIdrPeriod': {'python_name': ['preferred', 'idr', 'period']},
        'preferredConsecutiveBFrameCount': {'python_name': ['preferred', 'consecutive', 'bframe', 'count']},
        'preferredSubLayerCount': {'python_name': ['preferred', 'sub', 'layer', 'count']},
        'preferredConstantQp': {'python_name': ['preferred', 'constant', 'qp'], 'type': 'VkVideoEncodeH265QpKHR'},
        'preferredMaxL0ReferenceCount': {'python_name': ['preferred', 'max', 'l0reference', 'count']},
        'preferredMaxL1ReferenceCount': {'python_name': ['preferred', 'max', 'l1reference', 'count']},
    }
}
