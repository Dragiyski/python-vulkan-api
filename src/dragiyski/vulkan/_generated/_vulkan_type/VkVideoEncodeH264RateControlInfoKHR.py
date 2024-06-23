import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('gopFrameCount', ctypes.c_uint32),
        ('idrPeriod', ctypes.c_uint32),
        ('consecutiveBFrameCount', ctypes.c_uint32),
        ('temporalLayerCount', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkVideoBeginCodingInfoKHR',
        'VkVideoCodingControlInfoKHR',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_RATE_CONTROL_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkVideoEncodeH264RateControlFlagsKHR'},
        'gopFrameCount': {'python_name': ['gop', 'frame', 'count']},
        'idrPeriod': {'python_name': ['idr', 'period']},
        'consecutiveBFrameCount': {'python_name': ['consecutive', 'bframe', 'count']},
        'temporalLayerCount': {'python_name': ['temporal', 'layer', 'count']},
    }
}
