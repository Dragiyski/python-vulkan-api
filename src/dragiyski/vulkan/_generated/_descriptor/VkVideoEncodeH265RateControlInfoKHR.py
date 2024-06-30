from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeH265RateControlInfoKHR'
_member_list_ = ['sType', 'pNext', 'flags', 'gopFrameCount', 'idrPeriod', 'consecutiveBFrameCount', 'subLayerCount']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_RATE_CONTROL_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoEncodeH265RateControlFlagsKHR',
        'enum': 'VkVideoEncodeH265RateControlFlagsKHR',
        'is_string': False,
    },
    'gopFrameCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'idrPeriod': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'consecutiveBFrameCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'subLayerCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoBeginCodingInfoKHR',
    'VkVideoCodingControlInfoKHR',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
