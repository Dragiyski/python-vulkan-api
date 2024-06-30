from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkAcquireProfilingLockInfoKHR'
_member_list_ = ['sType', 'pNext', 'flags', 'timeout']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_ACQUIRE_PROFILING_LOCK_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkAcquireProfilingLockFlagsKHR',
        'enum': 'VkAcquireProfilingLockFlagsKHR',
        'is_string': False,
    },
    'timeout': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkAcquireProfilingLockKHR',
}
_output_of_ = set()
