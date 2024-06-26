import ctypes

class VkVideoProfileInfoKHR(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('videoCodecOperation', ctypes.c_uint32),
        ('chromaSubsampling', ctypes.c_uint32),
        ('lumaBitDepth', ctypes.c_uint32),
        ('chromaBitDepth', ctypes.c_uint32),
    ]

    _init_ = []
    _extends_ = {
        'VkQueryPoolCreateInfo',
    }
    _extended_by_ = {
        'VkVideoDecodeAV1ProfileInfoKHR',
        'VkVideoDecodeH264ProfileInfoKHR',
        'VkVideoDecodeH265ProfileInfoKHR',
        'VkVideoDecodeUsageInfoKHR',
        'VkVideoEncodeH264ProfileInfoKHR',
        'VkVideoEncodeH265ProfileInfoKHR',
        'VkVideoEncodeUsageInfoKHR',
    }
    _includes_ = set()
    _included_in_ = {
        'VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR',
        'VkVideoProfileListInfoKHR',
        'VkVideoSessionCreateInfoKHR',
    }
    _input_of_ = {
        'vkGetPhysicalDeviceVideoCapabilitiesKHR',
    }
    _output_of_ = set()
    _python_name_ = {
        'sType': 'type',
        'pNext': 'next',
        'videoCodecOperation': 'video_codec_operation',
        'chromaSubsampling': 'chroma_subsampling',
        'lumaBitDepth': 'luma_bit_depth',
        'chromaBitDepth': 'chroma_bit_depth',
    }
    _vk_versions_ = set()
    _vk_extensions_ = {
        'VK_KHR_video_queue',
    }
    _vk_enum_ = {
        'sType': 'VkStructureType',
        'chromaSubsampling': 'VkVideoChromaSubsamplingFlagsKHR',
        'lumaBitDepth': 'VkVideoComponentBitDepthFlagsKHR',
        'chromaBitDepth': 'VkVideoComponentBitDepthFlagsKHR',
    }
    _vk_structure_type_ = 'VK_STRUCTURE_TYPE_VIDEO_PROFILE_INFO_KHR'

    def __init__(self, *args, **kwargs):
        super().__init__()
        from .._vulkan_enum.VkStructureType import VkStructureType
        self.sType = VkStructureType.VK_STRUCTURE_TYPE_VIDEO_PROFILE_INFO_KHR
        for function in self._init_:
            function(self, *args, **kwargs)

VkVideoProfileInfoKHR._type_ = {
    'sType': ctypes.c_int,
    'pNext': ctypes.c_void_p,
    'videoCodecOperation': ctypes.c_uint32,
    'chromaSubsampling': ctypes.c_uint32,
    'lumaBitDepth': ctypes.c_uint32,
    'chromaBitDepth': ctypes.c_uint32,
}
