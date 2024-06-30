from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSemaphoreTypeCreateInfo'
_member_list_ = ['sType', 'pNext', 'semaphoreType', 'initialValue']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SEMAPHORE_TYPE_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'semaphoreType': {
        'type': CIntType('c_int'),
        'type_name': 'VkSemaphoreType',
        'enum': 'VkSemaphoreType',
        'is_string': False,
    },
    'initialValue': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceExternalSemaphoreInfo',
    'VkSemaphoreCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
