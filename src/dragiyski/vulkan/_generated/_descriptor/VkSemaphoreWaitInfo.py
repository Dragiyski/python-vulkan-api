from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSemaphoreWaitInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'semaphoreCount', 'pSemaphores', 'pValues']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SEMAPHORE_WAIT_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSemaphoreWaitFlags',
        'enum': 'VkSemaphoreWaitFlags',
        'is_string': False,
    },
    'semaphoreCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pSemaphores': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['semaphoreCount']],
        'is_string': False,
    },
    'pValues': {
        'type': CPointerType(CIntType('c_uint64')),
        'length': [['semaphoreCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkWaitSemaphores',
}
_output_of_ = set()
