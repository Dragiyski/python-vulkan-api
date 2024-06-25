import ctypes

class VkVideoDecodeH264DpbSlotInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pStdReferenceInfo': ctypes.POINTER(StdVideoDecodeH264ReferenceInfo),
        }


from .StdVideoDecodeH264ReferenceInfo import StdVideoDecodeH264ReferenceInfo

VkVideoDecodeH264DpbSlotInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoDecodeH264ReferenceInfo)),
]
