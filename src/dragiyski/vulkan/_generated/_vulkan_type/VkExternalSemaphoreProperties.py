import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('exportFromImportedHandleTypes', ctypes.c_uint32),
        ('compatibleHandleTypes', ctypes.c_uint32),
        ('externalSemaphoreFeatures', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkGetPhysicalDeviceExternalSemaphoreProperties',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_EXTERNAL_SEMAPHORE_PROPERTIES', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'exportFromImportedHandleTypes': {'python_name': ['export', 'from', 'imported', 'handle', 'types'], 'type': 'VkExternalSemaphoreHandleTypeFlags'},
        'compatibleHandleTypes': {'python_name': ['compatible', 'handle', 'types'], 'type': 'VkExternalSemaphoreHandleTypeFlags'},
        'externalSemaphoreFeatures': {'python_name': ['external', 'semaphore', 'features'], 'type': 'VkExternalSemaphoreFeatureFlags'},
    }
}
