import ctypes

class VkVideoEncodeH265SessionParametersFeedbackInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('hasStdVPSOverrides', ctypes.c_uint32),
        ('hasStdSPSOverrides', ctypes.c_uint32),
        ('hasStdPPSOverrides', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkVideoEncodeSessionParametersFeedbackInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'hasStdVPSOverrides': 'has_std_vpsoverrides',
        'hasStdSPSOverrides': 'has_std_spsoverrides',
        'hasStdPPSOverrides': 'has_std_ppsoverrides',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_h265',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_SESSION_PARAMETERS_FEEDBACK_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_SESSION_PARAMETERS_FEEDBACK_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkVideoEncodeH265SessionParametersFeedbackInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'hasStdVPSOverrides': ctypes.c_uint32,
    'hasStdSPSOverrides': ctypes.c_uint32,
    'hasStdPPSOverrides': ctypes.c_uint32,
}
