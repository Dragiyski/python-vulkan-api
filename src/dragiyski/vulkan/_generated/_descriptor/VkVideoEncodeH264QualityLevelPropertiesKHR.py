from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeH264QualityLevelPropertiesKHR'
_member_list_ = ['sType', 'pNext', 'preferredRateControlFlags', 'preferredGopFrameCount', 'preferredIdrPeriod', 'preferredConsecutiveBFrameCount', 'preferredTemporalLayerCount', 'preferredConstantQp', 'preferredMaxL0ReferenceCount', 'preferredMaxL1ReferenceCount', 'preferredStdEntropyCodingModeFlag']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_QUALITY_LEVEL_PROPERTIES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'preferredRateControlFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoEncodeH264RateControlFlagsKHR',
        'enum': 'VkVideoEncodeH264RateControlFlagsKHR',
        'is_string': False,
    },
    'preferredGopFrameCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'preferredIdrPeriod': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'preferredConsecutiveBFrameCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'preferredTemporalLayerCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'preferredConstantQp': {
        'type': CComplexType('VkVideoEncodeH264QpKHR'),
        'type_name': 'VkVideoEncodeH264QpKHR',
        'structure': 'VkVideoEncodeH264QpKHR',
        'is_string': False,
    },
    'preferredMaxL0ReferenceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'preferredMaxL1ReferenceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'preferredStdEntropyCodingModeFlag': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
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
