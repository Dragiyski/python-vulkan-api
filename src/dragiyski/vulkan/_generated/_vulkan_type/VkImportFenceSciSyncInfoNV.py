import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('fence', ctypes.c_void_p),
        ('handleType', ctypes.c_uint32),
        ('handle', ctypes.c_void_p),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkImportFenceSciSyncFenceNV',
        'vkImportFenceSciSyncObjNV',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_IMPORT_FENCE_SCI_SYNC_INFO_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'fence': {'python_name': ['fence'], 'externsync': [['true']]},
        'handleType': {'python_name': ['handle', 'type'], 'type': 'VkExternalFenceHandleTypeFlagBits'},
        'handle': {'python_name': ['handle']},
    }
}
