from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkQueryLowLatencySupportNV'
_member_list_ = ['sType', 'pNext', 'pQueriedLowLatencyData']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_QUERY_LOW_LATENCY_SUPPORT_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pQueriedLowLatencyData': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
}
_extends_ = {
    'VkSemaphoreCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
