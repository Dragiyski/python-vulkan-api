import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH264SliceHeader import CType as StdVideoEncodeH264SliceHeader

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('constantQp', ctypes.c_int32),
    ('pStdSliceHeader', ctypes.POINTER(StdVideoEncodeH264SliceHeader)),
]
