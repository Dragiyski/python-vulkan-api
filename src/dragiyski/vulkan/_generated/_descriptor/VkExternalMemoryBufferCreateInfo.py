from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkExternalMemoryBufferCreateInfo'
_member_list_ = ['sType', 'pNext', 'handleTypes']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_BUFFER_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'handleTypes': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkExternalMemoryHandleTypeFlags',
        'enum': 'VkExternalMemoryHandleTypeFlags',
        'is_string': False,
    },
}
_extends_ = {
    'VkBufferCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
