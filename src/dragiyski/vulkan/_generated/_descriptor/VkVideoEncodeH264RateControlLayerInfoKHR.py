from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeH264RateControlLayerInfoKHR'
_member_list_ = ['sType', 'pNext', 'useMinQp', 'minQp', 'useMaxQp', 'maxQp', 'useMaxFrameSize', 'maxFrameSize']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_RATE_CONTROL_LAYER_INFO_KHR',
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
        'type': CComplexType('VkVideoEncodeH264QpKHR'),
        'type_name': 'VkVideoEncodeH264QpKHR',
        'structure': 'VkVideoEncodeH264QpKHR',
        'is_string': False,
    },
    'useMaxQp': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxQp': {
        'type': CComplexType('VkVideoEncodeH264QpKHR'),
        'type_name': 'VkVideoEncodeH264QpKHR',
        'structure': 'VkVideoEncodeH264QpKHR',
        'is_string': False,
    },
    'useMaxFrameSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxFrameSize': {
        'type': CComplexType('VkVideoEncodeH264FrameSizeKHR'),
        'type_name': 'VkVideoEncodeH264FrameSizeKHR',
        'structure': 'VkVideoEncodeH264FrameSizeKHR',
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoEncodeRateControlLayerInfoKHR',
}
_extended_by_ = set()
_includes_ = {
    'VkVideoEncodeH264FrameSizeKHR',
    'VkVideoEncodeH264QpKHR',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
