import ctypes

class VkVideoEncodeH264DpbSlotInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pStdReferenceInfo': ctypes.POINTER(StdVideoEncodeH264ReferenceInfo),
        }


from .StdVideoEncodeH264ReferenceInfo import StdVideoEncodeH264ReferenceInfo

VkVideoEncodeH264DpbSlotInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoEncodeH264ReferenceInfo)),
]
