from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPipelineShaderStageModuleIdentifierCreateInfoEXT'
_member_list_ = ['sType', 'pNext', 'identifierSize', 'pIdentifier']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PIPELINE_SHADER_STAGE_MODULE_IDENTIFIER_CREATE_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'identifierSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pIdentifier': {
        'type': CPointerType(CIntType('c_uint8')),
        'length': [['identifierSize']],
        'is_string': False,
    },
}
_extends_ = {
    'VkPipelineShaderStageCreateInfo',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
