from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkMemoryGetRemoteAddressInfoNV'
_member_list_ = ['sType', 'pNext', 'memory', 'handleType']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_MEMORY_GET_REMOTE_ADDRESS_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'memory': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'handleType': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkExternalMemoryHandleTypeFlagBits',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetMemoryRemoteAddressNV',
}
_output_of_ = set()
