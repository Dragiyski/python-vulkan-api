from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineShaderStageNodeCreateInfoAMDX'
_member_list_ = ['sType', 'pNext', 'pName', 'index']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_NODE_CREATE_INFO_AMDX',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pName': {
        'type': CStringType('c_char_p'),
        'length': [],
        'is_string': True,
    },
    'index': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkPipelineShaderStageCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetExecutionGraphPipelineNodeIndexAMDX',
}
_output_of_ = set()
