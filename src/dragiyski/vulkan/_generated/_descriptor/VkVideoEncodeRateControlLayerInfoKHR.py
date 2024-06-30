from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeRateControlLayerInfoKHR'
_member_list_ = ['sType', 'pNext', 'averageBitrate', 'maxBitrate', 'frameRateNumerator', 'frameRateDenominator']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_RATE_CONTROL_LAYER_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'averageBitrate': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'maxBitrate': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'frameRateNumerator': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'frameRateDenominator': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
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
