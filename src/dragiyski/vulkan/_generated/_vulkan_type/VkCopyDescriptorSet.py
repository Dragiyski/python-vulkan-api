import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcSet', ctypes.c_void_p),
        ('srcBinding', ctypes.c_uint32),
        ('srcArrayElement', ctypes.c_uint32),
        ('dstSet', ctypes.c_void_p),
        ('dstBinding', ctypes.c_uint32),
        ('dstArrayElement', ctypes.c_uint32),
        ('descriptorCount', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkUpdateDescriptorSets',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_COPY_DESCRIPTOR_SET', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'srcSet': {'python_name': ['src', 'set']},
        'srcBinding': {'python_name': ['src', 'binding']},
        'srcArrayElement': {'python_name': ['src', 'array', 'element']},
        'dstSet': {'python_name': ['dst', 'set']},
        'dstBinding': {'python_name': ['dst', 'binding']},
        'dstArrayElement': {'python_name': ['dst', 'array', 'element']},
        'descriptorCount': {'python_name': ['descriptor', 'count']},
    }
}
