from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkOpticalFlowExecuteInfoNV'
_member_list_ = ['sType', 'pNext', 'flags', 'regionCount', 'pRegions']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_OPTICAL_FLOW_EXECUTE_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkOpticalFlowExecuteFlagsNV',
        'enum': 'VkOpticalFlowExecuteFlagsNV',
        'is_string': False,
    },
    'regionCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pRegions': {
        'type': CPointerType(CComplexType('VkRect2D')),
        'type_name': 'VkRect2D',
        'structure': 'VkRect2D',
        'length': [['regionCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkRect2D',
}
_included_in_ = set()
_input_of_ = {
    'vkCmdOpticalFlowExecuteNV',
}
_output_of_ = set()
