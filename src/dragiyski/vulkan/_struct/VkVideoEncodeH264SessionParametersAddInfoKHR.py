import ctypes, sys

class VkVideoEncodeH264SessionParametersAddInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoEncodeH264SessionParametersAddInfoKHR

from . import StdVideoH264SequenceParameterSet
from . import StdVideoH264PictureParameterSet

VkVideoEncodeH264SessionParametersAddInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stdSPSCount', ctypes.c_uint32),
    ('pStdSPSs', ctypes.POINTER(StdVideoH264SequenceParameterSet)),
    ('stdPPSCount', ctypes.c_uint32),
    ('pStdPPSs', ctypes.POINTER(StdVideoH264PictureParameterSet)),
]
