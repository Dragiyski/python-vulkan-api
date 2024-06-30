from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeSessionParametersGetInfoKHR'
_member_list_ = ['sType', 'pNext', 'videoSessionParameters']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_SESSION_PARAMETERS_GET_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'videoSessionParameters': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkVideoEncodeH264SessionParametersGetInfoKHR',
    'VkVideoEncodeH265SessionParametersGetInfoKHR',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetEncodedVideoSessionParametersKHR',
}
_output_of_ = set()
