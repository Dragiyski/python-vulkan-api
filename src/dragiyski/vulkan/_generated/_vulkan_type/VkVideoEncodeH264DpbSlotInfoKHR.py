import ctypes, sys

class VkVideoEncodeH264DpbSlotInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoEncodeH264DpbSlotInfoKHR

from . import StdVideoEncodeH264ReferenceInfo

VkVideoEncodeH264DpbSlotInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoEncodeH264ReferenceInfo)),
]
