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
