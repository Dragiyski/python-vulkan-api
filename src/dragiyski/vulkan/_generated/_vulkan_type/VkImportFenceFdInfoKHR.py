import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fence', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('handleType', ctypes.c_uint32),
        ('fd', ctypes.c_int),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkImportFenceFdKHR',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMPORT_FENCE_FD_INFO_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'fence': {'python_name': ['fence'], 'externsync': [['true']]},
        'flags': {'python_name': ['flags'], 'type': 'VkFenceImportFlags'},
        'handleType': {'python_name': ['handle', 'type'], 'type': 'VkExternalFenceHandleTypeFlagBits'},
        'fd': {'python_name': ['fd']},
    }
}
