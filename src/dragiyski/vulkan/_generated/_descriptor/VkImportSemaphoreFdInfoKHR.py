from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImportSemaphoreFdInfoKHR'
_member_list_ = ['sType', 'pNext', 'semaphore', 'flags', 'handleType', 'fd']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMPORT_SEMAPHORE_FD_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'semaphore': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSemaphoreImportFlags',
        'enum': 'VkSemaphoreImportFlags',
        'is_string': False,
    },
    'handleType': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkExternalSemaphoreHandleTypeFlagBits',
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
    'vkImportSemaphoreFdKHR',
}
_output_of_ = set()
