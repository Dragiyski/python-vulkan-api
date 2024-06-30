from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceRobustness2PropertiesEXT'
_member_list_ = ['sType', 'pNext', 'robustStorageBufferAccessSizeAlignment', 'robustUniformBufferAccessSizeAlignment']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ROBUSTNESS_2_PROPERTIES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'robustStorageBufferAccessSizeAlignment': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'robustUniformBufferAccessSizeAlignment': {
        'type': CIntType('c_uint64'),
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
