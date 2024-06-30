from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoProfileInfoKHR'
_member_list_ = ['sType', 'pNext', 'videoCodecOperation', 'chromaSubsampling', 'lumaBitDepth', 'chromaBitDepth']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_PROFILE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'videoCodecOperation': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoCodecOperationFlagBitsKHR',
        'is_string': False,
    },
    'chromaSubsampling': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoChromaSubsamplingFlagsKHR',
        'enum': 'VkVideoChromaSubsamplingFlagsKHR',
        'is_string': False,
    },
    'lumaBitDepth': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoComponentBitDepthFlagsKHR',
        'enum': 'VkVideoComponentBitDepthFlagsKHR',
        'is_string': False,
    },
    'chromaBitDepth': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoComponentBitDepthFlagsKHR',
        'enum': 'VkVideoComponentBitDepthFlagsKHR',
        'is_string': False,
    },
}
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
