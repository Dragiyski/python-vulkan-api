import ctypes

class VkVideoDecodeH265DpbSlotInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pStdReferenceInfo': ctypes.POINTER(StdVideoDecodeH265ReferenceInfo),
        }


from .StdVideoDecodeH265ReferenceInfo import StdVideoDecodeH265ReferenceInfo

VkVideoDecodeH265DpbSlotInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoDecodeH265ReferenceInfo)),
]
