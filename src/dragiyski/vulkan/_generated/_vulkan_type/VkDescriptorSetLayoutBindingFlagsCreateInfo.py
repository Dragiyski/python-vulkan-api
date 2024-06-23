import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('bindingCount', ctypes.c_uint32),
        ('pBindingFlags', ctypes.POINTER(ctypes.c_uint32)),
    ]

descriptor = {
    'extends': {
        'VkDescriptorSetLayoutCreateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DESCRIPTOR_SET_LAYOUT_BINDING_FLAGS_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'bindingCount': {'python_name': ['binding', 'count']},
        'pBindingFlags': {'python_name': ['p', 'binding', 'flags'], 'len': [['bindingCount']], 'type': 'VkDescriptorBindingFlags'},
    }
}
