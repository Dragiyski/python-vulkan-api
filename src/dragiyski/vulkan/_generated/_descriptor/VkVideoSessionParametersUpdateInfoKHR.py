from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoSessionParametersUpdateInfoKHR'
_member_list_ = ['sType', 'pNext', 'updateSequenceCount']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_SESSION_PARAMETERS_UPDATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'updateSequenceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkVideoDecodeH264SessionParametersAddInfoKHR',
    'VkVideoDecodeH265SessionParametersAddInfoKHR',
    'VkVideoEncodeH264SessionParametersAddInfoKHR',
    'VkVideoEncodeH265SessionParametersAddInfoKHR',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkUpdateVideoSessionParametersKHR',
}
_output_of_ = set()
