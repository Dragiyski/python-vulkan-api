from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkTimelineSemaphoreSubmitInfo'
_member_list_ = ['sType', 'pNext', 'waitSemaphoreValueCount', 'pWaitSemaphoreValues', 'signalSemaphoreValueCount', 'pSignalSemaphoreValues']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_TIMELINE_SEMAPHORE_SUBMIT_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'waitSemaphoreValueCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pWaitSemaphoreValues': {
        'type': CPointerType(CIntType('c_uint64')),
        'length': [['waitSemaphoreValueCount']],
        'is_string': False,
    },
    'signalSemaphoreValueCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pSignalSemaphoreValues': {
        'type': CPointerType(CIntType('c_uint64')),
        'length': [['signalSemaphoreValueCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkBindSparseInfo',
    'VkSubmitInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
