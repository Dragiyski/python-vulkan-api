import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('queueFamilyIndex', ctypes.c_uint32),
        ('queueCount', ctypes.c_uint32),
        ('pQueuePriorities', ctypes.POINTER(ctypes.c_float)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': {
        'VkDeviceQueueGlobalPriorityCreateInfoKHR',
        'VkDeviceQueueShaderCoreControlCreateInfoARM',
    },
    'includes': set(),
    'included_in': {
        'VkDeviceCreateInfo',
    },
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_DEVICE_QUEUE_CREATE_INFO', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkDeviceQueueCreateFlags'},
        'queueFamilyIndex': {'python_name': ['queue', 'family', 'index']},
        'queueCount': {'python_name': ['queue', 'count']},
        'pQueuePriorities': {'python_name': ['p', 'queue', 'priorities'], 'len': [['queueCount']]},
    }
}
