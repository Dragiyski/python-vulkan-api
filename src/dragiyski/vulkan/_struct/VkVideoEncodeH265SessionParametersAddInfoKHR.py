import ctypes, sys

class VkVideoEncodeH265SessionParametersAddInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoEncodeH265SessionParametersAddInfoKHR

from . import StdVideoH265SequenceParameterSet
from . import StdVideoH265VideoParameterSet
from . import StdVideoH265PictureParameterSet

VkVideoEncodeH265SessionParametersAddInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stdVPSCount', ctypes.c_uint32),
    ('pStdVPSs', ctypes.POINTER(StdVideoH265VideoParameterSet)),
    ('stdSPSCount', ctypes.c_uint32),
    ('pStdSPSs', ctypes.POINTER(StdVideoH265SequenceParameterSet)),
    ('stdPPSCount', ctypes.c_uint32),
    ('pStdPPSs', ctypes.POINTER(StdVideoH265PictureParameterSet)),
]
