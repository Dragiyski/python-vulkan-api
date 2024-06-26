import ctypes

class VkVideoEncodeCapabilitiesKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkVideoCapabilitiesKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkExtent2D',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'flags': 'flags',
        'rateControlModes': 'rate_control_modes',
        'maxRateControlLayers': 'max_rate_control_layers',
        'maxBitrate': 'max_bitrate',
        'maxQualityLevels': 'max_quality_levels',
        'encodeInputPictureGranularity': 'encode_input_picture_granularity',
        'supportedEncodeFeedbackFlags': 'supported_encode_feedback_flags',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_queue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'flags': 'VkVideoEncodeCapabilityFlagsKHR',
        'rateControlModes': 'VkVideoEncodeRateControlModeFlagsKHR',
        'supportedEncodeFeedbackFlags': 'VkVideoEncodeFeedbackFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_CAPABILITIES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_CAPABILITIES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkExtent2D import VkExtent2D

VkVideoEncodeCapabilitiesKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('rateControlModes', ctypes.c_uint32),
    ('maxRateControlLayers', ctypes.c_uint32),
    ('maxBitrate', ctypes.c_uint64),
    ('maxQualityLevels', ctypes.c_uint32),
    ('encodeInputPictureGranularity', VkExtent2D),
    ('supportedEncodeFeedbackFlags', ctypes.c_uint32),
]

VkVideoEncodeCapabilitiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'flags': ctypes.c_uint32,
    'rateControlModes': ctypes.c_uint32,
    'maxRateControlLayers': ctypes.c_uint32,
    'maxBitrate': ctypes.c_uint64,
    'maxQualityLevels': ctypes.c_uint32,
    'encodeInputPictureGranularity': VkExtent2D,
    'supportedEncodeFeedbackFlags': ctypes.c_uint32,
}
