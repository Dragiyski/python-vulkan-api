import ctypes, sys

class VkVideoDecodeH265DpbSlotInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoDecodeH265DpbSlotInfoKHR

from . import StdVideoDecodeH265ReferenceInfo

VkVideoDecodeH265DpbSlotInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoDecodeH265ReferenceInfo)),
]
