import ctypes

class VkVideoDecodeH264SessionParametersAddInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkVideoSessionParametersUpdateInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'StdVideoH264PictureParameterSet',
        'StdVideoH264SequenceParameterSet',
    }
    _included_in_ = {
        'VkVideoDecodeH264SessionParametersCreateInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'stdSPSCount': 'std_spscount',
        'pStdSPSs': 'std_spss',
        'stdPPSCount': 'std_ppscount',
        'pStdPPSs': 'std_ppss',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_decode_h264',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_DECODE_H264_SESSION_PARAMETERS_ADD_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H264_SESSION_PARAMETERS_ADD_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


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

VkVideoDecodeH264SessionParametersAddInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stdSPSCount': ctypes.c_uint32,
    'pStdSPSs': ctypes.POINTER(StdVideoH264SequenceParameterSet),
    'stdPPSCount': ctypes.c_uint32,
    'pStdPPSs': ctypes.POINTER(StdVideoH264PictureParameterSet),
}
