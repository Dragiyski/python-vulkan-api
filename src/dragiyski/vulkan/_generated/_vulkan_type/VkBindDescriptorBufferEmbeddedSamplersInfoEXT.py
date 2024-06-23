import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('stageFlags', ctypes.c_uint32),
        ('layout', ctypes.c_void_p),
        ('set', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkPipelineLayoutCreateInfo',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkCmdBindDescriptorBufferEmbeddedSamplers2EXT',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BIND_DESCRIPTOR_BUFFER_EMBEDDED_SAMPLERS_INFO_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'stageFlags': {'python_name': ['stage', 'flags'], 'type': 'VkShaderStageFlags'},
        'layout': {'python_name': ['layout']},
        'set': {'python_name': ['set']},
    }
}
