import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('size', ctypes.c_uint64),
        ('alignment', ctypes.c_uint64),
        ('memoryTypeBits', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': {
        'VkMemoryRequirements2',
        'VkVideoSessionMemoryRequirementsKHR',
    },
    'input_of': set(),
    'output_of': {
        'vkGetBufferMemoryRequirements',
        'vkGetImageMemoryRequirements',
    },
    'member_map': {
        'size': {'python_name': ['size']},
        'alignment': {'python_name': ['alignment']},
        'memoryTypeBits': {'python_name': ['memory', 'type', 'bits']},
    }
}
