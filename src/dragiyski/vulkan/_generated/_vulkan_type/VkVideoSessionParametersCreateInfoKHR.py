import ctypes

class VkVideoSessionParametersCreateInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('videoSessionParametersTemplate', ctypes.c_void_p),
        ('videoSession', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkVideoDecodeAV1SessionParametersCreateInfoKHR',
        'VkVideoDecodeH264SessionParametersCreateInfoKHR',
        'VkVideoDecodeH265SessionParametersCreateInfoKHR',
        'VkVideoEncodeH264SessionParametersCreateInfoKHR',
        'VkVideoEncodeH265SessionParametersCreateInfoKHR',
        'VkVideoEncodeQualityLevelInfoKHR',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkCreateVideoSessionParametersKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'videoSessionParametersTemplate': 'video_session_parameters_template',
        'videoSession': 'video_session',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_queue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkVideoSessionParametersCreateFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_SESSION_PARAMETERS_CREATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_SESSION_PARAMETERS_CREATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkVideoSessionParametersCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'videoSessionParametersTemplate': ctypes.c_void_p,
    'videoSession': ctypes.c_void_p,
}
