import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('deviceUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('driverUUID', ctypes.ARRAY(ctypes.c_uint8, 16)),
        ('deviceLUID', ctypes.ARRAY(ctypes.c_uint8, 8)),
        ('deviceNodeMask', ctypes.c_uint32),
        ('deviceLUIDValid', ctypes.c_uint32),
        ('subgroupSize', ctypes.c_uint32),
        ('subgroupSupportedStages', ctypes.c_uint32),
        ('subgroupSupportedOperations', ctypes.c_uint32),
        ('subgroupQuadOperationsInAllStages', ctypes.c_uint32),
        ('pointClippingBehavior', ctypes.c_int),
        ('maxMultiviewViewCount', ctypes.c_uint32),
        ('maxMultiviewInstanceIndex', ctypes.c_uint32),
        ('protectedNoFault', ctypes.c_uint32),
        ('maxPerSetDescriptors', ctypes.c_uint32),
        ('maxMemoryAllocationSize', ctypes.c_uint64),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_VULKAN_1_1_PROPERTIES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'deviceUUID': {'python_name': ['device', 'uuid']},
        'driverUUID': {'python_name': ['driver', 'uuid']},
        'deviceLUID': {'python_name': ['device', 'luid']},
        'deviceNodeMask': {'python_name': ['device', 'node', 'mask']},
        'deviceLUIDValid': {'python_name': ['device', 'luidvalid']},
        'subgroupSize': {'python_name': ['subgroup', 'size']},
        'subgroupSupportedStages': {'python_name': ['subgroup', 'supported', 'stages'], 'type': 'VkShaderStageFlags'},
        'subgroupSupportedOperations': {'python_name': ['subgroup', 'supported', 'operations'], 'type': 'VkSubgroupFeatureFlags'},
        'subgroupQuadOperationsInAllStages': {'python_name': ['subgroup', 'quad', 'operations', 'in', 'all', 'stages']},
        'pointClippingBehavior': {'python_name': ['point', 'clipping', 'behavior'], 'type': 'VkPointClippingBehavior'},
        'maxMultiviewViewCount': {'python_name': ['max', 'multiview', 'view', 'count']},
        'maxMultiviewInstanceIndex': {'python_name': ['max', 'multiview', 'instance', 'index']},
        'protectedNoFault': {'python_name': ['protected', 'no', 'fault']},
        'maxPerSetDescriptors': {'python_name': ['max', 'per', 'set', 'descriptors']},
        'maxMemoryAllocationSize': {'python_name': ['max', 'memory', 'allocation', 'size']},
    }
}
