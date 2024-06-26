import ctypes

class VkVideoEncodeRateControlLayerInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('averageBitrate', ctypes.c_uint64),
        ('maxBitrate', ctypes.c_uint64),
        ('frameRateNumerator', ctypes.c_uint32),
        ('frameRateDenominator', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = set()
    _extended_by_ = {
        'VkVideoEncodeH264RateControlLayerInfoKHR',
        'VkVideoEncodeH265RateControlLayerInfoKHR',
    }
    _includes_ = set()
    _included_in_ = {
        'VkVideoEncodeRateControlInfoKHR',
    }
    _input_of_ = set()
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'averageBitrate': 'average_bitrate',
        'maxBitrate': 'max_bitrate',
        'frameRateNumerator': 'frame_rate_numerator',
        'frameRateDenominator': 'frame_rate_denominator',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_encode_queue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_RATE_CONTROL_LAYER_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_ENCODE_RATE_CONTROL_LAYER_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkVideoEncodeRateControlLayerInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'averageBitrate': ctypes.c_uint64,
    'maxBitrate': ctypes.c_uint64,
    'frameRateNumerator': ctypes.c_uint32,
    'frameRateDenominator': ctypes.c_uint32,
}
