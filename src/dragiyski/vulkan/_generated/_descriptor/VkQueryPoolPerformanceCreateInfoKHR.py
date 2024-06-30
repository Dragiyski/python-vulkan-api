from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkQueryPoolPerformanceCreateInfoKHR'
_member_list_ = ['sType', 'pNext', 'queueFamilyIndex', 'counterIndexCount', 'pCounterIndices']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_QUERY_POOL_PERFORMANCE_CREATE_INFO_KHR',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'queueFamilyIndex': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'counterIndexCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pCounterIndices': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['counterIndexCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkQueryPoolCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetPhysicalDeviceQueueFamilyPerformanceQueryPassesKHR',
}
_output_of_ = set()
