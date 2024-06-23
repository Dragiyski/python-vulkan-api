import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('descriptorSetLayout', ctypes.c_void_p),
        ('binding', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetDescriptorSetLayoutHostMappingInfoVALVE',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_BINDING_REFERENCE_VALVE', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'descriptorSetLayout': {'python_name': ['descriptor', 'set', 'layout']},
        'binding': {'python_name': ['binding']},
    }
}
