from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPerformanceConfigurationAcquireInfoINTEL'
_member_list_ = ['sType', 'pNext', 'type']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PERFORMANCE_CONFIGURATION_ACQUIRE_INFO_INTEL',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'type': {
        'type': CIntType('c_int'),
        'type_name': 'VkPerformanceConfigurationTypeINTEL',
        'enum': 'VkPerformanceConfigurationTypeINTEL',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkAcquirePerformanceConfigurationINTEL',
}
_output_of_ = set()
