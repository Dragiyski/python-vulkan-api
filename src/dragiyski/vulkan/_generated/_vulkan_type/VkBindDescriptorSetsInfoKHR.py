import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stageFlags', ctypes.c_uint32),
        ('layout', ctypes.c_void_p),
        ('firstSet', ctypes.c_uint32),
        ('descriptorSetCount', ctypes.c_uint32),
        ('pDescriptorSets', ctypes.POINTER(ctypes.c_void_p)),
        ('dynamicOffsetCount', ctypes.c_uint32),
        ('pDynamicOffsets', ctypes.POINTER(ctypes.c_uint32)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkPipelineLayoutCreateInfo',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdBindDescriptorSets2KHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BIND_DESCRIPTOR_SETS_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'stageFlags': {'python_name': ['stage', 'flags'], 'type': 'VkShaderStageFlags'},
        'layout': {'python_name': ['layout']},
        'firstSet': {'python_name': ['first', 'set']},
        'descriptorSetCount': {'python_name': ['descriptor', 'set', 'count']},
        'pDescriptorSets': {'python_name': ['p', 'descriptor', 'sets'], 'len': [['descriptorSetCount']]},
        'dynamicOffsetCount': {'python_name': ['dynamic', 'offset', 'count']},
        'pDynamicOffsets': {'python_name': ['p', 'dynamic', 'offsets'], 'len': [['dynamicOffsetCount']]},
    }
}
