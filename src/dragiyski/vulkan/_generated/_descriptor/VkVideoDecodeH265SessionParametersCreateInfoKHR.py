from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkVideoDecodeH265SessionParametersCreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'maxStdVPSCount', 'maxStdSPSCount', 'maxStdPPSCount', 'pParametersAddInfo']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VIDEO_DECODE_H265_SESSION_PARAMETERS_CREATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'maxStdVPSCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxStdSPSCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxStdPPSCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pParametersAddInfo': {
        'type': CPointerType(CComplexType('VkVideoDecodeH265SessionParametersAddInfoKHR')),
        'type_name': 'VkVideoDecodeH265SessionParametersAddInfoKHR',
        'structure': 'VkVideoDecodeH265SessionParametersAddInfoKHR',
        'is_string': False,
    },
}
_extends_ = {
    'VkVideoSessionParametersCreateInfoKHR',
}
_extended_by_ = set()
_includes_ = {
    'VkVideoDecodeH265SessionParametersAddInfoKHR',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
