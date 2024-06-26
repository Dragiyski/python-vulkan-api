import ctypes

class VkVideoEncodeH264QualityLevelPropertiesKHR(ctypes.Structure):
    _init_ = []
    _extends_ = {
        'VkVideoEncodeQualityLevelPropertiesKHR',
    }
    _extended_by_ = set()
    _includes_ = {
        'VkVideoEncodeH264QpKHR',
    }
    _included_in_ = set()
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'preferredRateControlFlags': 'preferred_rate_control_flags',
        'preferredGopFrameCount': 'preferred_gop_frame_count',
        'preferredIdrPeriod': 'preferred_idr_period',
        'preferredConsecutiveBFrameCount': 'preferred_consecutive_bframe_count',
        'preferredTemporalLayerCount': 'preferred_temporal_layer_count',
        'preferredConstantQp': 'preferred_constant_qp',
        'preferredMaxL0ReferenceCount': 'preferred_max_l0reference_count',
        'preferredMaxL1ReferenceCount': 'preferred_max_l1reference_count',
        'preferredStdEntropyCodingModeFlag': 'preferred_std_entropy_coding_mode_flag',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_h264',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'preferredRateControlFlags': 'VkVideoEncodeH264RateControlFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_QUALITY_LEVEL_PROPERTIES_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_QUALITY_LEVEL_PROPERTIES_KHR
        for function in self._init_:
            function(self, *args, **kwargs)


from .VkVideoEncodeH264QpKHR import VkVideoEncodeH264QpKHR

VkVideoEncodeH264QualityLevelPropertiesKHR._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('preferredRateControlFlags', ctypes.c_uint32),
    ('preferredGopFrameCount', ctypes.c_uint32),
    ('preferredIdrPeriod', ctypes.c_uint32),
    ('preferredConsecutiveBFrameCount', ctypes.c_uint32),
    ('preferredTemporalLayerCount', ctypes.c_uint32),
    ('preferredConstantQp', VkVideoEncodeH264QpKHR),
    ('preferredMaxL0ReferenceCount', ctypes.c_uint32),
    ('preferredMaxL1ReferenceCount', ctypes.c_uint32),
    ('preferredStdEntropyCodingModeFlag', ctypes.c_uint32),
]

VkVideoEncodeH264QualityLevelPropertiesKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'preferredRateControlFlags': ctypes.c_uint32,
    'preferredGopFrameCount': ctypes.c_uint32,
    'preferredIdrPeriod': ctypes.c_uint32,
    'preferredConsecutiveBFrameCount': ctypes.c_uint32,
    'preferredTemporalLayerCount': ctypes.c_uint32,
    'preferredConstantQp': VkVideoEncodeH264QpKHR,
    'preferredMaxL0ReferenceCount': ctypes.c_uint32,
    'preferredMaxL1ReferenceCount': ctypes.c_uint32,
    'preferredStdEntropyCodingModeFlag': ctypes.c_uint32,
}
