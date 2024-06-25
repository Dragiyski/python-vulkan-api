import ctypes

class StdVideoDecodeAV1ReferenceInfo(ctypes.Structure):
    pass

from .StdVideoDecodeAV1ReferenceInfoFlags import StdVideoDecodeAV1ReferenceInfoFlags

StdVideoDecodeAV1ReferenceInfo._fields_ = [
    ('flags', StdVideoDecodeAV1ReferenceInfoFlags),
    ('frame_type', ctypes.c_uint8),
    ('RefFrameSignBias', ctypes.c_uint8),
    ('OrderHint', ctypes.c_uint8),
    ('SavedOrderHints', ctypes.ARRAY(ctypes.c_uint8, 8)),
]

StdVideoDecodeAV1ReferenceInfo._type_ = {
    'flags': StdVideoDecodeAV1ReferenceInfoFlags,
    'frame_type': ctypes.c_uint8,
    'RefFrameSignBias': ctypes.c_uint8,
    'OrderHint': ctypes.c_uint8,
    'SavedOrderHints': ctypes.ARRAY(ctypes.c_uint8, 8),
}
