import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('handleType', ctypes.c_uint32),
        ('fd', ctypes.c_int),
    ]

descriptor = {
    'extends': {
        'VkMemoryAllocateInfo',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMPORT_MEMORY_FD_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'handleType': {'python_name': ['handle', 'type'], 'type': 'VkExternalMemoryHandleTypeFlagBits'},
        'fd': {'python_name': ['fd']},
    }
}
