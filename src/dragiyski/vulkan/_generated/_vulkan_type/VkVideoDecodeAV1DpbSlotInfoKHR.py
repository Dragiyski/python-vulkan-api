import ctypes

class VkVideoDecodeAV1DpbSlotInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pStdReferenceInfo': ctypes.POINTER(StdVideoDecodeAV1ReferenceInfo),
        }


from .StdVideoDecodeAV1ReferenceInfo import StdVideoDecodeAV1ReferenceInfo

VkVideoDecodeAV1DpbSlotInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoDecodeAV1ReferenceInfo)),
]
