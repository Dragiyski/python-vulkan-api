import ctypes

class VkVideoEncodeSessionParametersFeedbackInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('hasOverrides', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkVideoEncodeH264SessionParametersFeedbackInfoKHR',
        'VkVideoEncodeH265SessionParametersFeedbackInfoKHR',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = {
        'vkGetEncodedVideoSessionParametersKHR',
    }
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'hasOverrides': 'has_overrides',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_queue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_SESSION_PARAMETERS_FEEDBACK_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_SESSION_PARAMETERS_FEEDBACK_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkVideoEncodeSessionParametersFeedbackInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'hasOverrides': ctypes.c_uint32,
}
