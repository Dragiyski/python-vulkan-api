import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('supported', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkDescriptorSetVariableDescriptorCountLayoutSupport',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetDescriptorSetLayoutSupport',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_SUPPORT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'supported': {'python_name': ['supported']},
    }
}
