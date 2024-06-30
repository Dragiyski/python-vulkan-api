from ..._ctypes import *

_category_ = 'structure'
_name_ = 'VkDescriptorUpdateTemplateCreateInfo'
_member_list_ = ['sType', 'pNext', 'flags', 'descriptorUpdateEntryCount', 'pDescriptorUpdateEntries', 'templateType', 'descriptorSetLayout', 'pipelineBindPoint', 'pipelineLayout', 'set']
_member_info_ = {
    'sType': {
        'type': CIntType('c_int'),
        'type_name': 'VkStructureType',
        'enum': 'VkStructureType',
        'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_UPDATE_TEMPLATE_CREATE_INFO',
        'is_string': False,
    },
    'pNext': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'flags': {
        'type': CIntType('c_uint32'),
        'type_name': 'VkDescriptorUpdateTemplateCreateFlags',
        'enum': 'VkDescriptorUpdateTemplateCreateFlags',
        'is_string': False,
    },
    'descriptorUpdateEntryCount': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
    'pDescriptorUpdateEntries': {
        'type': CPointerType(CComplexType('VkDescriptorUpdateTemplateEntry')),
        'type_name': 'VkDescriptorUpdateTemplateEntry',
        'structure': 'VkDescriptorUpdateTemplateEntry',
        'length': [['descriptorUpdateEntryCount']],
        'is_string': False,
    },
    'templateType': {
        'type': CIntType('c_int'),
        'type_name': 'VkDescriptorUpdateTemplateType',
        'enum': 'VkDescriptorUpdateTemplateType',
        'is_string': False,
    },
    'descriptorSetLayout': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'pipelineBindPoint': {
        'type': CIntType('c_int'),
        'type_name': 'VkPipelineBindPoint',
        'enum': 'VkPipelineBindPoint',
        'is_string': False,
    },
    'pipelineLayout': {
        'type': CIntType('c_void_p'),
        'is_string': False,
    },
    'set': {
        'type': CIntType('c_uint32'),
        'is_string': False,
    },
}
_extends_ = set()
_extended_by_ = set()
_includes_ = {
    'VkDescriptorUpdateTemplateEntry',
}
_included_in_ = set()
_input_of_ = {
    'vkCreateDescriptorUpdateTemplate',
}
_output_of_ = set()
