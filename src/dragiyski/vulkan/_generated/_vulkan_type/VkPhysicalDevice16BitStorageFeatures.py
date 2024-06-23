import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('storageBuffer16BitAccess', ctypes.c_uint32),
        ('uniformAndStorageBuffer16BitAccess', ctypes.c_uint32),
        ('storagePushConstant16', ctypes.c_uint32),
        ('storageInputOutput16', ctypes.c_uint32),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_16BIT_STORAGE_FEATURES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'storageBuffer16BitAccess': {'python_name': ['storage', 'buffer16', 'bit', 'access']},
        'uniformAndStorageBuffer16BitAccess': {'python_name': ['uniform', 'and', 'storage', 'buffer16', 'bit', 'access']},
        'storagePushConstant16': {'python_name': ['storage', 'push', 'constant16']},
        'storageInputOutput16': {'python_name': ['storage', 'input', 'output16']},
    }
}
