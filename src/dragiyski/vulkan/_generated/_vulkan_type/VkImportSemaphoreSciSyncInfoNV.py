import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('semaphore', ctypes.c_void_p),
        ('handleType', ctypes.c_uint32),
        ('handle', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkImportSemaphoreSciSyncObjNV',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMPORT_SEMAPHORE_SCI_SYNC_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'semaphore': {'python_name': ['semaphore'], 'externsync': [['true']]},
        'handleType': {'python_name': ['handle', 'type'], 'type': 'VkExternalSemaphoreHandleTypeFlagBits'},
        'handle': {'python_name': ['handle']},
    }
}
