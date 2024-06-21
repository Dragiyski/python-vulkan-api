import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoEncodeH264ReferenceInfo import CType as StdVideoEncodeH264ReferenceInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoEncodeH264ReferenceInfo)),
]
