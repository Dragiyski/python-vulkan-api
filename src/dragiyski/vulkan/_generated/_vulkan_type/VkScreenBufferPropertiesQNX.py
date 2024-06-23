import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('allocationSize', ctypes.c_uint64),
        ('memoryTypeBits', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkScreenBufferFormatPropertiesQNX',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetScreenBufferPropertiesQNX',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_SCREEN_BUFFER_PROPERTIES_QNX', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'allocationSize': {'python_name': ['allocation', 'size']},
        'memoryTypeBits': {'python_name': ['memory', 'type', 'bits']},
    }
}
