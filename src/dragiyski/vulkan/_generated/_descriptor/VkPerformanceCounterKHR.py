from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPerformanceCounterKHR'
_member_list_ = ['sType', 'pNext', 'unit', 'scope', 'storage', 'uuid']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PERFORMANCE_COUNTER_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'unit': {
        'type': CIntType('c_int'),
        'type_name': 'VkPerformanceCounterUnitKHR',
        'enum': 'VkPerformanceCounterUnitKHR',
        'is_string': False,
    },
    'scope': {
        'type': CIntType('c_int'),
        'type_name': 'VkPerformanceCounterScopeKHR',
        'enum': 'VkPerformanceCounterScopeKHR',
        'is_string': False,
    },
    'storage': {
        'type': CIntType('c_int'),
        'type_name': 'VkPerformanceCounterStorageKHR',
        'enum': 'VkPerformanceCounterStorageKHR',
        'is_string': False,
    },
    'uuid': {
        'type': CArrayType(CIntType('c_uint8'), 16),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = {
    'vkEnumeratePhysicalDeviceQueueFamilyPerformanceQueryCountersKHR',
}
