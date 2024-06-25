import ctypes

class VkVideoEncodeH265DpbSlotInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pStdReferenceInfo': ctypes.POINTER(StdVideoEncodeH265ReferenceInfo),
        }


from .StdVideoEncodeH265ReferenceInfo import StdVideoEncodeH265ReferenceInfo

VkVideoEncodeH265DpbSlotInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdReferenceInfo', ctypes.POINTER(StdVideoEncodeH265ReferenceInfo)),
]
