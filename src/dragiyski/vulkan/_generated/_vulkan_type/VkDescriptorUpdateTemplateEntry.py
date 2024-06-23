import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('dstBinding', ctypes.c_uint32),
        ('dstArrayElement', ctypes.c_uint32),
        ('descriptorCount', ctypes.c_uint32),
        ('descriptorType', ctypes.c_int),
        ('offset', ctypes.c_size_t),
        ('stride', ctypes.c_size_t),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkDescriptorUpdateTemplateCreateInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'dstBinding': {'python_name': ['dst', 'binding']},
        'dstArrayElement': {'python_name': ['dst', 'array', 'element']},
        'descriptorCount': {'python_name': ['descriptor', 'count']},
        'descriptorType': {'python_name': ['descriptor', 'type'], 'type': 'VkDescriptorType'},
        'offset': {'python_name': ['offset']},
        'stride': {'python_name': ['stride']},
    }
}
