from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoDecodeAV1ProfileInfoKHR'
_member_list_ = ['sType', 'pNext', 'stdProfile', 'filmGrainSupport']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_DECODE_AV1_PROFILE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'stdProfile': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoAV1Profile',
        'enum': 'StdVideoAV1Profile',
        'is_string': False,
    },
    'filmGrainSupport': {
        'type': CIntType('c_uint32'),
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
