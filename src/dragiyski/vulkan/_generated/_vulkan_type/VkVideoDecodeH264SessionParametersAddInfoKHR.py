import ctypes

class VkVideoDecodeH264SessionParametersAddInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'stdSPSCount': ctypes.c_uint32,
            'pStdSPSs': ctypes.POINTER(StdVideoH264SequenceParameterSet),
            'stdPPSCount': ctypes.c_uint32,
            'pStdPPSs': ctypes.POINTER(StdVideoH264PictureParameterSet),
        }


from .StdVideoH264PictureParameterSet import StdVideoH264PictureParameterSet
from .StdVideoH264SequenceParameterSet import StdVideoH264SequenceParameterSet

VkVideoDecodeH264SessionParametersAddInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stdSPSCount', ctypes.c_uint32),
    ('pStdSPSs', ctypes.POINTER(StdVideoH264SequenceParameterSet)),
    ('stdPPSCount', ctypes.c_uint32),
    ('pStdPPSs', ctypes.POINTER(StdVideoH264PictureParameterSet)),
]
