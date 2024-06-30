from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoCodingControlInfoKHR'
_member_list_ = ['sType', 'pNext', 'flags']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_CODING_CONTROL_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkVideoCodingControlFlagsKHR',
        'enum': 'VkVideoCodingControlFlagsKHR',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkVideoEncodeH264RateControlInfoKHR',
    'VkVideoEncodeH265RateControlInfoKHR',
    'VkVideoEncodeQualityLevelInfoKHR',
    'VkVideoEncodeRateControlInfoKHR',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCmdControlVideoCodingKHR',
}
_output_of_ = set()
