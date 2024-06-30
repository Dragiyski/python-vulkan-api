from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkGeneratedCommandsMemoryRequirementsInfoNV'
_member_list_ = ['sType', 'pNext', 'pipelineBindPoint', 'pipeline', 'indirectCommandsLayout', 'maxSequencesCount']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_GENERATED_COMMANDS_MEMORY_REQUIREMENTS_INFO_NV',
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
    'maxSequencesCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkGetGeneratedCommandsMemoryRequirementsNV',
}
_output_of_ = set()
