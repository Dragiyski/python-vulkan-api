import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('maxInlineUniformBlockSize', ctypes.c_uint32),
        ('maxPerStageDescriptorInlineUniformBlocks', ctypes.c_uint32),
        ('maxPerStageDescriptorUpdateAfterBindInlineUniformBlocks', ctypes.c_uint32),
        ('maxDescriptorSetInlineUniformBlocks', ctypes.c_uint32),
        ('maxDescriptorSetUpdateAfterBindInlineUniformBlocks', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_INLINE_UNIFORM_BLOCK_PROPERTIES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'maxInlineUniformBlockSize': {'python_name': ['max', 'inline', 'uniform', 'block', 'size']},
        'maxPerStageDescriptorInlineUniformBlocks': {'python_name': ['max', 'per', 'stage', 'descriptor', 'inline', 'uniform', 'blocks']},
        'maxPerStageDescriptorUpdateAfterBindInlineUniformBlocks': {'python_name': ['max', 'per', 'stage', 'descriptor', 'update', 'after', 'bind', 'inline', 'uniform', 'blocks']},
        'maxDescriptorSetInlineUniformBlocks': {'python_name': ['max', 'descriptor', 'set', 'inline', 'uniform', 'blocks']},
        'maxDescriptorSetUpdateAfterBindInlineUniformBlocks': {'python_name': ['max', 'descriptor', 'set', 'update', 'after', 'bind', 'inline', 'uniform', 'blocks']},
    }
}
