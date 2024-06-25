import ctypes

class VkVideoDecodeH264SessionParametersAddInfoKHR(ctypes.Structure):
    pass

from .StdVideoH264PictureParameterSet import StdVideoH264PictureParameterSet
from .StdVideoH264SequenceParameterSet import StdVideoH264SequenceParameterSet

VkVideoDecodeH264SessionParametersAddInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stdSPSCount', ctypes.c_uint32),
    ('pStdSPSs', ctypes.POINTER(StdVideoH264SequenceParameterSet)),
    ('stdPPSCount', ctypes.c_uint32),
    ('pStdPPSs', ctypes.POINTER(StdVideoH264PictureParameterSet)),
]

VkVideoDecodeH264SessionParametersAddInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stdSPSCount': ctypes.c_uint32,
    'pStdSPSs': ctypes.POINTER(StdVideoH264SequenceParameterSet),
    'stdPPSCount': ctypes.c_uint32,
    'pStdPPSs': ctypes.POINTER(StdVideoH264PictureParameterSet),
}
