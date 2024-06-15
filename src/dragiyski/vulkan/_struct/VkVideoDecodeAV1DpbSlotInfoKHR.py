import ctypes, sys

class VkVideoDecodeAV1DpbSlotInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoDecodeAV1DpbSlotInfoKHR

from . import StdVideoDecodeAV1ReferenceInfo

VkVideoDecodeAV1DpbSlotInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoDecodeAV1ReferenceInfo)),
]
