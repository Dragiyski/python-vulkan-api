import ctypes

class CType(ctypes.Structure):
    pass

from .VkExtent2D import CType as VkExtent2D

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('rateControlModes', ctypes.c_uint32),
    ('maxRateControlLayers', ctypes.c_uint32),
    ('maxBitrate', ctypes.c_uint64),
    ('maxQualityLevels', ctypes.c_uint32),
    ('encodeInputPictureGranularity', VkExtent2D),
    ('supportedEncodeFeedbackFlags', ctypes.c_uint32),
]

descriptor = {
    'extends': {
        'VkVideoCapabilitiesKHR',
    },
    'extended_by': set(),
    'includes': {
        'VkExtent2D',
    },
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_CAPABILITIES_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkVideoEncodeCapabilityFlagsKHR'},
        'rateControlModes': {'python_name': ['rate', 'control', 'modes'], 'type': 'VkVideoEncodeRateControlModeFlagsKHR'},
        'maxRateControlLayers': {'python_name': ['max', 'rate', 'control', 'layers']},
        'maxBitrate': {'python_name': ['max', 'bitrate']},
        'maxQualityLevels': {'python_name': ['max', 'quality', 'levels']},
        'encodeInputPictureGranularity': {'python_name': ['encode', 'input', 'picture', 'granularity'], 'type': 'VkExtent2D'},
        'supportedEncodeFeedbackFlags': {'python_name': ['supported', 'encode', 'feedback', 'flags'], 'type': 'VkVideoEncodeFeedbackFlagsKHR'},
    }
}
