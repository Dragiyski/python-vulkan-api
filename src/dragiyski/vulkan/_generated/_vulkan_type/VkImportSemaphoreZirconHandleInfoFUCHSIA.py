import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphore', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('handleType', ctypes.c_uint32),
        ('zirconHandle', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkImportSemaphoreZirconHandleFUCHSIA',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMPORT_SEMAPHORE_ZIRCON_HANDLE_INFO_FUCHSIA', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'semaphore': {'python_name': ['semaphore'], 'externsync': [['true']]},
        'flags': {'python_name': ['flags'], 'type': 'VkSemaphoreImportFlags'},
        'handleType': {'python_name': ['handle', 'type'], 'type': 'VkExternalSemaphoreHandleTypeFlagBits'},
        'zirconHandle': {'python_name': ['zircon', 'handle']},
    }
}
