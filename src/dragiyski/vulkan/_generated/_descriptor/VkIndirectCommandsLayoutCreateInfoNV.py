from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkIndirectCommandsLayoutCreateInfoNV'
_member_list_ = ['sType', 'pNext', 'flags', 'pipelineBindPoint', 'tokenCount', 'pTokens', 'streamCount', 'pStreamStrides']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_INDIRECT_COMMANDS_LAYOUT_CREATE_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkIndirectCommandsLayoutUsageFlagsNV',
        'enum': 'VkIndirectCommandsLayoutUsageFlagsNV',
        'is_string': False,
    },
    'pipelineBindPoint': {
        'type': CIntType('c_int'),
        'type_name': 'VkPipelineBindPoint',
        'enum': 'VkPipelineBindPoint',
        'is_string': False,
    },
    'tokenCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pTokens': {
        'type': CPointerType(CComplexType('VkIndirectCommandsLayoutTokenNV')),
        'type_name': 'VkIndirectCommandsLayoutTokenNV',
        'structure': 'VkIndirectCommandsLayoutTokenNV',
        'length': [['tokenCount']],
        'is_string': False,
    },
    'streamCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pStreamStrides': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['streamCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkIndirectCommandsLayoutTokenNV',
}
_included_in_ = set()
_input_of_ = {
    'vkCreateIndirectCommandsLayoutNV',
}
_output_of_ = set()
