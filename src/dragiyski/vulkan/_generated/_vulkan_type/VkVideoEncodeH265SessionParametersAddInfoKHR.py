import ctypes

class VkVideoEncodeH265SessionParametersAddInfoKHR(ctypes.Structure):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._type_ = {
            'sType': ctypes.c_int,
            'pNext': ctypes.c_void_p,
            'stdVPSCount': ctypes.c_uint32,
            'pStdVPSs': ctypes.POINTER(StdVideoH265VideoParameterSet),
            'stdSPSCount': ctypes.c_uint32,
            'pStdSPSs': ctypes.POINTER(StdVideoH265SequenceParameterSet),
            'stdPPSCount': ctypes.c_uint32,
            'pStdPPSs': ctypes.POINTER(StdVideoH265PictureParameterSet),
        }


from .StdVideoH265PictureParameterSet import StdVideoH265PictureParameterSet
from .StdVideoH265SequenceParameterSet import StdVideoH265SequenceParameterSet
from .StdVideoH265VideoParameterSet import StdVideoH265VideoParameterSet

VkVideoEncodeH265SessionParametersAddInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stdVPSCount', ctypes.c_uint32),
    ('pStdVPSs', ctypes.POINTER(StdVideoH265VideoParameterSet)),
    ('stdSPSCount', ctypes.c_uint32),
    ('pStdSPSs', ctypes.POINTER(StdVideoH265SequenceParameterSet)),
    ('stdPPSCount', ctypes.c_uint32),
    ('pStdPPSs', ctypes.POINTER(StdVideoH265PictureParameterSet)),
]
