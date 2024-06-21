import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoAV1SequenceHeader import CType as StdVideoAV1SequenceHeader

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdSequenceHeader', ctypes.POINTER(StdVideoAV1SequenceHeader)),
]
