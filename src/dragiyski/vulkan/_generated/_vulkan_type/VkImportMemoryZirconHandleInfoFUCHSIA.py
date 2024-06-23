import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('handleType', ctypes.c_uint32),
        ('handle', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMPORT_MEMORY_ZIRCON_HANDLE_INFO_FUCHSIA', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'handleType': {'python_name': ['handle', 'type'], 'type': 'VkExternalMemoryHandleTypeFlagBits'},
        'handle': {'python_name': ['handle']},
    }
}
