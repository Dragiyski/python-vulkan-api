from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeH265QualityLevelPropertiesKHR'
_member_list_ = ['sType', 'pNext', 'preferredRateControlFlags', 'preferredGopFrameCount', 'preferredIdrPeriod', 'preferredConsecutiveBFrameCount', 'preferredSubLayerCount', 'preferredConstantQp', 'preferredMaxL0ReferenceCount', 'preferredMaxL1ReferenceCount']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_QUALITY_LEVEL_PROPERTIES_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'preferredRateControlFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoEncodeH265RateControlFlagsKHR',
        'enum': 'VkVideoEncodeH265RateControlFlagsKHR',
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
    'preferredSubLayerCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'preferredConstantQp': {
        'type': CComplexType('VkVideoEncodeH265QpKHR'),
        'type_name': 'VkVideoEncodeH265QpKHR',
        'structure': 'VkVideoEncodeH265QpKHR',
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
}
_extends_ = {
    'VkVideoEncodeQualityLevelPropertiesKHR',
}
_extended_by_ = set()
_includes_ = {
    'VkVideoEncodeH265QpKHR',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
