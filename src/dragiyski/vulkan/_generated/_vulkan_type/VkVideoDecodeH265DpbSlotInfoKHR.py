import ctypes

class VkVideoDecodeH265DpbSlotInfoKHR(ctypes.Structure):
    pass

from .StdVideoDecodeH265ReferenceInfo import StdVideoDecodeH265ReferenceInfo

VkVideoDecodeH265DpbSlotInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoDecodeH265ReferenceInfo)),
]

VkVideoDecodeH265DpbSlotInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pStdReferenceInfo': ctypes.POINTER(StdVideoDecodeH265ReferenceInfo),
}
