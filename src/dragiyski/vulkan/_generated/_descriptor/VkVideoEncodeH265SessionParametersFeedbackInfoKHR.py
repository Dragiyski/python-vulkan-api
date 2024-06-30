from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeH265SessionParametersFeedbackInfoKHR'
_member_list_ = ['sType', 'pNext', 'hasStdVPSOverrides', 'hasStdSPSOverrides', 'hasStdPPSOverrides']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H265_SESSION_PARAMETERS_FEEDBACK_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'hasStdVPSOverrides': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'hasStdSPSOverrides': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'hasStdPPSOverrides': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoEncodeSessionParametersFeedbackInfoKHR',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
