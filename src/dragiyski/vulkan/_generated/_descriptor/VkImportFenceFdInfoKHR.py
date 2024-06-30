from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImportFenceFdInfoKHR'
_member_list_ = ['sType', 'pNext', 'fence', 'flags', 'handleType', 'fd']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMPORT_FENCE_FD_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'fence': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkFenceImportFlags',
        'enum': 'VkFenceImportFlags',
        'is_string': False,
    },
    'handleType': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkExternalFenceHandleTypeFlagBits',
        'is_string': False,
    },
    'fd': {
        'type': CIntType('c_int'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkImportFenceFdKHR',
}
_output_of_ = set()
