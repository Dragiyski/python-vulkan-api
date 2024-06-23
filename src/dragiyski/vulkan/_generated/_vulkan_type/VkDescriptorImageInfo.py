import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sampler', ctypes.c_void_p),
        ('imageView', ctypes.c_void_p),
        ('imageLayout', ctypes.c_int),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkDescriptorDataEXT',
        'VkWriteDescriptorSet',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sampler': {'python_name': ['sampler']},
        'imageView': {'python_name': ['image', 'view']},
        'imageLayout': {'python_name': ['image', 'layout'], 'type': 'VkImageLayout'},
    }
}
