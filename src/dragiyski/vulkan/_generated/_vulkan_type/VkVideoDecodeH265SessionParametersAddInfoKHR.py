import ctypes

class VkVideoDecodeH265SessionParametersAddInfoKHR(ctypes.Structure):
    pass

from .StdVideoH265PictureParameterSet import StdVideoH265PictureParameterSet
from .StdVideoH265SequenceParameterSet import StdVideoH265SequenceParameterSet
from .StdVideoH265VideoParameterSet import StdVideoH265VideoParameterSet

VkVideoDecodeH265SessionParametersAddInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stdVPSCount', ctypes.c_uint32),
    ('pStdVPSs', ctypes.POINTER(StdVideoH265VideoParameterSet)),
    ('stdSPSCount', ctypes.c_uint32),
    ('pStdSPSs', ctypes.POINTER(StdVideoH265SequenceParameterSet)),
    ('stdPPSCount', ctypes.c_uint32),
    ('pStdPPSs', ctypes.POINTER(StdVideoH265PictureParameterSet)),
]

VkVideoDecodeH265SessionParametersAddInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stdVPSCount': ctypes.c_uint32,
    'pStdVPSs': ctypes.POINTER(StdVideoH265VideoParameterSet),
    'stdSPSCount': ctypes.c_uint32,
    'pStdSPSs': ctypes.POINTER(StdVideoH265SequenceParameterSet),
    'stdPPSCount': ctypes.c_uint32,
    'pStdPPSs': ctypes.POINTER(StdVideoH265PictureParameterSet),
}
