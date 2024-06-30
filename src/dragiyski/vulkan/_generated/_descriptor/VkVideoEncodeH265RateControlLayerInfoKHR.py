from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeH265RateControlLayerInfoKHR'
_member_list_ = ['sType', 'pNext', 'useMinQp', 'minQp', 'useMaxQp', 'maxQp', 'useMaxFrameSize', 'maxFrameSize']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_RATE_CONTROL_LAYER_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'useMinQp': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'minQp': {
        'type': CComplexType('VkVideoEncodeH265QpKHR'),
        'type_name': 'VkVideoEncodeH265QpKHR',
        'structure': 'VkVideoEncodeH265QpKHR',
        'is_string': False,
    },
    'useMaxQp': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxQp': {
        'type': CComplexType('VkVideoEncodeH265QpKHR'),
        'type_name': 'VkVideoEncodeH265QpKHR',
        'structure': 'VkVideoEncodeH265QpKHR',
        'is_string': False,
    },
    'useMaxFrameSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxFrameSize': {
        'type': CComplexType('VkVideoEncodeH265FrameSizeKHR'),
        'type_name': 'VkVideoEncodeH265FrameSizeKHR',
        'structure': 'VkVideoEncodeH265FrameSizeKHR',
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoEncodeRateControlLayerInfoKHR',
}
_extended_by_ = set()
_includes_ = {
    'VkVideoEncodeH265FrameSizeKHR',
    'VkVideoEncodeH265QpKHR',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
