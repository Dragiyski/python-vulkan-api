import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('descriptorTypeCount', ctypes.c_uint32),
        ('pDescriptorTypes', ctypes.POINTER(ctypes.c_int)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkMutableDescriptorTypeCreateInfoEXT',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'descriptorTypeCount': {'python_name': ['descriptor', 'type', 'count']},
        'pDescriptorTypes': {'python_name': ['p', 'descriptor', 'types'], 'len': [['descriptorTypeCount']], 'type': 'VkDescriptorType'},
    }
}
