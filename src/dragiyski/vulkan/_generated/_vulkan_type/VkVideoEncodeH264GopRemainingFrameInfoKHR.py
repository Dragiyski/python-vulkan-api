import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('useGopRemainingFrames', ctypes.c_uint32),
        ('gopRemainingI', ctypes.c_uint32),
        ('gopRemainingP', ctypes.c_uint32),
        ('gopRemainingB', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkVideoBeginCodingInfoKHR',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_GOP_REMAINING_FRAME_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'useGopRemainingFrames': {'python_name': ['use', 'gop', 'remaining', 'frames']},
        'gopRemainingI': {'python_name': ['gop', 'remaining', 'i']},
        'gopRemainingP': {'python_name': ['gop', 'remaining', 'p']},
        'gopRemainingB': {'python_name': ['gop', 'remaining', 'b']},
    }
}
