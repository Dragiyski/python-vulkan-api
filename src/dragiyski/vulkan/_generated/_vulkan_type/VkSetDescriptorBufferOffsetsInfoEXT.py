import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stageFlags', ctypes.c_uint32),
        ('layout', ctypes.c_void_p),
        ('firstSet', ctypes.c_uint32),
        ('setCount', ctypes.c_uint32),
        ('pBufferIndices', ctypes.POINTER(ctypes.c_uint32)),
        ('pOffsets', ctypes.POINTER(ctypes.c_uint64)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkPipelineLayoutCreateInfo',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdSetDescriptorBufferOffsets2EXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SET_DESCRIPTOR_BUFFER_OFFSETS_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'stageFlags': {'python_name': ['stage', 'flags'], 'type': 'VkShaderStageFlags'},
        'layout': {'python_name': ['layout']},
        'firstSet': {'python_name': ['first', 'set']},
        'setCount': {'python_name': ['set', 'count']},
        'pBufferIndices': {'python_name': ['p', 'buffer', 'indices'], 'len': [['setCount']]},
        'pOffsets': {'python_name': ['p', 'offsets'], 'len': [['setCount']]},
    }
}
