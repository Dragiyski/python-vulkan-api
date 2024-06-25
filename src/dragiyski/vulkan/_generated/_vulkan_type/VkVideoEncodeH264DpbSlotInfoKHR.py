import ctypes

class VkVideoEncodeH264DpbSlotInfoKHR(ctypes.Structure):
    pass

from .StdVideoEncodeH264ReferenceInfo import StdVideoEncodeH264ReferenceInfo

VkVideoEncodeH264DpbSlotInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoEncodeH264ReferenceInfo)),
]

VkVideoEncodeH264DpbSlotInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pStdReferenceInfo': ctypes.POINTER(StdVideoEncodeH264ReferenceInfo),
}
