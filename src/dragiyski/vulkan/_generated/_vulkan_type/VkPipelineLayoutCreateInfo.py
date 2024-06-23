import ctypes

class CType(ctypes.Structure):
    pass

from .VkPushConstantRange import CType as VkPushConstantRange

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('flags', ctypes.c_uint32),
    ('setLayoutCount', ctypes.c_uint32),
    ('pSetLayouts', ctypes.POINTER(ctypes.c_void_p)),
    ('pushConstantRangeCount', ctypes.c_uint32),
    ('pPushConstantRanges', ctypes.POINTER(VkPushConstantRange)),
]

descriptor = {
    'extends': {
        'VkBindDescriptorBufferEmbeddedSamplersInfoEXT',
        'VkBindDescriptorSetsInfoKHR',
        'VkPushConstantsInfoKHR',
        'VkPushDescriptorSetInfoKHR',
        'VkPushDescriptorSetWithTemplateInfoKHR',
        'VkSetDescriptorBufferOffsetsInfoEXT',
    },
    'extended_by': set(),
    'includes': {
        'VkPushConstantRange',
    },
    'included_in': set(),
    'input_of': {
        'vkCreatePipelineLayout',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PIPELINE_LAYOUT_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPipelineLayoutCreateFlags'},
        'setLayoutCount': {'python_name': ['set', 'layout', 'count']},
        'pSetLayouts': {'python_name': ['p', 'set', 'layouts'], 'len': [['setLayoutCount']]},
        'pushConstantRangeCount': {'python_name': ['push', 'constant', 'range', 'count']},
        'pPushConstantRanges': {'python_name': ['p', 'push', 'constant', 'ranges'], 'len': [['pushConstantRangeCount']], 'type': 'VkPushConstantRange'},
    }
}
