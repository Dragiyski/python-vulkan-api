import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('size', ctypes.c_uint64),
        ('flags', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkPhysicalDeviceMemoryProperties',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'size': {'python_name': ['size']},
        'flags': {'python_name': ['flags'], 'type': 'VkMemoryHeapFlags'},
    }
}
