from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoSessionParametersCreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'flags', 'videoSessionParametersTemplate', 'videoSession']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_SESSION_PARAMETERS_CREATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoSessionParametersCreateFlagsKHR',
        'enum': 'VkVideoSessionParametersCreateFlagsKHR',
        'is_string': False,
    },
    'videoSessionParametersTemplate': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'videoSession': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkVideoDecodeAV1SessionParametersCreateInfoKHR',
    'VkVideoDecodeH264SessionParametersCreateInfoKHR',
    'VkVideoDecodeH265SessionParametersCreateInfoKHR',
    'VkVideoEncodeH264SessionParametersCreateInfoKHR',
    'VkVideoEncodeH265SessionParametersCreateInfoKHR',
    'VkVideoEncodeQualityLevelInfoKHR',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCreateVideoSessionParametersKHR',
}
_output_of_ = set()
