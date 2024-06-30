from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPerformanceCounterDescriptionKHR'
_member_list_ = ['sType', 'pNext', 'flags', 'name', 'category', 'description']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PERFORMANCE_COUNTER_DESCRIPTION_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkPerformanceCounterDescriptionFlagsKHR',
        'enum': 'VkPerformanceCounterDescriptionFlagsKHR',
        'is_string': False,
    },
    'name': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'category': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
    },
    'description': {
        'type': CArrayType(CCharType('c_char'), 256),
        'length': [],
        'is_string': True,
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
