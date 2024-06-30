from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineShaderStageRequiredSubgroupSizeCreateInfo'
_member_list_ = ['sType', 'pNext', 'requiredSubgroupSize']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_REQUIRED_SUBGROUP_SIZE_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'requiredSubgroupSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkPipelineShaderStageCreateInfo',
    'VkShaderCreateInfoEXT',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
