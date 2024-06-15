import ctypes, sys

class VkVideoDecodeAV1SessionParametersCreateInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoDecodeAV1SessionParametersCreateInfoKHR

from . import StdVideoAV1SequenceHeader

VkVideoDecodeAV1SessionParametersCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdSequenceHeader', ctypes.POINTER(StdVideoAV1SequenceHeader)),
]
