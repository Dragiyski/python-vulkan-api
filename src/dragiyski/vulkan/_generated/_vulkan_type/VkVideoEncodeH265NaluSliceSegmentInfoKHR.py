import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH265SliceSegmentHeader import CType as StdVideoEncodeH265SliceSegmentHeader

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('constantQp', ctypes.c_int32),
    ('pStdSliceSegmentHeader', ctypes.POINTER(StdVideoEncodeH265SliceSegmentHeader)),
]
