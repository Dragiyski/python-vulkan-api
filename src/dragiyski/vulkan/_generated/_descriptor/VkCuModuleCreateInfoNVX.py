from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkCuModuleCreateInfoNVX'
_member_list_ = ['sType', 'pNext', 'dataSize', 'pData']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_CU_MODULE_CREATE_INFO_NVX',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'dataSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'pData': {
        'type': CIntType('c_void_p'),
        'length': [['dataSize']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCreateCuModuleNVX',
}
_output_of_ = set()
