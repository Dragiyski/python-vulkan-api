import ctypes, sys

class VkVideoEncodeH265DpbSlotInfoKHR(ctypes.Structure):
    pass

sys.modules[__name__] = VkVideoEncodeH265DpbSlotInfoKHR

from . import StdVideoEncodeH265ReferenceInfo

VkVideoEncodeH265DpbSlotInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoEncodeH265ReferenceInfo)),
]
