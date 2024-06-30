from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkExportMemoryWin32HandleInfoKHR'
_member_list_ = ['sType', 'pNext', 'pAttributes', 'dwAccess', 'name']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_EXPORT_MEMORY_WIN32_HANDLE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pAttributes': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'dwAccess': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'name': {
        'type': CWideStringType('c_wchar_p'),
        'is_string': False,
    },
}
_extends_ = {
    'VkMemoryAllocateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
