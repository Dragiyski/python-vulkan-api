import ctypes

class VkVideoDecodeAV1SessionParametersCreateInfoKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkVideoSessionParametersCreateInfoKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'StdVideoAV1SequenceHeader',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'pStdSequenceHeader': 'std_sequence_header',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_decode_av1',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_DECODE_AV1_SESSION_PARAMETERS_CREATE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_DECODE_AV1_SESSION_PARAMETERS_CREATE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .StdVideoAV1SequenceHeader import StdVideoAV1SequenceHeader

VkVideoDecodeAV1SessionParametersCreateInfoKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('pStdSequenceHeader', ctypes.POINTER(StdVideoAV1SequenceHeader)),
]

VkVideoDecodeAV1SessionParametersCreateInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'pStdSequenceHeader': ctypes.POINTER(StdVideoAV1SequenceHeader),
}
