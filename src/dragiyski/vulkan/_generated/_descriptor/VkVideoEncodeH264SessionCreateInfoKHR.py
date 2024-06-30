from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeH264SessionCreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'useMaxLevelIdc', 'maxLevelIdc']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_SESSION_CREATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'useMaxLevelIdc': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxLevelIdc': {
        'type': CIntType('c_int'),
        'type_name': 'StdVideoH264LevelIdc',
        'enum': 'StdVideoH264LevelIdc',
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoSessionCreateInfoKHR',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
