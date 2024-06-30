from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImportSemaphoreWin32HandleInfoKHR'
_member_list_ = ['sType', 'pNext', 'semaphore', 'flags', 'handleType', 'handle', 'name']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMPORT_SEMAPHORE_WIN32_HANDLE_INFO_KHR',
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
    'handle': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'name': {
        'type': CWideStringType('c_wchar_p'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkImportSemaphoreWin32HandleKHR',
}
_output_of_ = set()
