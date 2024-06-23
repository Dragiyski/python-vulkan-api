import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('binding', ctypes.c_uint32),
        ('descriptorType', ctypes.c_int),
        ('descriptorCount', ctypes.c_uint32),
        ('stageFlags', ctypes.c_uint32),
        ('pImmutableSamplers', ctypes.POINTER(ctypes.c_void_p)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkDescriptorSetLayoutCreateInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'binding': {'python_name': ['binding']},
        'descriptorType': {'python_name': ['descriptor', 'type'], 'type': 'VkDescriptorType'},
        'descriptorCount': {'python_name': ['descriptor', 'count']},
        'stageFlags': {'python_name': ['stage', 'flags'], 'type': 'VkShaderStageFlags'},
        'pImmutableSamplers': {'python_name': ['p', 'immutable', 'samplers'], 'len': [['descriptorCount']]},
    }
}
