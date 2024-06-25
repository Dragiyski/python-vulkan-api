import ctypes

class VkVideoDecodeAV1SessionParametersCreateInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'pStdSequenceHeader': ctypes.POINTER(StdVideoAV1SequenceHeader),
        }


from .StdVideoAV1SequenceHeader import StdVideoAV1SequenceHeader

VkVideoDecodeAV1SessionParametersCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdSequenceHeader', ctypes.POINTER(StdVideoAV1SequenceHeader)),
]
