import ctypes

class VkVideoDecodeAV1SessionParametersCreateInfoKHR(ctypes.Structure):
    pass

from .StdVideoAV1SequenceHeader import StdVideoAV1SequenceHeader

VkVideoDecodeAV1SessionParametersCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdSequenceHeader', ctypes.POINTER(StdVideoAV1SequenceHeader)),
]

VkVideoDecodeAV1SessionParametersCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pStdSequenceHeader': ctypes.POINTER(StdVideoAV1SequenceHeader),
}
