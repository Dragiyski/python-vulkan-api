import ctypes

class CType(ctypes.Structure):
    pass

from .VkVideoEncodeRateControlLayerInfoKHR import CType as VkVideoEncodeRateControlLayerInfoKHR

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('rateControlMode', ctypes.c_uint32),
    ('layerCount', ctypes.c_uint32),
    ('pLayers', ctypes.POINTER(VkVideoEncodeRateControlLayerInfoKHR)),
    ('virtualBufferSizeInMs', ctypes.c_uint32),
    ('initialVirtualBufferSizeInMs', ctypes.c_uint32),
]

descriptor = {
    'extends': {
        'VkVideoBeginCodingInfoKHR',
        'VkVideoCodingControlInfoKHR',
    },
    'extended_by': set(),
    'includes': {
        'VkVideoEncodeRateControlLayerInfoKHR',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_RATE_CONTROL_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkVideoEncodeRateControlFlagsKHR'},
        'rateControlMode': {'python_name': ['rate', 'control', 'mode'], 'type': 'VkVideoEncodeRateControlModeFlagBitsKHR'},
        'layerCount': {'python_name': ['layer', 'count']},
        'pLayers': {'python_name': ['p', 'layers'], 'len': [['layerCount']], 'type': 'VkVideoEncodeRateControlLayerInfoKHR'},
        'virtualBufferSizeInMs': {'python_name': ['virtual', 'buffer', 'size', 'in', 'ms']},
        'initialVirtualBufferSizeInMs': {'python_name': ['initial', 'virtual', 'buffer', 'size', 'in', 'ms']},
    }
}
