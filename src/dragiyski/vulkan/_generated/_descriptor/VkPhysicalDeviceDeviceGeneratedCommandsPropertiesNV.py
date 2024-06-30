from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceDeviceGeneratedCommandsPropertiesNV'
_member_list_ = ['sType', 'pNext', 'maxGraphicsShaderGroupCount', 'maxIndirectSequenceCount', 'maxIndirectCommandsTokenCount', 'maxIndirectCommandsStreamCount', 'maxIndirectCommandsTokenOffset', 'maxIndirectCommandsStreamStride', 'minSequencesCountBufferOffsetAlignment', 'minSequencesIndexBufferOffsetAlignment', 'minIndirectCommandsBufferOffsetAlignment']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_DEVICE_GENERATED_COMMANDS_PROPERTIES_NV',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'maxGraphicsShaderGroupCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxIndirectSequenceCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxIndirectCommandsTokenCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxIndirectCommandsStreamCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxIndirectCommandsTokenOffset': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxIndirectCommandsStreamStride': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'minSequencesCountBufferOffsetAlignment': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'minSequencesIndexBufferOffsetAlignment': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'minIndirectCommandsBufferOffsetAlignment': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = {
    'VkPhysicalDeviceProperties2',
}
_extended_by_ = set()
_includes_ = set()
_included_in_ = set()
_input_of_ = set()
_output_of_ = set()
