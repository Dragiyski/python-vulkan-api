import ctypes, sys

class VkVideoDecodeH264DpbSlotInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoDecodeH264DpbSlotInfoKHR

from . import StdVideoDecodeH264ReferenceInfo

VkVideoDecodeH264DpbSlotInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoDecodeH264ReferenceInfo)),
]
