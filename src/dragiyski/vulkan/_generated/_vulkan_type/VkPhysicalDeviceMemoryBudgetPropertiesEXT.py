import ctypes

class CType(ctypes.Structure):
    _fields_ = [
        ('sType', ctypes.c_int),
        ('pNext', ctypes.c_void_p),
        ('heapBudget', ctypes.ARRAY(ctypes.c_uint64, 16)),
        ('heapUsage', ctypes.ARRAY(ctypes.c_uint64, 16)),
    ]

descriptor = {
    'extends': {
        'VkPhysicalDeviceMemoryProperties2',
    },
    'extended_by': set(),
    'includes': set(),
    'included_in': set(),
    'input_of': set(),
    'output_of': set(),
    'member_map': {
        'sType': {'python_name': ['s', 'type'], 'value': 'VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_MEMORY_BUDGET_PROPERTIES_EXT', 'type': 'VkStructureType'},
        'pNext': {'python_name': ['p', 'next']},
        'heapBudget': {'python_name': ['heap', 'budget']},
        'heapUsage': {'python_name': ['heap', 'usage']},
    }
}
