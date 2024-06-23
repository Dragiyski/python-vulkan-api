import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorPool', ctypes.c_void_p),
        ('descriptorSetCount', ctypes.c_uint32),
        ('pSetLayouts', ctypes.POINTER(ctypes.c_void_p)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkDescriptorSetVariableDescriptorCountAllocateInfo',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkAllocateDescriptorSets',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_ALLOCATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'descriptorPool': {'python_name': ['descriptor', 'pool']},
        'descriptorSetCount': {'python_name': ['descriptor', 'set', 'count']},
        'pSetLayouts': {'python_name': ['p', 'set', 'layouts'], 'len': [['descriptorSetCount']]},
    }
}
