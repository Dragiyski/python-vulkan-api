import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('sciSyncFence', ctypes.c_uint32),
        ('sciSyncSemaphore2', ctypes.c_uint32),
        ('sciSyncImport', ctypes.c_uint32),
        ('sciSyncExport', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkDeviceCreateInfo',
        'VkPhysicalDeviceFeatures2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_SCI_SYNC_2_FEATURES_NV', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'sciSyncFence': {'python_name': ['sci', 'sync', 'fence']},
        'sciSyncSemaphore2': {'python_name': ['sci', 'sync', 'semaphore2']},
        'sciSyncImport': {'python_name': ['sci', 'sync', 'import']},
        'sciSyncExport': {'python_name': ['sci', 'sync', 'export']},
    }
}
