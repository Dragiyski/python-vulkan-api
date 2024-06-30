from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkValidationFeaturesEXT'
_member_list_ = ['sType', 'pNext', 'enabledValidationFeatureCount', 'pEnabledValidationFeatures', 'disabledValidationFeatureCount', 'pDisabledValidationFeatures']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_VALIDATION_FEATURES_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'enabledValidationFeatureCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pEnabledValidationFeatures': {
        'type': CPointerType(CIntType('c_int')),
        'type_name': 'VkValidationFeatureEnableEXT',
        'enum': 'VkValidationFeatureEnableEXT',
        'length': [['enabledValidationFeatureCount']],
        'is_string': False,
    },
    'disabledValidationFeatureCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDisabledValidationFeatures': {
        'type': CPointerType(CIntType('c_int')),
        'type_name': 'VkValidationFeatureDisableEXT',
        'enum': 'VkValidationFeatureDisableEXT',
        'length': [['disabledValidationFeatureCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkInstanceCreateInfo',
    'VkShaderCreateInfoEXT',
    'VkShaderModuleCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
