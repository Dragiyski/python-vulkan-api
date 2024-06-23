import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('flags', ctypes.c_uint32),
        ('name', ctypes.ARRAY(ctypes.c_char, 256)),
        ('category', ctypes.ARRAY(ctypes.c_char, 256)),
        ('description', ctypes.ARRAY(ctypes.c_char, 256)),
    ]

descriptor = {
    'extends': set(),
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': {
        'vkEnumeratePhysicalDeviceQueueFamilyPerformanceQueryCountersKHR',
    },
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PERFORMANCE_COUNTER_DESCRIPTION_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'flags': {'python_name': ['flags'], 'type': 'VkPerformanceCounterDescriptionFlagsKHR'},
        'name': {'python_name': ['name'], 'len': [['null-terminated']]},
        'category': {'python_name': ['category'], 'len': [['null-terminated']]},
        'description': {'python_name': ['description'], 'len': [['null-terminated']]},
    }
}
