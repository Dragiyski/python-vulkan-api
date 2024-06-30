from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoEncodeH264SessionParametersGetInfoKHR'
_member_list_ = ['sType', 'pNext', 'writeStdSPS', 'writeStdPPS', 'stdSPSId', 'stdPPSId']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_ENCODE_H264_SESSION_PARAMETERS_GET_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'writeStdSPS': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'writeStdPPS': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'stdSPSId': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'stdPPSId': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoEncodeSessionParametersGetInfoKHR',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
