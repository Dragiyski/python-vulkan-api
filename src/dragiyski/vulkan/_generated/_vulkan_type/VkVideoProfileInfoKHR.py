import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('videoCodecOperation', ctypes.c_uint32),
        ('chromaSubsampling', ctypes.c_uint32),
        ('lumaBitDepth', ctypes.c_uint32),
        ('chromaBitDepth', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkQueryPoolCreateInfo',
    },
    'extended_by': {
        'VkVideoDecodeAV1ProfileInfoKHR',
        'VkVideoDecodeH264ProfileInfoKHR',
        'VkVideoDecodeH265ProfileInfoKHR',
        'VkVideoDecodeUsageInfoKHR',
        'VkVideoEncodeH264ProfileInfoKHR',
        'VkVideoEncodeH265ProfileInfoKHR',
        'VkVideoEncodeUsageInfoKHR',
    },
    'includes': set(),
    'included_in': {
        'VkPhysicalDeviceVideoEncodeQualityLevelInfoKHR',
        'VkVideoProfileListInfoKHR',
        'VkVideoSessionCreateInfoKHR',
    },
    'input_of': {
        'vkGetPhysicalDeviceVideoCapabilitiesKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_VIDEO_PROFILE_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'videoCodecOperation': {'python_name': ['video', 'codec', 'operation'], 'type': 'VkVideoCodecOperationFlagBitsKHR'},
        'chromaSubsampling': {'python_name': ['chroma', 'subsampling'], 'type': 'VkVideoChromaSubsamplingFlagsKHR'},
        'lumaBitDepth': {'python_name': ['luma', 'bit', 'depth'], 'type': 'VkVideoComponentBitDepthFlagsKHR'},
        'chromaBitDepth': {'python_name': ['chroma', 'bit', 'depth'], 'type': 'VkVideoComponentBitDepthFlagsKHR'},
    }
}
