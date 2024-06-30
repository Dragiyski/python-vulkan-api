from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeSessionParametersFeedbackInfoKHR'
_member_list_ = ['sType', 'pNext', 'hasOverrides']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_SESSION_PARAMETERS_FEEDBACK_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'hasOverrides': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkVideoEncodeH264SessionParametersFeedbackInfoKHR',
    'VkVideoEncodeH265SessionParametersFeedbackInfoKHR',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkGetEncodedVideoSessionParametersKHR',
}
