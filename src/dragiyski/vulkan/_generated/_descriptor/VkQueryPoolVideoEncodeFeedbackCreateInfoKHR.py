from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkQueryPoolVideoEncodeFeedbackCreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'encodeFeedbackFlags']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_QUERY_POOL_VIDEO_ENCODE_FEEDBACK_CREATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'encodeFeedbackFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoEncodeFeedbackFlagsKHR',
        'enum': 'VkVideoEncodeFeedbackFlagsKHR',
        'is_string': False,
    },
}
_extends_ = {
    'VkQueryPoolCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
