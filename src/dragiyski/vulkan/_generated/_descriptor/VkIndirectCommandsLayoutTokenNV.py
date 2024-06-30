from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkIndirectCommandsLayoutTokenNV'
_member_list_ = ['sType', 'pNext', 'tokenType', 'stream', 'offset', 'vertexBindingUnit', 'vertexDynamicStride', 'pushconstantPipelineLayout', 'pushconstantShaderStageFlags', 'pushconstantOffset', 'pushconstantSize', 'indirectStateFlags', 'indexTypeCount', 'pIndexTypes', 'pIndexTypeValues']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_INDIRECT_COMMANDS_LAYOUT_TOKEN_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'tokenType': {
        'type': CIntType('c_int'),
        'type_name': 'VkIndirectCommandsTokenTypeNV',
        'enum': 'VkIndirectCommandsTokenTypeNV',
        'is_string': False,
    },
    'stream': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'offset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'vertexBindingUnit': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'vertexDynamicStride': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pushconstantPipelineLayout': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pushconstantShaderStageFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkShaderStageFlags',
        'enum': 'VkShaderStageFlags',
        'is_string': False,
    },
    'pushconstantOffset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pushconstantSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'indirectStateFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkIndirectStateFlagsNV',
        'enum': 'VkIndirectStateFlagsNV',
        'is_string': False,
    },
    'indexTypeCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pIndexTypes': {
        'type': CPointerType(CIntType('c_int')),
        'type_name': 'VkIndexType',
        'enum': 'VkIndexType',
        'length': [['indexTypeCount']],
        'is_string': False,
    },
    'pIndexTypeValues': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['indexTypeCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = {
    'VkIndirectCommandsLayoutCreateInfoNV',
}
_input_of_ = set()
_output_of_ = set()
