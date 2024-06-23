import ctypes

class CType(ctypes.Structure):
    pass

from .VkWriteDescriptorSet import CType as VkWriteDescriptorSet

CType._fields_ = [
    ('sType', ctypes.c_int),
    ('pNext', ctypes.c_void_p),
    ('stageFlags', ctypes.c_uint32),
    ('layout', ctypes.c_void_p),
    ('set', ctypes.c_uint32),
    ('descriptorWriteCount', ctypes.c_uint32),
    ('pDescriptorWrites', ctypes.POINTER(VkWriteDescriptorSet)),
]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkPipelineLayoutCreateInfo',
    },
    'includes': {
        'VkWriteDescriptorSet',
    },
    'included_in': set(),
    'input_of': {
        'vkCmdPushDescriptorSet2KHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PUSH_DESCRIPTOR_SET_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'stageFlags': {'python_name': ['stage', 'flags'], 'type': 'VkShaderStageFlags'},
        'layout': {'python_name': ['layout']},
        'set': {'python_name': ['set']},
        'descriptorWriteCount': {'python_name': ['descriptor', 'write', 'count']},
        'pDescriptorWrites': {'python_name': ['p', 'descriptor', 'writes'], 'len': [['descriptorWriteCount']], 'type': 'VkWriteDescriptorSet'},
    }
}
