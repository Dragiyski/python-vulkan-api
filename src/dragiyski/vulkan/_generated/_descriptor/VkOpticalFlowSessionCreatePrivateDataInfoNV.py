from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkOpticalFlowSessionCreatePrivateDataInfoNV'
_member_list_ = ['sType', 'pNext', 'id', 'size', 'pPrivateData']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_OPTICAL_FLOW_SESSION_CREATE_PRIVATE_DATA_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'id': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'size': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pPrivateData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = {
    'VkOpticalFlowSessionCreateInfoNV',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
