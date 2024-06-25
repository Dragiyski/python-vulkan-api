import ctypes

class VkVideoDecodeAV1DpbSlotInfoKHR(ctypes.Structure):
    pass

from .StdVideoDecodeAV1ReferenceInfo import StdVideoDecodeAV1ReferenceInfo

VkVideoDecodeAV1DpbSlotInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoDecodeAV1ReferenceInfo)),
]

VkVideoDecodeAV1DpbSlotInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pStdReferenceInfo': ctypes.POINTER(StdVideoDecodeAV1ReferenceInfo),
}
