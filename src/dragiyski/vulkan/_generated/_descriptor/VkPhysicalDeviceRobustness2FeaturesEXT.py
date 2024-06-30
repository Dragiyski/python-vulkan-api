from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceRobustness2FeaturesEXT'
_member_list_ = ['sType', 'pNext', 'robustBufferAccess2', 'robustImageAccess2', 'nullDescriptor']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ROBUSTNESS_2_FEATURES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'robustBufferAccess2': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'robustImageAccess2': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'nullDescriptor': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkDeviceCreateInfo',
    'VkPhysicalDeviceFeatures2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
