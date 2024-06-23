import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoDecodeAV1ReferenceInfoFlags import CType as StdVideoDecodeAV1ReferenceInfoFlags

CType._fields_ = [
    ('flags', StdVideoDecodeAV1ReferenceInfoFlags),
    ('frame_type', ctypes.c_uint8),
    ('RefFrameSignBias', ctypes.c_uint8),
    ('OrderHint', ctypes.c_uint8),
    ('SavedOrderHints', ctypes.ARRAY(ctypes.c_uint8, 8)),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'StdVideoDecodeAV1ReferenceInfoFlags',
    },
    'included_in': {
        'VkVideoDecodeAV1DpbSlotInfoKHR',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'flags': {'python_name': ['flags'], 'type': 'StdVideoDecodeAV1ReferenceInfoFlags'},
        'frame_type': {'python_name': ['frame', 'type']},
        'RefFrameSignBias': {'python_name': ['ref', 'frame', 'sign', 'bias']},
        'OrderHint': {'python_name': ['order', 'hint']},
        'SavedOrderHints': {'python_name': ['saved', 'order', 'hints']},
    }
}
