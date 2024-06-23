import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('maxLevelIdc', ctypes.c_int),
        ('maxSliceCount', ctypes.c_uint32),
        ('maxPPictureL0ReferenceCount', ctypes.c_uint32),
        ('maxBPictureL0ReferenceCount', ctypes.c_uint32),
        ('maxL1ReferenceCount', ctypes.c_uint32),
        ('maxTemporalLayerCount', ctypes.c_uint32),
        ('expectDyadicTemporalLayerPattern', ctypes.c_uint32),
        ('minQp', ctypes.c_int32),
        ('maxQp', ctypes.c_int32),
        ('prefersGopRemainingFrames', ctypes.c_uint32),
        ('requiresGopRemainingFrames', ctypes.c_uint32),
        ('stdSyntaxFlags', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkVideoCapabilitiesKHR',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_CAPABILITIES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkVideoEncodeH264CapabilityFlagsKHR'},
        'maxLevelIdc': {'python_name': ['max', 'level', 'idc'], 'type': 'StdVideoH264LevelIdc'},
        'maxSliceCount': {'python_name': ['max', 'slice', 'count']},
        'maxPPictureL0ReferenceCount': {'python_name': ['max', 'ppicture', 'l0reference', 'count']},
        'maxBPictureL0ReferenceCount': {'python_name': ['max', 'bpicture', 'l0reference', 'count']},
        'maxL1ReferenceCount': {'python_name': ['max', 'l1reference', 'count']},
        'maxTemporalLayerCount': {'python_name': ['max', 'temporal', 'layer', 'count']},
        'expectDyadicTemporalLayerPattern': {'python_name': ['expect', 'dyadic', 'temporal', 'layer', 'pattern']},
        'minQp': {'python_name': ['min', 'qp']},
        'maxQp': {'python_name': ['max', 'qp']},
        'prefersGopRemainingFrames': {'python_name': ['prefers', 'gop', 'remaining', 'frames']},
        'requiresGopRemainingFrames': {'python_name': ['requires', 'gop', 'remaining', 'frames']},
        'stdSyntaxFlags': {'python_name': ['std', 'syntax', 'flags'], 'type': 'VkVideoEncodeH264StdFlagsKHR'},
    }
}
