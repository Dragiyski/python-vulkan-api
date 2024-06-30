from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceMemoryBudgetPropertiesEXT'
_member_list_ = ['sType', 'pNext', 'heapBudget', 'heapUsage']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MEMORY_BUDGET_PROPERTIES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'heapBudget': {
        'type': CArrayType(CIntType('c_uint64'), 16),
        'is_string': False,
    },
    'heapUsage': {
        'type': CArrayType(CIntType('c_uint64'), 16),
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceMemoryProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
