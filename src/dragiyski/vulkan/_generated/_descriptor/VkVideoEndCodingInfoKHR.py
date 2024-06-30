from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEndCodingInfoKHR'
_member_list_ = ['sType', 'pNext', 'flags']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_END_CODING_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoEndCodingFlagsKHR',
        'enum': 'VkVideoEndCodingFlagsKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCmdEndVideoCodingKHR',
}
_output_of_ = set()
