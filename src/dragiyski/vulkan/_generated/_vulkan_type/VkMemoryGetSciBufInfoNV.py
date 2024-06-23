import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('memory', ctypes.c_void_p),
        ('handleType', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetMemorySciBufNV',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_MEMORY_GET_SCI_BUF_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'memory': {'python_name': ['memory']},
        'handleType': {'python_name': ['handle', 'type'], 'type': 'VkExternalMemoryHandleTypeFlagBits'},
    }
}
