from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkQueryPoolPerformanceQueryCreateInfoINTEL'
_member_list_ = ['sType', 'pNext', 'performanceCountersSampling']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_QUERY_POOL_PERFORMANCE_QUERY_CREATE_INFO_INTEL',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'performanceCountersSampling': {
        'type': CIntType('c_int'),
        'type_name': 'VkQueryPoolSamplingModeINTEL',
        'enum': 'VkQueryPoolSamplingModeINTEL',
        'is_string': False,
    },
}
_extends_ = {
    'VkQueryPoolCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
