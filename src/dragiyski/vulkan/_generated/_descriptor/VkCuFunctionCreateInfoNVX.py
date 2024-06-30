from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCuFunctionCreateInfoNVX'
_member_list_ = ['sType', 'pNext', 'module', 'pName']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_CU_FUNCTION_CREATE_INFO_NVX',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'module': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pName': {
        'type': CStringType('c_char_p'),
        'length': [],
        'is_string': True,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCreateCuFunctionNVX',
}
_output_of_ = set()
