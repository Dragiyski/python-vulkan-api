from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoDecodeH265ProfileInfoKHR'
_member_list_ = ['sType', 'pNext', 'stdProfileIdc']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_PROFILE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'stdProfileIdc': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH265ProfileIdc',
        'enum': 'StdVideoH265ProfileIdc',
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
