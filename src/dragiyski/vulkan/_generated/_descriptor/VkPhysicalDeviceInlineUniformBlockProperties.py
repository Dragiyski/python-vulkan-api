from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkPhysicalDeviceInlineUniformBlockProperties'
_member_list_ = ['sType', 'pNext', 'maxInlineUniformBlockSize', 'maxPerStageDescriptorInlineUniformBlocks', 'maxPerStageDescriptorUpdateAfterBindInlineUniformBlocks', 'maxDescriptorSetInlineUniformBlocks', 'maxDescriptorSetUpdateAfterBindInlineUniformBlocks']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_INLINE_UNIFORM_BLOCK_PROPERTIES',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'maxInlineUniformBlockSize': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPerStageDescriptorInlineUniformBlocks': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxPerStageDescriptorUpdateAfterBindInlineUniformBlocks': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetInlineUniformBlocks': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'maxDescriptorSetUpdateAfterBindInlineUniformBlocks': {
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
