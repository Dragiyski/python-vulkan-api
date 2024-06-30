from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceSubgroupProperties'
_member_list_ = ['sType', 'pNext', 'subgroupSize', 'supportedStages', 'supportedOperations', 'quadOperationsInAllStages']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SUBGROUP_PROPERTIES',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'subgroupSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'supportedStages': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkShaderStageFlags',
        'enum': 'VkShaderStageFlags',
        'is_string': False,
    },
    'supportedOperations': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkSubgroupFeatureFlags',
        'enum': 'VkSubgroupFeatureFlags',
        'is_string': False,
    },
    'quadOperationsInAllStages': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
