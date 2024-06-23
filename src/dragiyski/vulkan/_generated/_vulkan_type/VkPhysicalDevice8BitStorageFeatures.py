import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('storageBuffer8BitAccess', ctypes.c_uint32),
        ('uniformAndStorageBuffer8BitAccess', ctypes.c_uint32),
        ('storagePushConstant8', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_8BIT_STORAGE_FEATURES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'storageBuffer8BitAccess': {'python_name': ['storage', 'buffer8', 'bit', 'access']},
        'uniformAndStorageBuffer8BitAccess': {'python_name': ['uniform', 'and', 'storage', 'buffer8', 'bit', 'access']},
        'storagePushConstant8': {'python_name': ['storage', 'push', 'constant8']},
    }
}
