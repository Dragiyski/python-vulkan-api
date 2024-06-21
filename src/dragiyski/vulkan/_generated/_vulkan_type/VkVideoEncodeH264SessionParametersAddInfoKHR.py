import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoH264PictureParameterSet import CType as StdVideoH264PictureParameterSet
from .StdVideoH264SequenceParameterSet import CType as StdVideoH264SequenceParameterSet

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stdSPSCount', ctypes.c_uint32),
    ('pStdSPSs', ctypes.POINTER(StdVideoH264SequenceParameterSet)),
    ('stdPPSCount', ctypes.c_uint32),
    ('pStdPPSs', ctypes.POINTER(StdVideoH264PictureParameterSet)),
]
