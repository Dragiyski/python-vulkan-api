import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoEncodeH264FrameSizeKHR import CType as VkVideoEncodeH264FrameSizeKHR
from .VkVideoEncodeH264QpKHR import CType as VkVideoEncodeH264QpKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('useMinQp', ctypes.c_uint32),
    ('minQp', VkVideoEncodeH264QpKHR),
    ('useMaxQp', ctypes.c_uint32),
    ('maxQp', VkVideoEncodeH264QpKHR),
    ('useMaxFrameSize', ctypes.c_uint32),
    ('maxFrameSize', VkVideoEncodeH264FrameSizeKHR),
]

descriptor = {
    'extends': {
        'VkVideoEncodeRateControlLayerInfoKHR',
    },
    'extended_by': set(),
    'includes': {
        'VkVideoEncodeH264FrameSizeKHR',
        'VkVideoEncodeH264QpKHR',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_RATE_CONTROL_LAYER_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'useMinQp': {'python_name': ['use', 'min', 'qp']},
        'minQp': {'python_name': ['min', 'qp'], 'type': 'VkVideoEncodeH264QpKHR'},
        'useMaxQp': {'python_name': ['use', 'max', 'qp']},
        'maxQp': {'python_name': ['max', 'qp'], 'type': 'VkVideoEncodeH264QpKHR'},
        'useMaxFrameSize': {'python_name': ['use', 'max', 'frame', 'size']},
        'maxFrameSize': {'python_name': ['max', 'frame', 'size'], 'type': 'VkVideoEncodeH264FrameSizeKHR'},
    }
}
