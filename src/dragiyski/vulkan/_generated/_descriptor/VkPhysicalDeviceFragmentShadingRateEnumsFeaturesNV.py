from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceFragmentShadingRateEnumsFeaturesNV'
_member_list_ = ['sType', 'pNext', 'fragmentShadingRateEnums', 'supersampleFragmentShadingRates', 'noInvocationFragmentShadingRates']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FRAGMENT_SHADING_RATE_ENUMS_FEATURES_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'fragmentShadingRateEnums': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'supersampleFragmentShadingRates': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'noInvocationFragmentShadingRates': {
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
