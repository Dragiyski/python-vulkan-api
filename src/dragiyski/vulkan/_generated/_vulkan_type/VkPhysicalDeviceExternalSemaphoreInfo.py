import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('handleType', ctypes.c_uint32),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkSemaphoreTypeCreateInfo',
    },
    'includes': set(),
    'included_in': set(),
    'input_of': {
        'vkGetPhysicalDeviceExternalSemaphoreProperties',
    },
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_EXTERNAL_SEMAPHORE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'handleType': {'python_name': ['handle', 'type'], 'type': 'VkExternalSemaphoreHandleTypeFlagBits'},
    }
}
