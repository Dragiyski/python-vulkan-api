from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkShaderModuleCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'codeSize', 'pCode']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SHADER_MODULE_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkShaderModuleCreateFlags',
        'enum': 'VkShaderModuleCreateFlags',
        'is_string': False,
    },
    'codeSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'pCode': {
        'type': CPointerType(CIntType('c_uint32')),
        'is_string': False,
    },
}
_extends_ = {
    'VkPipelineShaderStageCreateInfo',
}
_extended_by_ = {
    'VkShaderModuleValidationCacheCreateInfoEXT',
    'VkValidationFeaturesEXT',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCreateShaderModule',
    'vkGetShaderModuleCreateInfoIdentifierEXT',
}
_output_of_ = set()
