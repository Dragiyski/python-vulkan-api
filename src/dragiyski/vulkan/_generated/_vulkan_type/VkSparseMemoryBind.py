import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('resourceOffset', ctypes.c_uint64),
        ('size', ctypes.c_uint64),
        ('memory', ctypes.c_void_p),
        ('memoryOffset', ctypes.c_uint64),
        ('flags', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkSparseBufferMemoryBindInfo',
        'VkSparseImageOpaqueMemoryBindInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'resourceOffset': {'python_name': ['resource', 'offset']},
        'size': {'python_name': ['size']},
        'memory': {'python_name': ['memory']},
        'memoryOffset': {'python_name': ['memory', 'offset']},
        'flags': {'python_name': ['flags'], 'type': 'VkSparseMemoryBindFlags'},
    }
}
