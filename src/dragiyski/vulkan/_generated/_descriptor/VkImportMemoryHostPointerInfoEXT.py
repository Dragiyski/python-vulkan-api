from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkImportMemoryHostPointerInfoEXT'
_member_list_ = ['sType', 'pNext', 'handleType', 'pHostPointer']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_IMPORT_MEMORY_HOST_POINTER_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'handleType': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkExternalMemoryHandleTypeFlagBits',
        'is_string': False,
    },
    'pHostPointer': {
        'type': CIntType('c_void_p'),
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
