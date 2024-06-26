import ctypes

class VkVideoEncodeH264SessionParametersGetInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('writeStdSPS', ctypes.c_uint32),
        ('writeStdPPS', ctypes.c_uint32),
        ('stdSPSId', ctypes.c_uint32),
        ('stdPPSId', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkVideoEncodeSessionParametersGetInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'writeStdSPS': 'write_std_sps',
        'writeStdPPS': 'write_std_pps',
        'stdSPSId': 'std_spsid',
        'stdPPSId': 'std_ppsid',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_h264',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_SESSION_PARAMETERS_GET_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_SESSION_PARAMETERS_GET_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkVideoEncodeH264SessionParametersGetInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'writeStdSPS': ctypes.c_uint32,
    'writeStdPPS': ctypes.c_uint32,
    'stdSPSId': ctypes.c_uint32,
    'stdPPSId': ctypes.c_uint32,
}
