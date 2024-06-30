from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImportFenceWin32HandleInfoKHR'
_member_list_ = ['sType', 'pNext', 'fence', 'flags', 'handleType', 'handle', 'name']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMPORT_FENCE_WIN32_HANDLE_INFO_KHR',
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
    'vkImportFenceWin32HandleKHR',
}
_output_of_ = set()
