import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoDecodeAV1ReferenceInfo import CType as StdVideoDecodeAV1ReferenceInfo

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoDecodeAV1ReferenceInfo)),
]
