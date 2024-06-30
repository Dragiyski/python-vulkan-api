from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkSetDescriptorBufferOffsetsInfoEXT'
_member_list_ = ['sType', 'pNext', 'stageFlags', 'layout', 'firstSet', 'setCount', 'pBufferIndices', 'pOffsets']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_SET_DESCRIPTOR_BUFFER_OFFSETS_INFO_EXT',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'stageFlags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkShaderStageFlags',
        'enum': 'VkShaderStageFlags',
        'is_string': False,
    },
    'layout': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'firstSet': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'setCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pBufferIndices': {
        'type': CPointerType(CIntType('c_uint32')),
        'length': [['setCount']],
        'is_string': False,
    },
    'pOffsets': {
        'type': CPointerType(CIntType('c_uint64')),
        'length': [['setCount']],
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = {
    'VkPipelineLayoutCreateInfo',
}
_includes_ = set()
_included_in_ = set()
_input_of_ = {
    'vkCmdSetDescriptorBufferOffsets2EXT',
}
_output_of_ = set()
