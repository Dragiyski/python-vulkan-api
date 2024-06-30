from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkGraphicsPipelineShaderGroupsCreateInfoNV'
_member_list_ = ['sType', 'pNext', 'groupCount', 'pGroups', 'pipelineCount', 'pPipelines']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_GRAPHICS_PIPELINE_SHADER_GROUPS_CREATE_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'groupCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pGroups': {
        'type': CPointerType(CComplexType('VkGraphicsShaderGroupCreateInfoNV')),
        'type_name': 'VkGraphicsShaderGroupCreateInfoNV',
        'structure': 'VkGraphicsShaderGroupCreateInfoNV',
        'length': [['groupCount']],
        'is_string': False,
    },
    'pipelineCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pPipelines': {
        'type': CPointerType(CIntType('c_void_p')),
        'length': [['pipelineCount']],
        'is_string': False,
    },
}
_extends_ = {
    'VkGraphicsPipelineCreateInfo',
}
_extended_by_ = set()
_includes_ = {
    'VkGraphicsShaderGroupCreateInfoNV',
}
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
