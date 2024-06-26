import ctypes

class VkVideoDecodeH265SessionParametersAddInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkVideoSessionParametersUpdateInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'StdVideoH265PictureParameterSet',
        'StdVideoH265SequenceParameterSet',
        'StdVideoH265VideoParameterSet',
    }
    _included_in_ = {
        'VkVideoDecodeH265SessionParametersCreateInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'stdVPSCount': 'std_vpscount',
        'pStdVPSs': 'std_vpss',
        'stdSPSCount': 'std_spscount',
        'pStdSPSs': 'std_spss',
        'stdPPSCount': 'std_ppscount',
        'pStdPPSs': 'std_ppss',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_decode_h265',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_SESSION_PARAMETERS_ADD_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_SESSION_PARAMETERS_ADD_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoH265PictureParameterSet import StdVideoH265PictureParameterSet
from .StdVideoH265SequenceParameterSet import StdVideoH265SequenceParameterSet
from .StdVideoH265VideoParameterSet import StdVideoH265VideoParameterSet

VkVideoDecodeH265SessionParametersAddInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stdVPSCount', ctypes.c_uint32),
    ('pStdVPSs', ctypes.POINTER(StdVideoH265VideoParameterSet)),
    ('stdSPSCount', ctypes.c_uint32),
    ('pStdSPSs', ctypes.POINTER(StdVideoH265SequenceParameterSet)),
    ('stdPPSCount', ctypes.c_uint32),
    ('pStdPPSs', ctypes.POINTER(StdVideoH265PictureParameterSet)),
]

VkVideoDecodeH265SessionParametersAddInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'stdVPSCount': ctypes.c_uint32,
    'pStdVPSs': ctypes.POINTER(StdVideoH265VideoParameterSet),
    'stdSPSCount': ctypes.c_uint32,
    'pStdSPSs': ctypes.POINTER(StdVideoH265SequenceParameterSet),
    'stdPPSCount': ctypes.c_uint32,
    'pStdPPSs': ctypes.POINTER(StdVideoH265PictureParameterSet),
}
