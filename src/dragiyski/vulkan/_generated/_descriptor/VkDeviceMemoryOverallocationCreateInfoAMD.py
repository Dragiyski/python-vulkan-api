from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDeviceMemoryOverallocationCreateInfoAMD'
_member_list_ = ['sType', 'pNext', 'overallocationBehavior']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DEVICE_MEMORY_OVERALLOCATION_CREATE_INFO_AMD',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'overallocationBehavior': {
        'type': CIntType('c_int'),
        'type_name': 'VkMemoryOverallocationBehaviorAMD',
        'enum': 'VkMemoryOverallocationBehaviorAMD',
        'is_string': False,
    },
}
_extends_ = {
    'VkDeviceCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
