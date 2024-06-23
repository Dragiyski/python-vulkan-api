import ctypes

class CType(ctypes.Structure):
    pass

from .VkDescriptorUpdateTemplateEntry import CType as VkDescriptorUpdateTemplateEntry

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('descriptorUpdateEntryCount', ctypes.c_uint32),
    ('pDescriptorUpdateEntries', ctypes.POINTER(VkDescriptorUpdateTemplateEntry)),
    ('templateType', ctypes.c_int),
    ('descriptorSetLayout', ctypes.c_void_p),
    ('pipelineBindPoint', ctypes.c_int),
    ('pipelineLayout', ctypes.c_void_p),
    ('set', ctypes.c_uint32),
]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': {
        'VkDescriptorUpdateTemplateEntry',
    },
    'included_in': set(),
    'input_of': {
        'vkCreateDescriptorUpdateTemplate',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_UPDATE_TEMPLATE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkDescriptorUpdateTemplateCreateFlags'},
        'descriptorUpdateEntryCount': {'python_name': ['descriptor', 'update', 'entry', 'count']},
        'pDescriptorUpdateEntries': {'python_name': ['p', 'descriptor', 'update', 'entries'], 'len': [['descriptorUpdateEntryCount']], 'type': 'VkDescriptorUpdateTemplateEntry'},
        'templateType': {'python_name': ['template', 'type'], 'type': 'VkDescriptorUpdateTemplateType'},
        'descriptorSetLayout': {'python_name': ['descriptor', 'set', 'layout']},
        'pipelineBindPoint': {'python_name': ['pipeline', 'bind', 'point'], 'type': 'VkPipelineBindPoint'},
        'pipelineLayout': {'python_name': ['pipeline', 'layout']},
        'set': {'python_name': ['set']},
    }
}
