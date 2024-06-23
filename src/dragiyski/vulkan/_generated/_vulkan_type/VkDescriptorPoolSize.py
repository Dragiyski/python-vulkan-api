import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('type', ctypes.c_int),
        ('descriptorCount', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkDescriptorPoolCreateInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'type': {'python_name': ['type'], 'type': 'VkDescriptorType'},
        'descriptorCount': {'python_name': ['descriptor', 'count']},
    }
}
