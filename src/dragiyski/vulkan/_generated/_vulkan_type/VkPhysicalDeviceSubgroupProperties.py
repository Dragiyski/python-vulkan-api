import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('subgroupSize', ctypes.c_uint32),
        ('supportedStages', ctypes.c_uint32),
        ('supportedOperations', ctypes.c_uint32),
        ('quadOperationsInAllStages', ctypes.c_uint32),
    ]

descriptor = {
    'extends': {
        'VkPhysicalDeviceProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_SUBGROUP_PROPERTIES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'subgroupSize': {'python_name': ['subgroup', 'size']},
        'supportedStages': {'python_name': ['supported', 'stages'], 'type': 'VkShaderStageFlags'},
        'supportedOperations': {'python_name': ['supported', 'operations'], 'type': 'VkSubgroupFeatureFlags'},
        'quadOperationsInAllStages': {'python_name': ['quad', 'operations', 'in', 'all', 'stages']},
    }
}
