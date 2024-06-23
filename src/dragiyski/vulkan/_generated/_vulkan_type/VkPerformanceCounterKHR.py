import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('unit', ctypes.c_int),
        ('scope', ctypes.c_int),
        ('storage', ctypes.c_int),
        ('uuid', ctypes.ARRAY(ctypes.c_uint8, 16)),
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
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PERFORMANCE_COUNTER_KHR', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'unit': {'python_name': ['unit'], 'type': 'VkPerformanceCounterUnitKHR'},
        'scope': {'python_name': ['scope'], 'type': 'VkPerformanceCounterScopeKHR'},
        'storage': {'python_name': ['storage'], 'type': 'VkPerformanceCounterStorageKHR'},
        'uuid': {'python_name': ['uuid']},
    }
}
