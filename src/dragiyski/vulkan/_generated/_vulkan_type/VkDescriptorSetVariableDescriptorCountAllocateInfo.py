import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorSetCount', ctypes.c_uint32),
        ('pDescriptorCounts', ctypes.POINTER(ctypes.c_uint32)),
    ]

descriptor = {
    'extends': {
        'VkDescriptorSetAllocateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_VARIABLE_DESCRIPTOR_COUNT_ALLOCATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'descriptorSetCount': {'python_name': ['descriptor', 'set', 'count']},
        'pDescriptorCounts': {'python_name': ['p', 'descriptor', 'counts'], 'len': [['descriptorSetCount']]},
    }
}
