import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoEncodeH265FrameSizeKHR import CType as VkVideoEncodeH265FrameSizeKHR
from .VkVideoEncodeH265QpKHR import CType as VkVideoEncodeH265QpKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('useMinQp', ctypes.c_uint32),
    ('minQp', VkVideoEncodeH265QpKHR),
    ('useMaxQp', ctypes.c_uint32),
    ('maxQp', VkVideoEncodeH265QpKHR),
    ('useMaxFrameSize', ctypes.c_uint32),
    ('maxFrameSize', VkVideoEncodeH265FrameSizeKHR),
]

descriptor = {
    'extends': {
        'VkVideoEncodeRateControlLayerInfoKHR',
    },
    'extended_by': set(),
    'includes': {
        'VkVideoEncodeH265FrameSizeKHR',
        'VkVideoEncodeH265QpKHR',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_RATE_CONTROL_LAYER_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'useMinQp': {'python_name': ['use', 'min', 'qp']},
        'minQp': {'python_name': ['min', 'qp'], 'type': 'VkVideoEncodeH265QpKHR'},
        'useMaxQp': {'python_name': ['use', 'max', 'qp']},
        'maxQp': {'python_name': ['max', 'qp'], 'type': 'VkVideoEncodeH265QpKHR'},
        'useMaxFrameSize': {'python_name': ['use', 'max', 'frame', 'size']},
        'maxFrameSize': {'python_name': ['max', 'frame', 'size'], 'type': 'VkVideoEncodeH265FrameSizeKHR'},
    }
}
