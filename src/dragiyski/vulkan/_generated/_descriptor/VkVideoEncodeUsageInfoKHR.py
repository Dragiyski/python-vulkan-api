from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeUsageInfoKHR'
_member_list_ = ['sType', 'pNext', 'videoUsageHints', 'videoContentHints', 'tuningMode']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_USAGE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'videoUsageHints': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoEncodeUsageFlagsKHR',
        'enum': 'VkVideoEncodeUsageFlagsKHR',
        'is_string': False,
    },
    'videoContentHints': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoEncodeContentFlagsKHR',
        'enum': 'VkVideoEncodeContentFlagsKHR',
        'is_string': False,
    },
    'tuningMode': {
        'type': CIntType('c_int'),
        'type_name': 'VkVideoEncodeTuningModeKHR',
        'enum': 'VkVideoEncodeTuningModeKHR',
        'is_string': False,
    },
}
_extends_ = {
    'VkQueryPoolCreateInfo',
    'VkVideoProfileInfoKHR',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
