import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('dataSize', ctypes.c_uint32),
        ('pData', ctypes.c_void_p),
    ]

descriptor = {
    'extends': {
        'VkWriteDescriptorSet',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_WRITE_DESCRIPTOR_SET_INLINE_UNIFORM_BLOCK', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'dataSize': {'python_name': ['data', 'size']},
        'pData': {'python_name': ['p', 'data'], 'len': [['dataSize']]},
    }
}
