from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkExternalMemoryAcquireUnmodifiedEXT'
_member_list_ = ['sType', 'pNext', 'acquireUnmodifiedMemory']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_EXTERNAL_MEMORY_ACQUIRE_UNMODIFIED_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'acquireUnmodifiedMemory': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkBufferMemoryBarrier',
    'VkBufferMemoryBarrier2',
    'VkImageMemoryBarrier',
    'VkImageMemoryBarrier2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
