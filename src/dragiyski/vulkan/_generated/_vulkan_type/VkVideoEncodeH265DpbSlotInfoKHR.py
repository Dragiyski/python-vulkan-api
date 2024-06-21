import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH265ReferenceInfo import CType as StdVideoEncodeH265ReferenceInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoEncodeH265ReferenceInfo)),
]
