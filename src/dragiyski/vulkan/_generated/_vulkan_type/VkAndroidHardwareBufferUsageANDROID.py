import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('androidHardwareBufferUsage', ctypes.c_uint64),
    ]

descriptor = {
    'extends': {
        'VkImageFormatProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_ANDROID_HARDWARE_BUFFER_USAGE_ANDROID', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'androidHardwareBufferUsage': {'python_name': ['android', 'hardware', 'buffer', 'usage']},
    }
}
