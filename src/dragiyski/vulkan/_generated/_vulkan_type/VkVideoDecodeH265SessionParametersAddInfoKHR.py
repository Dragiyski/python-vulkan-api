import ctypes

class CType(ctypes.Structure):
    pass

from .StdVideoH265PictureParameterSet import CType as StdVideoH265PictureParameterSet
from .StdVideoH265SequenceParameterSet import CType as StdVideoH265SequenceParameterSet
from .StdVideoH265VideoParameterSet import CType as StdVideoH265VideoParameterSet

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stdVPSCount', ctypes.c_uint32),
    ('pStdVPSs', ctypes.POINTER(StdVideoH265VideoParameterSet)),
    ('stdSPSCount', ctypes.c_uint32),
    ('pStdSPSs', ctypes.POINTER(StdVideoH265SequenceParameterSet)),
    ('stdPPSCount', ctypes.c_uint32),
    ('pStdPPSs', ctypes.POINTER(StdVideoH265PictureParameterSet)),
]
