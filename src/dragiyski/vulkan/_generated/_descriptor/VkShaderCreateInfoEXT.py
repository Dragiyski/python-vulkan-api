from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkShaderCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'flags', 'stage', 'nextStage', 'codeType', 'codeSize', 'pCode', 'pName', 'setLayoutCount', 'pSetLayouts', 'pushConstantRangeCount', 'pPushConstantRanges', 'pSpecializationInfo']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SHADER_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkShaderCreateFlagsEXT',
        'enum': 'VkShaderCreateFlagsEXT',
        'is_string': False,
    },
    'stage': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkShaderStageFlagBits',
        'is_string': False,
    },
    'nextStage': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkShaderStageFlags',
        'enum': 'VkShaderStageFlags',
        'is_string': False,
    },
    'codeType': {
        'type': CIntType('c_int'),
        'type_name': 'VkShaderCodeTypeEXT',
        'enum': 'VkShaderCodeTypeEXT',
        'is_string': False,
    },
    'codeSize': {
        'type': CIntType('c_size_t'),
        'is_string': False,
    },
    'pCode': {
        'type': CIntType('c_void_p'),
        'length': [['codeSize']],
        'is_string': False,
    },
    'pName': {
        'type': CStringType('c_char_p'),
        'length': [],
        'is_string': True,
    },
    'setLayoutCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pSetLayouts': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['setLayoutCount']],
        'is_string': False,
    },
    'pushConstantRangeCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pPushConstantRanges': {
        'type': CPointerType(CComplexType('VkPushConstantRange')),
        'type_name': 'VkPushConstantRange',
        'structure': 'VkPushConstantRange',
        'length': [['pushConstantRangeCount']],
        'is_string': False,
    },
    'pSpecializationInfo': {
        'type': CPointerType(CComplexType('VkSpecializationInfo')),
        'type_name': 'VkSpecializationInfo',
        'structure': 'VkSpecializationInfo',
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkPipelineShaderStageRequiredSubgroupSizeCreateInfo',
    'VkValidationFeaturesEXT',
}
_includes_ = {
    'VkPushConstantRange',
    'VkSpecializationInfo',
}
_included_in_ = set()
_input_of_ = {
    'vkCreateShadersEXT',
}
_output_of_ = set()
