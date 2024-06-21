import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoDecodeH264ReferenceInfo import CType as StdVideoDecodeH264ReferenceInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoDecodeH264ReferenceInfo)),
]
