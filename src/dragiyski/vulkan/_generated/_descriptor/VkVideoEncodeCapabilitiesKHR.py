from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeCapabilitiesKHR'
_member_list_ = ['sType', 'pNext', 'flags', 'rateControlModes', 'maxRateControlLayers', 'maxBitrate', 'maxQualityLevels', 'encodeInputPictureGranularity', 'supportedEncodeFeedbackFlags']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_CAPABILITIES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoEncodeCapabilityFlagsKHR',
        'enum': 'VkVideoEncodeCapabilityFlagsKHR',
        'is_string': False,
    },
    'rateControlModes': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoEncodeRateControlModeFlagsKHR',
        'enum': 'VkVideoEncodeRateControlModeFlagsKHR',
        'is_string': False,
    },
    'maxRateControlLayers': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxBitrate': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'maxQualityLevels': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'encodeInputPictureGranularity': {
        'type': CComplexType('VkExtent2D'),
        'type_name': 'VkExtent2D',
        'structure': 'VkExtent2D',
        'is_string': False,
    },
    'supportedEncodeFeedbackFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoEncodeFeedbackFlagsKHR',
        'enum': 'VkVideoEncodeFeedbackFlagsKHR',
        'is_string': False,
    },
}
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
