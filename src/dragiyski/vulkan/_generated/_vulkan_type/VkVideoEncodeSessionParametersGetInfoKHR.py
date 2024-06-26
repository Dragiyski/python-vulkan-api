import ctypes

class VkVideoEncodeSessionParametersGetInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('videoSessionParameters', ctypes.c_void_p),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkVideoEncodeH264SessionParametersGetInfoKHR',
        'VkVideoEncodeH265SessionParametersGetInfoKHR',
    }
    _includes_ = set()
    _included_in_ = set()
    _input_of_ = {
        'vkGetEncodedVideoSessionParametersKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'videoSessionParameters': 'video_session_parameters',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_queue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_SESSION_PARAMETERS_GET_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_SESSION_PARAMETERS_GET_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkVideoEncodeSessionParametersGetInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'videoSessionParameters': ctypes.c_void_p,
}
