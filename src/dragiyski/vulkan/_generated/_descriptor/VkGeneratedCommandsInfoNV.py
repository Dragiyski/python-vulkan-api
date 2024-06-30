from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkGeneratedCommandsInfoNV'
_member_list_ = ['sType', 'pNext', 'pipelineBindPoint', 'pipeline', 'indirectCommandsLayout', 'streamCount', 'pStreams', 'sequencesCount', 'preprocessBuffer', 'preprocessOffset', 'preprocessSize', 'sequencesCountBuffer', 'sequencesCountOffset', 'sequencesIndexBuffer', 'sequencesIndexOffset']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_GENERATED_COMMANDS_INFO_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pipelineBindPoint': {
        'type': CIntType('c_int'),
        'type_name': 'VkPipelineBindPoint',
        'enum': 'VkPipelineBindPoint',
        'is_string': False,
    },
    'pipeline': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'indirectCommandsLayout': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'streamCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pStreams': {
        'type': CPointerType(CComplexType('VkIndirectCommandsStreamNV')),
        'type_name': 'VkIndirectCommandsStreamNV',
        'structure': 'VkIndirectCommandsStreamNV',
        'length': [['streamCount']],
        'is_string': False,
    },
    'sequencesCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'preprocessBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'preprocessOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'preprocessSize': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'sequencesCountBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'sequencesCountOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
    'sequencesIndexBuffer': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'sequencesIndexOffset': {
        'type': CIntType('c_uint64'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkIndirectCommandsStreamNV',
}
_included_in_ = set()
_input_of_ = {
    'vkCmdExecuteGeneratedCommandsNV',
    'vkCmdPreprocessGeneratedCommandsNV',
}
_output_of_ = set()
