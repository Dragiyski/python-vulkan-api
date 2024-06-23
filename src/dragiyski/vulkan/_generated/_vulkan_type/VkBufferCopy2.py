import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('srcOffset', ctypes.c_uint64),
        ('dstOffset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkCopyBufferInfo2',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_BUFFER_COPY_2', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'srcOffset': {'python_name': ['src', 'offset']},
        'dstOffset': {'python_name': ['dst', 'offset']},
        'size': {'python_name': ['size']},
    }
}
