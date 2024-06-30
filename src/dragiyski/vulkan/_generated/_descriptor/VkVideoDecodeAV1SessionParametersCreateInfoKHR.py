from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoDecodeAV1SessionParametersCreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'pStdSequenceHeader']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_DECODE_AV1_SESSION_PARAMETERS_CREATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pStdSequenceHeader': {
        'type': CPointerType(CComplexType('StdVideoAV1SequenceHeader')),
        'type_name': 'StdVideoAV1SequenceHeader',
        'structure': 'StdVideoAV1SequenceHeader',
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoSessionParametersCreateInfoKHR',
}
_extended_by_ = set()
_includes_ = {
    'StdVideoAV1SequenceHeader',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
