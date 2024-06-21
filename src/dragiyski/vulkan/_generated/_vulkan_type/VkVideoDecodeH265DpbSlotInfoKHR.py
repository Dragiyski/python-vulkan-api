import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoDecodeH265ReferenceInfo import CType as StdVideoDecodeH265ReferenceInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoDecodeH265ReferenceInfo)),
]
